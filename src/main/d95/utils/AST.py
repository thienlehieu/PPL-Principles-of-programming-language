from abc import ABC


def printlist(lst):
    return f"[{','.join([str(x) for x in lst])}]"


def printIfThenStmt(stmt):
    return f"({str(stmt[0])},{printlist(stmt[1])})"


class AST(ABC):
    pass


class Program(AST):
    # const: List[ConstDecl]
    # nonconst: List[NonConstDecl]
    def __init__(self, const, nonconst):
        self.const = const
        self.nonconst = nonconst

    def __str__(self):
        return f"Program({printlist(self.const)},{printlist(self.nonconst)})"

    def accept(self, v, param):
        return v.visitProgram(self, param)


class Decl(AST):
    pass


class Stmt(AST):
    pass


class ConstDecl(Decl):
    # id: Id
    # value: Expr

    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __str__(self):
        return f"ConstDecl({str(self.id)},{str(self.value)})"

    def accept(self, v, param):
        return v.visitConstDecl(self, param)


class NonConstDecl(Decl):
    pass


class Assign(NonConstDecl, Stmt):  # Used for variable declaration and assignment statement
    # lhs: LHS
    # rhs: Exp

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"Assign({str(self.lhs)},{self.rhs})"

    def accept(self, v, param):
        return v.visitAssign(self, param)


class ParamDecl(Decl):
    # id: Id

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"ParamDecl({str(self.id)})"

    def accept(self, v, param):
        return v.visitParamDecl(self, param)


class FuncDecl(NonConstDecl):
    # name: Id
    # param: List[ParamDecl]
    # body: List[Statement]

    def __init__(self, name, param, body):
        self.name = name
        self.param = param
        self.body = body

    def __str__(self):
        return f"FuncDecl({str(self.name)},{printlist(self.param)},{printlist(self.body)})"

    def accept(self, v, param):
        return v.visitFuncDecl(self, param)


class ForEach(Stmt):
    # arr: Exp
    # key: Id
    # value: Id
    # body: List[Stmt]

    def __init__(self, arr, key, value, body):
        self.arr = arr
        self.key = key
        self.value = value
        self.body = body

    def __str__(self):
        return f"ForEach({str(self.arr)},{self.key},{self.value},{printlist(self.body)})"

    def accept(self, v, param):
        return v.visitForEach(self, param)


class While(Stmt):
    # cond: Exp
    # body: List[Stmt]

    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

    def __str__(self):
        return f"While({str(self.cond)},{printlist(self.body)})"

    def accept(self, v, param):
        return v.visitWhile(self, param)


class Break(Stmt):
    def __str__(self):
        return f"Break()"

    def accept(self, v, param):
        return v.visitBreak(self, param)


class Continue(Stmt):
    def __str__(self):
        return f"Continue()"

    def accept(self, v, param):
        return v.visitContinue(self, param)


class Return(Stmt):
    # exp: Exp or None if empty
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return f"Return({str(self.exp) if self.exp else ''})"

    def accept(self, v, param):
        return v.visitReturn(self, param)


class Exp(AST):
    pass


class LHS(Exp):
    pass


class Id(LHS):
    # name: str

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Id({self.name})"

    def accept(self, v, param):
        return v.visitId(self, param)


class ArrayAccess(LHS):
    # id: Id
    # idx: List[Expr]
    def __init__(self, id, idx):
        self.id = id
        self.idx = idx

    def __str__(self):
        return f"ArrayAccess({str(self.id)},{printlist(self.idx)})"

    def accept(self, v, param):
        return v.visitArrayAccess(self, param)


class BinExp(Exp):
    # op: str
    # left: Exp
    # right: Exp

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return f"BinExp({self.op},{str(self.left)},{str(self.right)})"

    def accept(self, v, param):
        return v.visitBinExp(self, param)


class UnExp(Exp):
    # op: str
    # exp: Exp

    def __init__(self, op, exp):
        self.op = op
        self.exp = exp

    def __str__(self):
        return f"UnExp({self.op},{str(self.exp)})"

    def accept(self, v, param):
        return v.visitUnExp(self, param)


class AssocExp(Exp):
    # key: Exp
    # value: Exp

    def __init__(self, key, value):
        self.key, self.value = key, value

    def __str__(self):
        return f"AssocExp({self.key},{str(self.value)})"

    def accept(self, v, param):
        return v.visitAssocExp(self, param)


class IntLit(Exp):
    # value: int

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"IntLit({str(self.value)})"

    def accept(self, v, param):
        return v.visitIntLit(self, param)


class FloatLit(Exp):
    #value: float
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"FloatLit({str(self.value)})"

    def accept(self, v, param):
        return v.visitFloatLit(self, param)


class BoolLit(Exp):
    # value: bool
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"BoolLit({str(self.value)})"

    def accept(self, v, param):
        return v.visitBoolLit(self, param)


class StringLit(Exp):
    # value: str
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"StringLit({self.value})"

    def accept(self, v, param):
        return v.visitStringLit(self, param)


class ArrayLit(Exp):
    # value: List[Exp]

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ArrayLit({printlist(self.value)})"

    def accept(self, v, param):
        return v.visitArrayLit(self, param)


class Call(Exp, Stmt):
    # id: Id
    # param: List[Exp]

    def __init__(self, id, param):
        self.id, self.param = id, param

    def __str__(self):
        return f"Call({str(self.id)}),{printlist(self.param)})"

    def accept(self, v, param):
        return v.visitCall(self, param)


class If(Stmt):
    # ifthenStmt: List[Tuple[Expr, List[Stmt]]]
    # elseStmt: List[Stmt]  # for Else branch, empty list if no Else

    def __init__(self, ifthenStmt, elseStmt):
        self.ifthenStmt = ifthenStmt
        self.elseStmt = elseStmt

    def __str__(self):
        return f"If({','.join([printIfThenStmt(stmt) for stmt in self.ifthenStmt])},{printlist(self.elseStmt)})"

    def accept(self, v, param):
        return v.visitIf(self, param)
