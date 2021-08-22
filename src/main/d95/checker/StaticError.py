class StaticError(BaseException):
    pass


class Kind():
    pass


class Const(Kind):
    def __str__(self):
        return "Const"


class Var(Kind):
    def __str__(self):
        return "Var"


class Func(Kind):
    def __str__(self):
        return "Func"


class Param(Kind):
    def __str__(self):
        return "Param"


class Redeclared(StaticError):
    def __init__(self, typ: Kind, id: str):
        self.typ = typ
        self.id = id

    def __str__(self):
        return f"Redeclared({str(self.typ)},{self.id})"


class TypeCannotBeInferred(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"TypeCannotBeInferred({str(self.stmt)})"


class TypeMismatchInStmt(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"TypeMismatchInStmt({str(self.stmt)})"


class TypeMismatchInExpr(StaticError):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return f"TypeMismatchInExpr({str(self.expr)})"


class UndeclaredIdentifier(StaticError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"UndeclaredIdentifier({str(self.name)})"


class InvalidArrayLiteral(StaticError):
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        return f"InvalidArrayLiteral({str(self.arr)})"


class NoEntryPoint(StaticError):
    def __init__(self): pass

    def __str__(self):
        return f"NoEntryPoint()"
