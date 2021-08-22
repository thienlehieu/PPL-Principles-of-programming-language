//student's id: 1613318
grammar D95;

@lexer::header {
from lexererr import *
import re
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program: (var_declare | const_declare | func_declare)+ EOF ;
/*
*Parser
*/
//var_declare: VAR_NAME ASSIGN exp SEMI;
var_declare: assign_lhs ASSIGN exp SEMI;

const_declare: DEFINE LP CONSTANT_NAME COMMA exp RP SEMI;

func_declare: FUNCTION FUNCTION_NAME LP params RP LCB body RCB;

stmt: assign_stmt
    | if_stmt
    | foreach_stmt | while_stmt
    | break_stmt | continue_stmt
    | call_stmt | return_stmt
    ;

assign_stmt: var_declare;

assign_lhs: VAR_NAME | CONSTANT_NAME | index_opr;

if_stmt: IF LP exp RP LCB stmt* RCB elif_part* else_part?;

elif_part: ELSEIF LP exp RP LCB stmt* RCB;

else_part: ELSE LCB stmt* RCB;

foreach_stmt: FOREACH LP fe_id AS fe_id '=>' fe_id RP LCB stmt* RCB;

while_stmt: WHILE LP exp RP LCB stmt* RCB;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

call_stmt: FUNCTION_NAME LP func_params RP SEMI;

return_stmt: RETURN exp? SEMI;

exp: exp1 ASSO exp1 | exp1;
exp1: exp2 (CONCATSTR | COMPSTR) exp2 | exp2;
exp2: exp3 (EQ | NEQ | GT | LT | GTE | LTE) exp3 | exp3;
exp3: exp3 (AND | OR) exp4 | exp4;
exp4: exp4 (ADD | MINUS) exp5 | exp5;
exp5: exp5 (MUL | DIV | MOD) exp6 | exp6;
exp6: NOT exp6 | exp7;
exp7: MINUS exp7 | exp8;
exp8: exp8 index_exp+ | exp9;
//exp8: exp8 LSB exp RSB | exp9;
exp9: exp10 LP func_params RP| exp10;
exp10: LP exp RP | operands;

//func_call: exp10 LP exp RP;
operands: identifier
        | primitive_lit
        | func_call
        | array_lit
        ;


func_call: FUNCTION_NAME LP func_params RP;

func_params: exp (COMMA exp)* |;

index_exp: LSB exp RSB;

index_opr: identifier index_exp+;

params: VAR_NAME (COMMA VAR_NAME)* |;

body: stmt+;

literal: primitive_lit | array_lit;

identifier: VAR_NAME | FUNCTION_NAME | CONSTANT_NAME;

primitive_lit:  INTLIT
                | FLOATLIT
                | STRINGLIT
                | BOOLEAN
                ;

array_lit: index_arr | asso_arr | multidim_arr;

index_arr: ARRAY LP index_arr_body RP;

index_arr_body: primitive_lit (COMMA primitive_lit)*;

asso_arr: ARRAY LP asso_ele (COMMA asso_ele)* RP;

asso_ele: asso_key '=>' exp;

multidim_arr: ARRAY LP multidim_arr_ele (COMMA multidim_arr_ele)* RP;

multidim_arr_ele: index_arr | asso_arr | multidim_arr;

asso_key: INTLIT | STRINGLIT;

fe_id: VAR_NAME | CONSTANT_NAME;

//token sets

//key word
RETURN: 'r' E T U R N;
BREAK: 'b' R E A K;
CONTINUE: 'c' O N T I N U E;
IF: 'i' F;
ELSEIF: 'e' L S E I F ;
ELSE: 'e' L S E;
WHILE: 'w' H I L E;
FOREACH: 'f' O R E A C H;
AS: 'a' S;
FUNCTION: 'f' U N C T I O N;
ARRAY: 'a' R R A Y;
DEFINE: 'd' E F I N E;

//operators
ASSIGN: '=';
CONCATSTR: '+.';
COMPSTR: '==.';
ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';
ASSO: '=>';

//seperators
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
COLON: ':';
COMMA: ',';
SEMI: ';';
LCB: '{';
RCB: '}';

//literals
//interger:
INTLIT: '0'[0-7]+ //octal
        | '0'[xX][0-9a-fA-F]+ //hexa
        | '0'[bB][01]+ //binary
        | [1-9][0-9]*('_'[0-9]+)* //interger literals
        | '0'
        {
            y = str(self.text)
            x = re.sub("_","",y)
            self.text = x[0:]
        };

//float
fragment INTPART: [0-9]+('_'[0-9]+)*;
fragment DECPART: DOT INTPART*;
fragment EXPOPART: [eE] [-+]? INTPART+;

FLOATLIT: INTPART (DECPART EXPOPART? | EXPOPART)
        {
            y = str(self.text)
            x = re.sub("_","",y)
            self.text = x[0:]
        };

DOT: '.';

//boolean
BOOLEAN: 't' R U E | 'f' A L S E;

//string

fragment ESC_SEQ: '\\' [btnfr'\\] ;
fragment STRINGCHAR: ('\\' [btfr'\\] | ~[\n\\'"] | '\'' '"');
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | '\\' ;

STRINGLIT: '"' STRINGCHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	};

//comments
BLOCKCOMMENT: '/*' .*? '*/' -> skip; //skip comments

/**identifiers**/
//variable, parameter, constant and function names

VAR_NAME: '$'[A-Za-z_0-9]*;

FUNCTION_NAME: '_'[A-Za-z_0-9]*
                | 'str2int'
                | 'int2str'
                | 'str2float'
                | 'float2str'
                | 'str2bool'
                | 'bool2str'
                ;

CONSTANT_NAME: [A-Za-z_][A-Za-z_0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ILLEGAL_ESCAPE: '"' STRINGCHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};

UNCLOSE_STRING: '"' STRINGCHAR* ( [\b\t\n\f\r'\\] | EOF )
	{
		y = str(self.text)
		raise UncloseString(y[1:])
	};

//UNCLOSE_STRING: .;

UNTERMINATED_COMMENT: '/*' .*? ~[*] ~[/]
    {
        raise UnterminatedComment()
    };

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};

fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];