# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D95Parser import D95Parser
else:
    from D95Parser import D95Parser

# This class defines a complete generic visitor for a parse tree produced by D95Parser.

class D95Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D95Parser#program.
    def visitProgram(self, ctx:D95Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#var_declare.
    def visitVar_declare(self, ctx:D95Parser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#const_declare.
    def visitConst_declare(self, ctx:D95Parser.Const_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#func_declare.
    def visitFunc_declare(self, ctx:D95Parser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt.
    def visitStmt(self, ctx:D95Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D95Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:D95Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#if_stmt.
    def visitIf_stmt(self, ctx:D95Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#elif_part.
    def visitElif_part(self, ctx:D95Parser.Elif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#else_part.
    def visitElse_part(self, ctx:D95Parser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#foreach_stmt.
    def visitForeach_stmt(self, ctx:D95Parser.Foreach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#while_stmt.
    def visitWhile_stmt(self, ctx:D95Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D95Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D95Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#call_stmt.
    def visitCall_stmt(self, ctx:D95Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D95Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp.
    def visitExp(self, ctx:D95Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp1.
    def visitExp1(self, ctx:D95Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp2.
    def visitExp2(self, ctx:D95Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp3.
    def visitExp3(self, ctx:D95Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp4.
    def visitExp4(self, ctx:D95Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp5.
    def visitExp5(self, ctx:D95Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp6.
    def visitExp6(self, ctx:D95Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp7.
    def visitExp7(self, ctx:D95Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp8.
    def visitExp8(self, ctx:D95Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp9.
    def visitExp9(self, ctx:D95Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#exp10.
    def visitExp10(self, ctx:D95Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operands.
    def visitOperands(self, ctx:D95Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#func_call.
    def visitFunc_call(self, ctx:D95Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#func_params.
    def visitFunc_params(self, ctx:D95Parser.Func_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#index_exp.
    def visitIndex_exp(self, ctx:D95Parser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#index_opr.
    def visitIndex_opr(self, ctx:D95Parser.Index_oprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#params.
    def visitParams(self, ctx:D95Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#body.
    def visitBody(self, ctx:D95Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#literal.
    def visitLiteral(self, ctx:D95Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#identifier.
    def visitIdentifier(self, ctx:D95Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#primitive_lit.
    def visitPrimitive_lit(self, ctx:D95Parser.Primitive_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#array_lit.
    def visitArray_lit(self, ctx:D95Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#index_arr.
    def visitIndex_arr(self, ctx:D95Parser.Index_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#index_arr_body.
    def visitIndex_arr_body(self, ctx:D95Parser.Index_arr_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#asso_arr.
    def visitAsso_arr(self, ctx:D95Parser.Asso_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#asso_ele.
    def visitAsso_ele(self, ctx:D95Parser.Asso_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#multidim_arr.
    def visitMultidim_arr(self, ctx:D95Parser.Multidim_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#multidim_arr_ele.
    def visitMultidim_arr_ele(self, ctx:D95Parser.Multidim_arr_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#asso_key.
    def visitAsso_key(self, ctx:D95Parser.Asso_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#fe_id.
    def visitFe_id(self, ctx:D95Parser.Fe_idContext):
        return self.visitChildren(ctx)



del D95Parser