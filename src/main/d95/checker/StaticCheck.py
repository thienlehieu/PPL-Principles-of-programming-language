#student's id: 1613318
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from StaticError import *
from functools import *

class Visitor(ABC):
    def visit(self, ctx, o):
        return ctx.accept(self, o)

def checkMulDimArr(arr, ctx):
    if arr[0][0] != 8:
        valid = all(ele == arr[0] for ele in arr)
        if not valid:
            raise InvalidArrayLiteral(ctx)
        return [1, arr[0][1]]
    else:
        return [1] + checkMulDimArr(arr[0][1], ctx)

def checkType(ltyp, rtyp, ctx, inferType, acceptType, o):
    if ltyp == 0:
        for env in o[0]:
            if ctx.left.name in env:
                env[ctx.left.name] = inferType
                break
        ltyp = inferType
    if rtyp == 0:
        for env in o[0]:
            if ctx.right.name in env:
                env[ctx.right.name] = inferType
                break
        rtyp = inferType
    if rtyp not in acceptType or ltyp not in acceptType:
        raise TypeMismatchInExpr(ctx)
    return ltyp, rtyp


class StaticChecker(Visitor):
    def __init__(self,ctx):
        self.ctx = ctx

    def check(self):
        return self.visit(self.ctx, [[{}]])

    def checkCallStmt(self, ctx1, o, ctx2=None):
        if ctx2:
            if isinstance(ctx1, Call) or isinstance(ctx2, Call):
                env1 = o[:]
                env1[3] = False
                ltype = self.visit(ctx1, env1)
                rtype = self.visit(ctx2, env1)
            else:
                ltype = self.visit(ctx1, o)
                rtype = self.visit(ctx2, o)
            return ltype, rtype
        else:
            if isinstance(ctx1, Call):
                env1 = o[:]
                env1[3] = False
                ltype = self.visit(ctx1, env1)
            else:
                ltype = self.visit(ctx1, o)
            return ltype

    def visitProgram(self, ctx, o):
        o = [[{}]]

        for decl in ctx.const:
            self.visit(decl, o)

        for decl in ctx.nonconst:
            if isinstance(decl, FuncDecl):
                if decl.name.name == "_main":
                    break
        else:
            raise NoEntryPoint()

        for decl in ctx.nonconst:
            self.visit(decl, o)

    def visitConstDecl(self, ctx, o):
        for env in o[0]:
            if ctx.id.name in env:
                raise Redeclared(Const(), ctx.id.name)
        else:
            typ = self.visit(ctx.value, o)
            if isinstance(ctx.value, ArrayLit):
                if typ[0] == 8:
                    ndims = checkMulDimArr(typ[1], ctx.value)
                    typ = (8, (len(ndims), ndims[len(ndims) - 1]))
            o[0][0][ctx.id.name] = ("const", typ)

    def visitAssign(self, ctx, o):
        varName = ctx.lhs.name if isinstance(ctx.lhs, Id) else ctx.lhs.id.name
        for env in o[0]:
            if varName in env:
                if isinstance(env[varName], tuple):
                    if env[varName][0] == "const":
                        raise Redeclared("Const", varName)
                break
        else:
            o[0][0][varName] = 0

        # lhs = self.visit(ctx.lhs, o)
        # rhs = self.visit(ctx.rhs, o)

        lhs, rhs = self.checkCallStmt(ctx.lhs, o, ctx.rhs)

        def checkAssign(ctx, typ, o):
            if isinstance(ctx, ArrayAccess):
                if len(ctx.idx) > 1:
                    typInfer = (8, (len(ctx.idx), typ))
                elif isinstance(ctx.idx[0], IntLit):
                    typInfer = (9, typ)
                else:
                    typInfer = (7, [6, typ])
                for env in o[0]:
                    if ctx.id.name in env:
                        env[ctx.id.name] = typInfer
                        break
            else:
                for env in o[0]:
                    if ctx.name in env:
                        env[ctx.name] = typ
                        break

        if isinstance(ctx.rhs, ArrayLit):
            if self.visit(ctx.rhs, o)[0] == 8:
                ndims = checkMulDimArr(rhs[1], ctx.rhs)
                rhs = (8, (len(ndims), ndims[len(ndims)-1]))

        if lhs == 0:
            if rhs == 0:
                raise TypeCannotBeInferred(ctx)
            checkAssign(ctx.lhs, rhs, o)

        elif rhs == 0:
            checkAssign(ctx.rhs, lhs, o)

        elif rhs != lhs:
            if lhs == 4:
                if rhs not in [3, 5]:
                    raise TypeMismatchInStmt(ctx)
            elif lhs == 3:
                if rhs != 5:
                    raise TypeMismatchInStmt(ctx)

    def visitParamDecl(self, ctx, o):
        if ctx.id.name in o[0][0]:
            raise Redeclared(Param(), ctx.id.name)
        else:
            o[0][0][ctx.id.name] = 0

    def visitFuncDecl(self, ctx, o):
        #o = [[{}]]
        if ctx.name.name in o[0][0]:
            raise Redeclared(Func(), ctx.name.name)

        o[0][0][ctx.name.name] = []
        isInLoop = False
        isReturn = [False, 0]
        isCallStmt = True
        env = [[{}] + o[0], isInLoop, isReturn, isCallStmt]

        for param in ctx.param:
            self.visit(param, env)

        for stmt in ctx.body:
            self.visit(stmt, env)

        if not isReturn[0]:
            raise TypeMismatchInStmt(ctx)

        params = [env[0][0][param.id.name] for param in ctx.param]

        o[0][0][ctx.name.name].append(params)
        o[0][0][ctx.name.name].append(isReturn[1])


    def visitForEach(self, ctx, o):
        arrType = self.visit(ctx.arr, o)
        if not isinstance(arrType, tuple):
            raise TypeMismatchInStmt(ctx)

        env = o[:]
        env[0] = [{}] + env[0]
        env[1] = True
        #arrType = (8, (2,3))
        if arrType[0] == 7:
            env[0][0][ctx.key.name] = arrType[1][0]
            env[0][0][ctx.value.name] = arrType[1][1]
        elif arrType[0] == 8:
            env[0][0][ctx.key.name] = 3
            if arrType[1][0] == 2:
                env[0][0][ctx.value.name] = (9, arrType[1][1])
            else:
                env[0][0][ctx.value.name] = (8, (arrType[1][0] - 1, arrType[1][0]))
        else:
            env[0][0][ctx.key.name] = 3
            env[0][0][ctx.value.name] = arrType[1]

        for stmt in ctx.body:
            self.visit(stmt, env)

    def visitWhile(self, ctx, o):
        condTyp = self.checkCallStmt(ctx.cond, o)
        if condTyp != 5:
            raise TypeMismatchInStmt(ctx)

        env = o[:]
        env[0] = [{}] + env[0]
        env[1] = True
        for stmt in ctx.body:
            self.visit(stmt, env)

    def visitBreak(self, ctx, o):
        if not o[1]:
            raise TypeMismatchInStmt(ctx)

    def visitContinue(self, ctx, o):
        if not o[1]:
            raise TypeMismatchInStmt(ctx)

    def visitReturn(self, ctx, o):
        if ctx.exp != None:
            returnType = self.visit(ctx.exp, o)
            if returnType != 0 and o[2][1] != 0 and returnType != o[2][1]:
                raise TypeMismatchInStmt(ctx)
            o[2][1] = self.visit(ctx.exp, o)
        else:
            o[2][1] = -1
        o[2][0] = True

    def visitId(self, ctx, o):
        for env in o[0]:
            if ctx.name in env:
                if isinstance(env[ctx.name], tuple):
                    if env[ctx.name][0] == "const":
                        return env[ctx.name][1]
                    return env[ctx.name]
                return env[ctx.name]
        raise UndeclaredIdentifier(ctx.name)

    def visitArrayAccess(self, ctx, o):
        typ = self.visit(ctx.id, o)
        if isinstance(typ, tuple):
            if typ[0] == 7:
                if len(ctx.idx) > 1:
                    raise TypeMismatchInExpr(ctx)
                if self.visit(ctx.idx[0], o) != typ[1][0]:
                    raise TypeMismatchInExpr(ctx)
                return typ[1][1]

            if typ[0] == 8:
                nDim = typ[1][0]
                if len(ctx.idx) != nDim:
                    raise TypeMismatchInExpr(ctx)
                for exp in ctx.idx:
                    if self.visit(exp, o) != 3:
                        raise TypeMismatchInExpr(ctx)
                return typ[1][1]

            if typ[0] == 9:
                if len(ctx.idx) > 1:
                    raise TypeMismatchInExpr(ctx)
                if self.visit(ctx.idx[0], o) != 3:
                    raise TypeMismatchInExpr(ctx)
                return typ[1]
        return 0

    def visitBinExp(self, ctx, o):
        ltype, rtype = self.checkCallStmt(ctx.left, o, ctx.right)

        if ctx.op in ["+", "-", "*", "/", "%"]:
            ltype, rtype = checkType(ltype, rtype, ctx, 4, [3,4], o)
            if rtype == 4 or ltype == 4:
                return 4
            return 3

        if ctx.op in ["==", "!=", "<", ">", "<=", ">="]:
            ltype, rtype = checkType(ltype, rtype, ctx, 4, [3,4], o)
            return 5

        if ctx.op in ["&&", "||"]:
            ltype, rtype = checkType(ltype, rtype, ctx, 5, [5], o)
            return 5

        if ctx.op in ["==.", "+."]:
            ltype, rtype = checkType(ltype, rtype, ctx, 6, [6], o)
            return 5 if ctx.op == "==." else 6

    def visitUnExp(self, ctx, o):
        typ = self.checkCallStmt(ctx.exp, o)

        if ctx.op == "-":
            if typ == 0:
                for env in o:
                    if ctx.exp.name in env:
                        env[ctx.exp.name] = 4
                        break
                typ = 4

            if typ == 4: return 4
            if typ == 3: return 3
            raise TypeMismatchInExpr(ctx)

        if ctx.op == "!":
            if typ == 0:
                for env in o:
                    if ctx.exp.name in env:
                        env[ctx.exp.name] = 5
                        break
                typ = 5

            if typ == 5: return 5
            raise TypeMismatchInExpr(ctx)

    def visitAssocExp(self, ctx, o):
        value = self.checkCallStmt(ctx.value, o)
        return [self.visit(ctx.key, o), value]

    def visitCall(self, ctx, o):
        if ctx.id.name in ["str2int", "int2str", "str2float", "float2str", "str2bool", "bool2str", "_echo", "_read"]:
            if len(ctx.param) != 1:
                raise TypeMismatchInStmt(ctx)
            paramType = self.checkCallStmt(ctx.param[0], o)
            if ctx.id.name == "str2int":
                if paramType != 6:
                    raise TypeMismatchInStmt(ctx)
                return 3
            elif ctx.id.name == "int2str":
                if paramType != 3:
                    raise TypeMismatchInStmt(ctx)
                return 6
            elif ctx.id.name == "str2float":
                if paramType != 6:
                    raise TypeMismatchInStmt(ctx)
                return 4
            elif ctx.id.name == "float2str":
                if paramType != 4:
                    raise TypeMismatchInStmt(ctx)
                return 6
            elif ctx.id.name == "str2bool":
                if paramType != 6:
                    raise TypeMismatchInStmt(ctx)
                return 5
            elif ctx.id.name == "bool2str":
                if paramType != 5:
                    raise TypeMismatchInStmt(ctx)
                return 6
            else:
                return -1

        for env in o[0]:
            if ctx.id.name in env:
                if not isinstance(env[ctx.id.name], list):
                    raise TypeMismatchInStmt(ctx)

                if o[3]:
                    if env[ctx.id.name][1] != -1:
                        raise TypeMismatchInStmt(ctx)

                if len(ctx.param) == 0 and len(env[ctx.id.name][0]) == 0:
                    return -2 if env[ctx.id.name][1] == 0 else env[ctx.id.name][1]

                if len(ctx.param) != len(env[ctx.id.name][0]):
                    raise TypeMismatchInStmt(ctx)

                if len(ctx.param) > 0:
                    paramPair = zip(ctx.param, env[ctx.id.name][0])
                    newParamType = []
                    for aPara, fPara in paramPair:
                        actType = self.checkCallStmt(aPara, o)
                        if fPara == 0:
                            if actType == 0:
                                raise TypeCannotBeInferred(ctx)
                            fPara = actType
                        elif actType == 0 or fPara != actType:
                            if fPara == 4:
                                if actType not in [3, 5]:
                                    raise TypeMismatchInStmt(ctx)
                            elif fPara == 3:
                                if actType != 5:
                                    raise TypeMismatchInStmt(ctx)
                        newParamType.append(fPara)
                    env[ctx.id.name][0] = newParamType
                    return -2 if env[ctx.id.name][1] == 0 else env[ctx.id.name][1]
        else:
            raise UndeclaredIdentifier(ctx.id.name)

    def visitIf(self, ctx, o):
        env = o[:]
        env[0] = [{}] + env[0]
        for exp, stmts in ctx.ifthenStmt:
            condTyp = self.checkCallStmt(exp, env)
            if condTyp != 5:
                raise TypeMismatchInStmt(exp)
            for stmt in stmts:
                self.visit(stmt, env)

        for stmt in ctx.elseStmt:
            self.visit(stmt, env)

    def visitIntLit(self, ctx, o):
        return 3

    def visitFloatLit(self, ctx, o):
        return 4

    def visitBoolLit(self, ctx, o):
        return 5

    def visitStringLit(self, ctx, o):
        return 6

    def visitArrayLit(self, ctx, o):
        arrayEle = []
        if isinstance(ctx.value[0], AssocExp):
            arrayEle.append(self.visit(ctx.value[0], o))
            for id in range(1, len(ctx.value)):
                if isinstance(ctx.value[id], AssocExp):
                    key_val = self.visit(ctx.value[id], o)
                    if key_val[0] != arrayEle[id-1][0] or key_val[1] != arrayEle[id-1][1]:
                        raise InvalidArrayLiteral(ctx)
                    arrayEle.append(key_val)
                else:
                    raise InvalidArrayLiteral(ctx)
            return (7, arrayEle[0])

        elif isinstance(ctx.value[0], ArrayLit):
            for exp in ctx.value:
                if isinstance(exp, ArrayLit):
                    arrayEle.append(self.visit(exp, o))
                else:
                    raise InvalidArrayLiteral(exp)
            return (8, arrayEle)

        else:
            arrayEle.append(self.visit(ctx.value[0], o))
            for id in range(1, len(ctx.value)):
                typ = self.visit(ctx.value[id], o)
                if typ != arrayEle[id-1]:
                    raise InvalidArrayLiteral(ctx)
                arrayEle.append(typ)
            return (9, arrayEle[0])
