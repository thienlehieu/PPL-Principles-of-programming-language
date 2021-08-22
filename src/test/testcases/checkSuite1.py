import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_complex(self):
        """Simple program: main"""
        input = """
        define(aa, 12);
        $k = array(1,2,3);
        $x = 1;
        $y = 1.1;
        function _foo($a, $b, $q){
            $z = array(1,2,4);
            $a = $x + 2;
            $y = $x + $z[1];
            $b[1] = $x + 2;
            while($b[1] == $z[1] + $a){
                if($k[1] >= aa){
                    $z[1] = $x + $k[1];
                    return 123;
                }
                else{
                    if($a == 2){
                        $o = 1;
                        break;
                    }
                }
            }
            foreach($k as $key => $value){
                if($key == $x){
                    $g = 1.1;
                    $value = $value + aa;
                    break;
                }
                elseif($z[2] >= $x){
                    $z[2] = $z[1] + $value;
                    return $z[2];
                }
                $d = $key + $value;
            }
        }
        function _main(){
            $arr = array(1,2,3);
            $n = $x + $arr[1];
            $int = _foo($n, $arr, $arr[2]) + aa;
            return 1;            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_redeclared1(self):
        input = """
            define(x, 12);
            function _main(){
                x = 1;
                $y = 2;
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared2(self):
        input = """
            define(x, 12);
            function _main(){
                $y = x + 3 ;
                x = 2;
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared3(self):
        input = """
            define(x, 12);
            define(y, 2);
            $z = 5;
            function _main(){
                $z = x + y ;
                x = $z + y;
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared4(self):
        input = """
            define(x, 12);
            define(y, 2);
            $z = 5;
            function _main(){
                $z = x + y ;
                y = $z + x;
                return 1;
            }
        """
        expect = "Redeclared(Const,y)"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared5(self):
        input = """
            define(str, "string");
            define(y, 2);
            $z = 5;
            function _main(){
                $k = $z + 1;
                str = $k;
                return 1;
            }
        """
        expect = "Redeclared(Const,str)"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared6(self):
        input = """
            define(str, "string");
            define(y, 2);
            $z = 5;
            function _main(){
                $k = $z + 1;
                str = $k;
                return 1;
            }
        """
        expect = "Redeclared(Const,str)"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared7(self):
        input = """
            define(str, "string");
            define(y, 2.1);
            $z = 5;
            function _main(){
                $k = $z + y;
                str = $k + $z;
                return 1;
            }
        """
        expect = "Redeclared(Const,str)"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclared8(self):
        input = """
            define(str, "string");
            define(y, array(1,2,3));
            $z = 5;
            function _main(){
                $k = $z + y[1];
                y = str;
                return 1;
            }
        """
        expect = "Redeclared(Const,y)"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclared9(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5;
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclared10(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5;
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared11(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b){
                $z = $a + $b;
                return $a;
            }
            function _foo($a, $b){
                $z = $a - $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Func,_foo)"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared12(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b){
                $a = y[1] + x;
                $z = $a + $b;
                return $a;
            }
            function _foo($a, $b){
                $z = $a - $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Func,_foo)"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared13(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b, $a){
                $a = y[1] + x;
                $z = $a + $b;
                return $a;
            }
            function _foo1($a, $b){
                $z = $a - $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Param,$a)"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared14(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b){
                $a = y[1] + x;
                $z = $a + $b;
                return $a;
            }
            function _foo1($a, $b, $b){
                $z = $a - $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Param,$b)"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared15(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b){
                $a = y[1] + x;
                $z = $a + $b;
                return $a;
            }
            function _foo1($a, $b){
                $z = $a - $b;
                x = $z + $a + $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_redeclared16(self):
        input = """
            define(x, 1.2);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b){
                $a = y[1] + x;
                $z = $a + $b;
                return $a;
            }
            function _foo1($a, $b){
                $z = $a - $b;
                y = $z + $a + $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Const,y)"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_redeclared17(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b){
                $a = y[1] + x;
                $z = $a + $b;
                return $a;
            }
            function _foo1($a, $b){
                $y[1] = $a - $b;
                x = $z + $a + $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_redeclared18(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5.1;
            function _foo($a, $b){
                $a = y[1] + x;
                $z = $a + $b;
                return $a;
            }
            function _foo1($a, $b, $c, $c){
                $y[1] = $a - $b + $c;
                x = $z + $a + $b;
                return;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Param,$c)"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclared19(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                $a = y[1] + x;
                x = y[2] + y[$a];
                return $a;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Const,x)"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_redeclared20(self):
        input = """
            define(x, 3);
            define(y, 1.4);
            $z = 5;
            function _foo($a, $b){
                $a = y + x;
                y = $b - $a;
                return $a;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "Redeclared(Const,y)"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_undeclared1(self):
        input = """
            define(x, 3);
            define(y, 1.4);
            $z = 5;
            function _foo($a, $b){
                $a = y + $d;
                y = $b - $a;
                return $a;
            }
            function _main(){
                $k = x + y[2];
                x = $z + y[1];
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($d)"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_undeclared2(self):
        input = """
            define(x, 3);
            $z = 5;
            function _foo($a, $b){
                $a = $z + 1;
                $b = $b - x;
                return $a;
            }
            function _main(){
                $k = x + y[2];
                x = $z + $k;
                return 1;
            }
        """
        expect = "UndeclaredIdentifier(y)"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_undeclared3(self):
        input = """
            define(x, 3);
            $z = 5;
            function _foo($a, $b){
                if($c == 1){
                    $z = $a + $b;
                }
                return $a - $b;
            }
            function _main(){
                $s = $z + _foo(1,2);
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($c)"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_undeclared4(self):
        input = """
            define(x, 3);
            $z = 5;
            function _foo($a, $b){
                if($a == 1){
                    $z = $a + $c;
                }
                return $a - $b;
            }
            function _main(){
                $s = $z + _foo(1,2);
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($c)"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_undeclared5(self):
        input = """
            define(x, 3);
            $z = 5.1;
            function _foo($a, $b){
                if($a == 1){
                    $z = $a + $b;
                }
                else{
                    $b = $h + 1;
                }
                return $a - $b;
            }
            function _main(){
                $s = $z + _foo(1,2);
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($h)"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_undeclared6(self):
        input = """
            define(x, 3);
            $z = 5.1;
            function _foo($a, $b){
                if($a == 1){
                    $z = $a + $b;
                }
                else{
                    $b = $a + 1;
                }
                return $a - $b;
            }
            function _main(){
                $s = $z + $k;
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($k)"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_undeclared7(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $c = $key + $h;
                }
                return 1;
            }
            function _main(){
                $s = $z + $k;
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($h)"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_undeclared8(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $c = $key + $b;
                    $z = $e + $a;
                }
                return 1;
            }
            function _main(){
                $s = $z + $k;
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($e)"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_undeclared9(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $c = $key + $b;
                    if($value > ($h + 1)){
                        break;
                    }
                }
                return 1;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($h)"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_undeclared10(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $c = $key + $b;
                    if($value > ($z + 1)){
                        $m = $n*2;
                        break;
                    }
                }
                return 1;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "UndeclaredIdentifier($n)"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_type_cannot_be_infered1(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                $a = $b;
                return $a;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeCannotBeInferred(Assign(Id($a),Id($b)))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_cannot_be_infered2(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                $z = y[1] + x;
                $a = $b;
                return $b;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeCannotBeInferred(Assign(Id($a),Id($b)))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_type_mismatch_in_stmt1(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                if($a + $b){
                    break;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(BinExp(+,Id($a),Id($b)))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_in_stmt2(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            $z = 5;
            function _foo($a, $b){
                if($a >= $b){
                    $h = y[1][2] + 1;
                    break;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id(y),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_type_mismatch_in_stmt3(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(q as $key => $value){
                    $z = y[1] + $key;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(+,ArrayAccess(Id(y),[IntLit(1)]),Id($key)))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_type_mismatch_in_stmt4(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                $k = q[1] + $z;
                foreach(q as $key => $value){
                    $z = y[1] + x;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id(q),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_type_mismatch_in_stmt5(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                $k = q["a"] + $z;
                $z = $k + "str";
                foreach(q as $key => $value){
                    $z = y[1] + x;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(+,Id($k),StringLit(str)))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_type_mismatch_in_stmt6(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z + 2){
                    $a = $b + 1;
                    break;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(While(BinExp(+,Id($z),IntLit(2)),[Assign(Id($a),BinExp(+,Id($b),IntLit(1))),Break()]))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_type_mismatch_in_stmt7(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z == y[1]){
                    if(x > q["a"]){
                        break;
                    }
                    $z = x + q[2];
                    $g = $a - $b;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id(q),[IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_type_mismatch_in_stmt8(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z == y[1]){
                    if(x > q["a"]){
                        break;
                    }
                    $z = x + $a;
                    $g = $a - $b;
                }
                return;
            }
            function _main(){
                $s = $z + _foo(1,2,3);
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Assign(Id($z),BinExp(+,Id(x),Id($a))))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_type_mismatch_in_stmt9(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z == y[1]){
                    if(x > q["a"]){
                        break;
                    }
                    $z = x + $a;
                    $g = $a - $b;
                }
                return;
            }
            function _main(){
                $s = $z + _foo("a",3);
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Assign(Id($z),BinExp(+,Id(x),Id($a))))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_type_mismatch_in_stmt10(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $a = $key + $value;
                    $b = $key + $value;
                }
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3,3);
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Call(Id(_foo)),[IntLit(1),IntLit(3),IntLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_type_mismatch_in_stmt11(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(q as $key => $value){
                    $a = $key + $value;
                    $b = $key + $value;
                }
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(+,Id($key),Id($value)))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_type_mismatch_in_stmt12(self):
        input = """
            define(x, 3);
            define(y, array(array(1,2,3)));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    foreach($value as $key1 => $value1){
                        $a = $key1 + $value1;
                        $b = $key1 - $value1;
                    }
                }
                $z = q["a"] + y[1][2][3];
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id(y),[IntLit(1),IntLit(2),IntLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_type_mismatch_in_stmt13(self):
        input = """
            define(x, 3);
            define(y, array(array(1,2,3)));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $z = $value + 1;
                    foreach($value as $key1 => $value1){
                        $a = $key1 + $value1;
                        $b = $key1 - $value1;
                    }
                }
                $z = q["a"] + y[1][2];
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(+,Id($value),IntLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_type_mismatch_in_stmt14(self):
        input = """
            $x = 1.1;
            define(y, array(array(1,2,3)));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                $z = $x + $b;
                $z = q["a"] + y[1][2];
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Assign(Id($z),BinExp(+,Id($x),Id($b))))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_type_mismatch_in_stmt15(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                continue;
                return $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Continue())"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_type_mismatch_in_stmt16(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                            $z = $value + $a;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                return $b;
            }
            function _main(){
                $s = $z + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Assign(Id($z),BinExp(+,Id($value),Id($a))))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_type_mismatch_in_stmt17(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                            $x = $value + $a;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                return $b;
            }
            function _main(){
                $s = $z + _foo($x, $z);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_in_stmt18(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                            $x = $value + $a;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                return $b;
            }
            function _main(){
                $k = 1.12;
                $s = $z + _foo($x, $k);
                $z = $s + $k;
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Assign(Id($z),BinExp(+,Id($s),Id($k))))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_type_mismatch_in_stmt19(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            $str = "string";
            function _foo($a, $b){
                foreach(q as $key => $value){
                    if($key == $z){
                        $a = $value + $b;
                    }
                }
                return 1;
            }
            function _main(){
                $s = $z + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(==,Id($key),Id($z)))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_type_mismatch_in_stmt20(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            $str = "string";
            function _foo($a, $b){
                foreach(q as $key => $value){
                    if($key == $str){
                        $a = $value + $b;
                        q[$str] = $z + $key;
                    }
                }
                return 1;
            }
            function _main(){
                $s = $z + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(==,Id($key),Id($str)))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_type_mismatch_in_stmt21(self):
        input = """
            define(x, 1);
            y = array(array(1,2,3), array(3,4,5));
            function _foo($a, $b){
                while(true){
                    $a = x + y[1][2][3];
                    if($z >=0){
                        $b = $x + y[1][2];
                    }
                    else{
                        break;
                    }
                }
                return $a;
            }
            function _main(){
                $s = _foo($x, 2) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id(y),[IntLit(1),IntLit(2),IntLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_type_mismatch_in_stmt22(self):
        input = """
            define(x, 1);
            y = array(array(1,2,3), array(3,4,5));
            function _foo($a, $b){
                while(true){
                    $a = x + y[1][2];
                    if(x >= y[1]){
                        $b = $x + y[1][2];
                    }
                    else{
                        break;
                    }
                }
                return $a;
            }
            function _main(){
                $s = _foo($x, 2) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id(y),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_type_mismatch_in_stmt23(self):
        input = """
            define(x, 1);
            y = array(array(1,2,3), array(3,4,5));
            function _foo($a, $b){
                while(true){
                    $a = x + y[1][2];
                    if(x >= y[1][2]){
                        $z = $b + y[1][2];
                    }
                    else{
                        break;
                    }
                }
                return $a;
            }
            function _main(){
                $s = _foo(x, y[1][2]) + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_type_mismatch_in_stmt24(self):
        input = """
            define(x, 1);
            y = array(1,2,3);
            $z = 1;
            function _foo($a, $b){
                $q = $a + $b;
                $z = $a + y[1];
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Assign(Id($z),BinExp(+,Id($a),ArrayAccess(Id(y),[IntLit(1)]))))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_type_mismatch_in_exp1(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $z = 1;
            function _foo($a, $b){
                $q = $a + $b;
                $z = $a + $y[1];
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(+,Id($a),ArrayAccess(Id($y),[IntLit(1)])))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_type_mismatch_in_exp2(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if($key == $y[$val]){
                        $h = $val + $z;
                    }
                }
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(==,Id($key),ArrayAccess(Id($y),[Id($val)])))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_type_mismatch_in_exp3(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if($key ==. $y[$val]){
                        $h = $val + $z;
                    }
                    $z = $key + x;
                }
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(+,Id($key),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_type_mismatch_in_exp4(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if($key ==. $y[$val]){
                        $h = $val + $z;
                    }
                    elseif($val >= $y[1]){
                        break;
                    }
                    $z = $val + x;
                }
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(BinExp(>=,Id($val),ArrayAccess(Id($y),[IntLit(1)])))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_type_mismatch_in_exp5(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if($key ==. $y[$val]){
                        $h = $val + $z;
                    }
                    elseif($val >= $z){
                        break;
                    }
                    $z = $a + $b;
                }
                return $y[$val];
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInStmt(Assign(Id($z),BinExp(+,Id($a),Id($b))))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_type_mismatch_in_exp6(self):
        input = """
            define(x, 1);
            $y = array(array(1,2,3), array(1,2,3));
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1][2] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id($y),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_type_mismatch_in_exp7(self):
        input = """
            define(x, 1);
            $y = array(array(1,2,3), array(1,2,3));
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1][2][3] + $arr["a"];
                $b = $y[1][2] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id($y),[IntLit(1),IntLit(2),IntLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_type_mismatch_in_exp8(self):
        input = """
            define(x, 1);
            $y = array(array(1,2,3), array(1,2,3));
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1]["a"] + $arr["a"];
                $b = $y[1][2] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id($y),[IntLit(1),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_type_mismatch_in_exp9(self):
        input = """
            define(x, 1);
            $y = array(array(array(1,2,3)));
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1][2] + $arr["a"];
                $b = $y[1][2][3] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id($y),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_type_mismatch_in_exp10(self):
        input = """
            define(x, 1);
            $y = array(array(array(1,2,3)));
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1][2] + $arr["a"];
                $b = $y[1][2][3] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "TypeMismatchInExpr(ArrayAccess(Id($y),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_invalid_arr1(self):
        input = """
            define(x, 1);
            $y = array(1,2,3,"a");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "InvalidArrayLiteral(ArrayLit([IntLit(1),IntLit(2),IntLit(3),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_invalid_arr2(self):
        input = """
            define(x, 1);
            $y = array("a","b",3,"a");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "InvalidArrayLiteral(ArrayLit([StringLit(a),StringLit(b),IntLit(3),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_invalid_arr3(self):
        input = """
            define(x, 1);
            $y = array(1,2,3,4);
            $arr = array("a"=>1, "b"=>2, 3=>"c");
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "InvalidArrayLiteral(ArrayLit([AssocExp(StringLit(a),IntLit(1)),AssocExp(StringLit(b),IntLit(2)),AssocExp(IntLit(3),StringLit(c))]))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_invalid_arr4(self):
        input = """
            define(x, 1);
            $y = array(array(1,2,3,"a"));
            $arr = array("a"=>1, "b"=>2, 3=>"c");
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "InvalidArrayLiteral(ArrayLit([IntLit(1),IntLit(2),IntLit(3),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_invalid_arr5(self):
        input = """
            define(x, 1);
            $y = array(array(1,2,3,4));
            $arr = array(array("a"=>1, "b"=>2, 3=>"c"));
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "InvalidArrayLiteral(ArrayLit([AssocExp(StringLit(a),IntLit(1)),AssocExp(StringLit(b),IntLit(2)),AssocExp(IntLit(3),StringLit(c))]))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_no_entry_point1(self):
        input = """
            define(x, 1);
            $y = array(1,2,3,4);
            $arr = array("a"=>1, "b"=>2, 3=>"c");
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1] - $arr["a"];
                return $a + $b;
            }
            function _main1(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = "NoEntryPoint()"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_no_entry_point2(self):
        input = """
            define(x, 1);
            $y = array(1,2,3,4);
            $arr = array("a"=>1, "b"=>2, 3=>"c");
            $z = 1;
            function _foo($a, $b){
                $a = $y[1] + $arr["a"];
                $b = $y[1] - $arr["a"];
                return $a + $b;
            }
        """
        expect = "NoEntryPoint()"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_ok_1(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                $k = q["a"] + $z;
                foreach(q as $key => $value){
                    $z = y[1] + x;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_ok_2(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                $k = q["a"] + $z;
                $z = $k + 1;
                foreach(q as $key => $value){
                    $z = y[1] + x;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_ok_3(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z >= 2){
                    $a = $b + 1;
                    break;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_ok_4(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z == y[1]){
                    if(x > q["a"]){
                        break;
                    }
                    $z = x + q["a"];
                    $g = $a - $b;
                }
                return;
            }
            function _main(){
                $s = $z + x;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_ok_5(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5.1;
            function _foo($a, $b){
                while($z == y[1]){
                    if(x > q["a"]){
                        break;
                    }
                    $z = x + $a;
                    $g = $a - $b;
                }
                return $z;
            }
            function _main(){
                $s = $z + _foo(1,2);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_ok_6(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5.1;
            function _foo($a, $b){
                while($z == y[1]){
                    if(x > q["a"]){
                        break;
                    }
                    $z = x + $a;
                    $g = $a - $b;
                }
                return $z;
            }
            function _main(){
                $s = $z + _foo($z,3);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_ok_7(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $a = $key + $value;
                    $b = $key + $value;
                }
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_ok_8(self):
        input = """
            define(x, 3);
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(q as $key => $value){
                    $a = $z + $value;
                    $b = $z + $value;
                }
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_ok_9(self):
        input = """
            define(x, 3);
            define(y, array(array(1,2,3)));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    foreach($value as $key1 => $value1){
                        $a = $key1 + $value1;
                        $b = $key1 - $value1;
                    }
                }
                $z = q["a"] + y[1][2];
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_ok_10(self):
        input = """
            define(x, 3);
            define(y, array(array(1,2,3)));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                foreach(y as $key => $value){
                    $z = $value[1] + 1;
                    foreach($value as $key1 => $value1){
                        $a = $key1 + $value1;
                        $b = $key1 - $value1;
                    }
                }
                $z = q["a"] + y[1][2];
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_ok_11(self):
        input = """
            $x = 1.1;
            define(y, array(array(1,2,3)));
            define(q, array("a"=>1, "b"=>2));
            $z = 51.1;
            function _foo($a, $b){
                $z = $x + $b;
                $z = q["a"] + y[1][2];
                return $a + $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_ok_12(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                return $b;
            }
            function _main(){
                $s = $z + _foo(1,3);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_ok_13(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5.1;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                            $z = $value + $a;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                return $b;
            }
            function _main(){
                $s = $z + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_ok_14(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                            $x = $value + $a;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                return $b;
            }
            function _main(){
                $s = $z + _foo($x, $z);
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_ok_15(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5.1;
            function _foo($a, $b){
                while($z >= 1){
                    if($z == $a){
                        foreach(q as $key => $value){
                            $h = $b + $value;
                            $x = $value + $a;
                        }
                    }
                    elseif($z == y[1]){
                        break;
                    }
                }
                return $b;
            }
            function _main(){
                $k = 1.12;
                $s = $z + _foo($x, $k);
                $z = $s + $k;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_ok_16(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            $str = "string";
            function _foo($a, $b){
                foreach(q as $key => $value){
                    if($value == $z){
                        $a = $value + $b;
                    }
                }
                return 1;
            }
            function _main(){
                $s = $z + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_ok_17(self):
        input = """
            $x = 1.1;
            define(y, array(1,2,3));
            define(q, array("a"=>1, "b"=>2));
            $z = 5;
            $str = "string";
            function _foo($a, $b){
                foreach(q as $key => $value){
                    if($key ==. $str){
                        $a = $value + $b;
                    }
                }
                return 1;
            }
            function _main(){
                $s = $z + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_ok_18(self):
        input = """
            define(x, 1);
            y = array(array(1,2,3), array(3,4,5));
            function _foo($a, $b){
                while(true){
                    $a = x + y[1][2];
                    if(x >= 0){
                        $b = x + y[1][2];
                    }
                    else{
                        break;
                    }
                }
                return $a;
            }
            function _main(){
                $s = _foo(x, 2) + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_ok_19(self):
        input = """
            define(x, 1);
            y = array(array(1,2,3), array(3,4,5));
            function _foo($a, $b){
                while(true){
                    $a = x + y[1][2];
                    if(x >= y[1][0]){
                        $b = x + y[1][2];
                    }
                    else{
                        break;
                    }
                }
                return $a;
            }
            function _main(){
                $s = _foo(x, 2) + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_ok_20(self):
        input = """
            define(x, 1);
            y = array(array(1,2,3), array(3,4,5));
            function _foo($a, $b){
                while(true){
                    $a = x + y[1][2];
                    if(x >= y[1][2]){
                        $z = $b + y[1][2];
                    }
                    else{
                        break;
                    }
                }
                return $a;
            }
            function _main(){
                $s = _foo(x, y[1][2]) + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_ok_21(self):
        input = """
            define(x, 1);
            y = array(1,2,3);
            $z = 1.1;
            function _foo($a, $b){
                $q = $a + $b;
                $z = $a + y[1];
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_ok_22(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $z = 1.1;
            function _foo($a, $b){
                $q = $a + $b;
                $z = $a + x;
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_ok_23(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if("str" ==. $y[$val]){
                        $h = $val + $z;
                    }
                }
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_ok_24(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if($key ==. $y[$val]){
                        $h = $val + $z;
                    }
                    $z = $val + x;
                }
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_ok_25(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if($key ==. $y[$val]){
                        $h = $val + $z;
                    }
                    elseif($val >= $arr["a"]){
                        break;
                    }
                    $z = $val + x;
                }
                return 1;
            }
            function _main(){
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_ok_26(self):
        input = """
            define(x, 1);
            $y = array("a","b","c");
            $arr = array("a"=>1, "b"=>2);
            $z = 1.1;
            function _foo($a, $b){
                foreach($arr as $key => $val){
                    if($key ==. $y[$val]){
                        $h = $val + $z;
                    }
                    elseif($val >= $z){
                        break;
                    }
                    $z = $a + $b;
                }
                return $a;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_ok_27(self):
        input = """
            define(x, 1);
            $y = array(array(1,2,3), array(1,2,3));
            $arr = array("a"=>1, "b"=>2);
            $z = 1;
            function _foo($a, $b){
                $a = $y[1][2] + $arr["a"];
                $b = $y[1][2] - $arr["a"];
                return $a + $b;
            }
            function _main(){
                $t = _foo(x, $z) + 1;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))