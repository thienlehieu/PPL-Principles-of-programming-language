import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    def test_complex(self):
        input = """
            function _foo($a){
                return;
            }
            function _foo2(){
                return 1;
            }
            function _main(){
                $w = 1;
                _echo("ada");
                _foo(str2float("1.1"));
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 600))