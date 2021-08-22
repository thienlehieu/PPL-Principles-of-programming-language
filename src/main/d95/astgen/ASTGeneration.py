from AST import *
from D95Visitor import D95Visitor
from D95Parser import D95Parser
from functools import *


class ASTGeneration(D95Visitor):
    # Visit a parse tree produced by D95Parser#program.
    def visitProgram(self, ctx: D95Parser.ProgramContext):
        const_decl = []
        non_const_decl = []
        if ctx.const_declare():
            for decl in ctx.const_declare():
                const_decl.append(self.visit(decl))
        if ctx.var_declare():
            for decl in ctx.var_declare():
                non_const_decl.append(self.visit(decl))
        if ctx.func_declare():
            for decl in ctx.func_declare():
                non_const_decl.append(self.visit(decl))
        return Program(const_decl, non_const_decl)

    # Visit a parse tree produced by D95Parser#var_declare.
    def visitVar_declare(self, ctx: D95Parser.Var_declareContext):
        return Assign(self.visit(ctx.assign_lhs()), self.visit(ctx.exp()))

    # Visit a parse tree produced by D95Parser#const_declare.
    def visitConst_declare(self, ctx: D95Parser.Const_declareContext):
        return ConstDecl(Id(ctx.CONSTANT_NAME().getText()), self.visit(ctx.exp()))

    # Visit a parse tree produced by D95Parser#func_declare.
    def visitFunc_declare(self, ctx: D95Parser.Func_declareContext):
        return FuncDecl(Id(ctx.FUNCTION_NAME().getText()), self.visit(ctx.params()), self.visit(ctx.body()))

    # Visit a parse tree produced by D95Parser#stmt.
    def visitStmt(self, ctx: D95Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D95Parser#assign_stmt.
    def visitAssign_stmt(self, ctx: D95Parser.Assign_stmtContext):
        return self.visit(ctx.var_declare())

    # Visit a parse tree produced by D95Parser#assign_lhs.
    def visitAssign_lhs(self, ctx: D95Parser.Assign_lhsContext):
        if ctx.VAR_NAME():
            return Id(ctx.VAR_NAME().getText())
        elif ctx.CONSTANT_NAME():
            return Id(ctx.CONSTANT_NAME().getText())
        return self.visit(ctx.index_opr())

    # Visit a parse tree produced by D95Parser#if_stmt.
    def visitIf_stmt(self, ctx: D95Parser.If_stmtContext):
        exp1 = self.visit(ctx.exp())
        stmt1 = [self.visit(stmt) for stmt in ctx.stmt()]
        if ctx.elif_part() and ctx.else_part():
            elseif_part = list(reduce(lambda x,y: x+y, [self.visit(part) for part in ctx.elif_part()], []))
            return If([(exp1,stmt1)] + elseif_part, self.visit(ctx.else_part()))
        elif ctx.elif_part():
            elseif_part = list(reduce(lambda x, y: x + y, [self.visit(part) for part in ctx.elif_part()], []))
            return If([(exp1,stmt1)] + elseif_part, [])
        elif ctx.else_part():
            return If([(exp1,stmt1)], self.visit(ctx.else_part()))
        return If([(exp1,stmt1)], [])

    def visitElif_part(self, ctx: D95Parser.Elif_partContext):
        exp = self.visit(ctx.exp())
        stmts = [self.visit(stmt) for stmt in ctx.stmt()]
        return [(exp, stmts)]

    def visitElse_part(self, ctx: D95Parser.Else_partContext):
        return [self.visit(stmt) for stmt in ctx.stmt()]

    # Visit a parse tree produced by D95Parser#foreach_stmt.
    def visitForeach_stmt(self, ctx: D95Parser.Foreach_stmtContext):
        return ForEach(self.visit(ctx.fe_id(0)),self.visit(ctx.fe_id(1)),self.visit(ctx.fe_id(2)),[self.visit(stmt) for stmt in ctx.stmt()])

    # Visit a parse tree produced by D95Parser#while_stmt.
    def visitWhile_stmt(self, ctx: D95Parser.While_stmtContext):
        return While(self.visit(ctx.exp()), [self.visit(stmt) for stmt in ctx.stmt()])

    # Visit a parse tree produced by D95Parser#break_stmt.
    def visitBreak_stmt(self, ctx: D95Parser.Break_stmtContext):
        return Break()

    # Visit a parse tree produced by D95Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: D95Parser.Continue_stmtContext):
        return Continue()

    # Visit a parse tree produced by D95Parser#call_stmt.
    def visitCall_stmt(self, ctx: D95Parser.Call_stmtContext):
        return Call(Id(ctx.FUNCTION_NAME().getText()), self.visit(ctx.func_params()))

    # Visit a parse tree produced by D95Parser#return_stmt.
    def visitReturn_stmt(self, ctx: D95Parser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return(None)

    # Visit a parse tree produced by D95Parser#exp.
    def visitExp(self, ctx: D95Parser.ExpContext):
        if ctx.ASSO():
            return AssocExp(self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        return self.visit(ctx.exp1(0))

    # Visit a parse tree produced by D95Parser#exp1.
    def visitExp1(self, ctx: D95Parser.Exp1Context):
        if ctx.CONCATSTR():
            return BinExp(ctx.CONCATSTR().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.COMPSTR():
            return BinExp(ctx.COMPSTR().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        return self.visit(ctx.exp2(0))

    # Visit a parse tree produced by D95Parser#exp2.
    def visitExp2(self, ctx: D95Parser.Exp2Context):
        if ctx.EQ():
            return BinExp(ctx.EQ().getText(), self.visit(ctx.exp3(0)), self.visit(ctx.exp3(1)))
        elif ctx.NEQ():
            return BinExp(ctx.NEQ().getText(), self.visit(ctx.exp3(0)), self.visit(ctx.exp3(1)))
        elif ctx.GT():
            return BinExp(ctx.GT().getText(), self.visit(ctx.exp3(0)), self.visit(ctx.exp3(1)))
        elif ctx.LT():
            return BinExp(ctx.LT().getText(), self.visit(ctx.exp3(0)), self.visit(ctx.exp3(1)))
        elif ctx.GTE():
            return BinExp(ctx.GTE().getText(), self.visit(ctx.exp3(0)), self.visit(ctx.exp3(1)))
        elif ctx.LTE():
            return BinExp(ctx.LTE().getText(), self.visit(ctx.exp3(0)), self.visit(ctx.exp3(1)))
        return self.visit(ctx.exp3(0))

    # Visit a parse tree produced by D95Parser#exp3.
    def visitExp3(self, ctx: D95Parser.Exp3Context):
        if ctx.AND():
            return BinExp(ctx.AND().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.OR():
            return BinExp(ctx.OR().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        return self.visit(ctx.exp4())

    # Visit a parse tree produced by D95Parser#exp4.
    def visitExp4(self, ctx: D95Parser.Exp4Context):
        if ctx.ADD():
            return BinExp(ctx.ADD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.MINUS():
            return BinExp(ctx.MINUS().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        return self.visit(ctx.exp5())

    # Visit a parse tree produced by D95Parser#exp5.
    def visitExp5(self, ctx: D95Parser.Exp5Context):
        if ctx.MUL():
            return BinExp(ctx.MUL().getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        elif ctx.DIV():
            return BinExp(ctx.DIV().getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        elif ctx.MOD():
            return BinExp(ctx.MOD().getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        return self.visit(ctx.exp6())

    # Visit a parse tree produced by D95Parser#exp6.
    def visitExp6(self, ctx: D95Parser.Exp6Context):
        if ctx.NOT():
            return UnExp(ctx.NOT().getText(), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())

    # Visit a parse tree produced by D95Parser#exp7.
    def visitExp7(self, ctx: D95Parser.Exp7Context):
        if ctx.MINUS():
            return UnExp(ctx.MINUS().getText(), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())

    # Visit a parse tree produced by D95Parser#exp8.
    def visitExp8(self, ctx: D95Parser.Exp8Context):
        if ctx.exp8():
            #return ArrayAccess(self.visit(ctx.exp8()), [self.visit(ctx.exp())])
            #return ArrayAccess(self.visit(ctx.identifier()), [self.visit(exp) for exp in ctx.index_exp()])
            return ArrayAccess(self.visit(ctx.exp8()), [self.visit(exp) for exp in ctx.index_exp()])
        return self.visit(ctx.exp9())

    # Visit a parse tree produced by D95Parser#exp9.
    def visitExp9(self, ctx: D95Parser.Exp9Context):
        if ctx.getChildCount() > 1:
            #return Call(self.visit(ctx.exp10()), [self.visit(ctx.exp())])
            return Call(self.visit(ctx.exp10()), self.visit(ctx.func_params()))
        return self.visit(ctx.exp10())

    # Visit a parse tree produced by D95Parser#exp10.
    def visitExp10(self, ctx: D95Parser.Exp10Context):
        if ctx.exp():
            return self.visit(ctx.exp())
        return self.visit(ctx.operands())

    # Visit a parse tree produced by D95Parser#operands.
    def visitOperands(self, ctx: D95Parser.OperandsContext):
        if ctx.identifier():
            return self.visit(ctx.identifier())
        elif ctx.primitive_lit():
            return self.visit(ctx.primitive_lit())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        else:
            return self.visit(ctx.array_lit())

    # Visit a parse tree produced by D95Parser#func_call.
    def visitFunc_call(self, ctx: D95Parser.Func_callContext):
        return Call(Id(ctx.FUNCTION_NAME().getText()), self.visit(ctx.func_params()))

    def visitFunc_params(self, ctx: D95Parser.Func_paramsContext):
        if ctx.getChildCount() >= 1:
            return [self.visit(exp) for exp in ctx.exp()]
        else:
            return []

    # Visit a parse tree produced by D95Parser#index_exp.
    def visitIndex_exp(self, ctx: D95Parser.Index_expContext):
        #return ArrayAccess(self.visit(ctx.exp8()), [self.visit(ctx.exp())])
        return self.visit(ctx.exp())

    def visitIndex_opr(self, ctx: D95Parser.Index_oprContext):
        return ArrayAccess(self.visit(ctx.identifier()), [self.visit(exp) for exp in ctx.index_exp()])

    # Visit a parse tree produced by D95Parser#params.
    def visitParams(self, ctx: D95Parser.ParamsContext):
        if ctx.getChildCount() >= 1:
            return [ParamDecl(Id(name.getText())) for name in ctx.VAR_NAME()]
        else:
            return []

    # Visit a parse tree produced by D95Parser#body.
    def visitBody(self, ctx: D95Parser.BodyContext):
        return [self.visit(stmt) for stmt in ctx.stmt()]

    # Visit a parse tree produced by D95Parser#literal.
    def visitLiteral(self, ctx: D95Parser.LiteralContext):
        if ctx.primitive_lit():
            return self.visit(ctx.primitive_lit())
        return self.visit(ctx.array_lit())

    def visitIdentifier(self, ctx: D95Parser.IdentifierContext):
        if ctx.VAR_NAME():
            return Id(ctx.VAR_NAME().getText())
        elif ctx.FUNCTION_NAME():
            return Id(ctx.FUNCTION_NAME().getText())
        return Id(ctx.CONSTANT_NAME().getText())

    # Visit a parse tree produced by D95Parser#primitive_lit.
    def visitPrimitive_lit(self, ctx: D95Parser.Primitive_litContext):
        if ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        else:
            return BoolLit(True) if ctx.BOOLEAN().getText() == 'True' else BoolLit(False)

    # Visit a parse tree produced by D95Parser#array_lit.
    def visitArray_lit(self, ctx: D95Parser.Array_litContext):
        if ctx.index_arr():
            return self.visit(ctx.index_arr())
        elif ctx.asso_arr():
            return self.visit(ctx.asso_arr())
        else:
            return self.visit(ctx.multidim_arr())

    # Visit a parse tree produced by D95Parser#index_arr.
    def visitIndex_arr(self, ctx: D95Parser.Index_arrContext):
        return self.visit(ctx.index_arr_body())

    # Visit a parse tree produced by D95Parser#index_arr_body.
    def visitIndex_arr_body(self, ctx: D95Parser.Index_arr_bodyContext):
        return ArrayLit([self.visit(arrEle) for arrEle in ctx.primitive_lit()])

    # Visit a parse tree produced by D95Parser#asso_arr.
    def visitAsso_arr(self, ctx: D95Parser.Asso_arrContext):
        asso_arr = [self.visit(arr) for arr in ctx.asso_ele()]
        return ArrayLit(asso_arr)

    # Visit a parse tree produced by D95Parser#asso_ele.
    def visitAsso_ele(self, ctx: D95Parser.Asso_eleContext):
        return AssocExp(self.visit(ctx.asso_key()), self.visit(ctx.exp()))

    # Visit a parse tree produced by D95Parser#multidim_arr.
    def visitMultidim_arr(self, ctx: D95Parser.Multidim_arrContext):
        return ArrayLit([self.visit(arr) for arr in ctx.multidim_arr_ele()])

    # Visit a parse tree produced by D95Parser#multidim_arr_ele.
    def visitMultidim_arr_ele(self, ctx: D95Parser.Multidim_arr_eleContext):
        if ctx.index_arr():
            return self.visit(ctx.index_arr())
        elif ctx.asso_arr():
            return self.visit(ctx.asso_arr())
        else:
            return self.visit(ctx.multidim_arr())

    # Visit a parse tree produced by D95Parser#asso_key.
    def visitAsso_key(self, ctx: D95Parser.Asso_keyContext):
        if ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText()))
        return StringLit(ctx.STRINGLIT().getText())

    # Visit a parse tree produced by D95Parser#fe_id.
    def visitFe_id(self, ctx: D95Parser.Fe_idContext):
        if ctx.VAR_NAME():
            return Id(ctx.VAR_NAME().getText())
        return Id(ctx.CONSTANT_NAME().getText())
