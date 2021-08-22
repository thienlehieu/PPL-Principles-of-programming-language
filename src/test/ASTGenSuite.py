import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_vardecl1(self):
        """global variables"""
        input = """
        $x = 1;
        function _foo($a, $b){
            $a = $x + 1;
            $b = $x + 2;
            return $a;
        }
        """
        expect = "Program([],[Assign(Id($a),IntLit(1)),Assign(Id($b),BinExp(-,BinExp(+,IntLit(1),IntLit(2)),IntLit(1)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # def test_more_complex_program(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Body:
    #         x = 10;
    #         printLn(x);
    #     EndBody.
    #     """
    #     expect = str(Program([
    #         VarDecl(Id("x"),[],IntLiteral(5)),
    #         FuncDecl(Id("main"),[],([],[
    #             Assign(Id("x"),IntLiteral(10)),
    #             CallStmt(Id("printLn"),[Id("x")])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
   