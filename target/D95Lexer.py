# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import re



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u026b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\6)\u013c\n)\r)\16)\u013d\3)\3)\3")
        buf.write(")\6)\u0143\n)\r)\16)\u0144\3)\3)\3)\6)\u014a\n)\r)\16")
        buf.write(")\u014b\3)\3)\7)\u0150\n)\f)\16)\u0153\13)\3)\3)\6)\u0157")
        buf.write("\n)\r)\16)\u0158\7)\u015b\n)\f)\16)\u015e\13)\3)\3)\5")
        buf.write(")\u0162\n)\3*\6*\u0165\n*\r*\16*\u0166\3*\3*\6*\u016b")
        buf.write("\n*\r*\16*\u016c\7*\u016f\n*\f*\16*\u0172\13*\3+\3+\7")
        buf.write("+\u0176\n+\f+\16+\u0179\13+\3,\3,\5,\u017d\n,\3,\6,\u0180")
        buf.write("\n,\r,\16,\u0181\3-\3-\3-\5-\u0187\n-\3-\5-\u018a\n-\3")
        buf.write("-\3-\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u019b\n")
        buf.write("/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u01a5\n")
        buf.write("\61\3\62\3\62\3\62\5\62\u01aa\n\62\3\63\3\63\7\63\u01ae")
        buf.write("\n\63\f\63\16\63\u01b1\13\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\7\64\u01ba\n\64\f\64\16\64\u01bd\13\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\7\65\u01c6\n\65\f\65\16")
        buf.write("\65\u01c9\13\65\3\66\3\66\7\66\u01cd\n\66\f\66\16\66\u01d0")
        buf.write("\13\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0202\n\66\3\67\3")
        buf.write("\67\7\67\u0206\n\67\f\67\16\67\u0209\13\67\38\68\u020c")
        buf.write("\n8\r8\168\u020d\38\38\39\39\79\u0214\n9\f9\169\u0217")
        buf.write("\139\39\39\39\3:\3:\7:\u021e\n:\f:\16:\u0221\13:\3:\5")
        buf.write(":\u0224\n:\3:\3:\3;\3;\3;\3;\7;\u022c\n;\f;\16;\u022f")
        buf.write("\13;\3;\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3")
        buf.write("A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3")
        buf.write("S\3T\3T\3U\3U\3V\3V\4\u01bb\u022d\2W\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S\2U\2W\2Y+[,]-")
        buf.write("_\2a\2c\2e.g/i\60k\61m\62o\63q\64s\65u\66w\67y\2{\2}\2")
        buf.write("\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2")
        buf.write("\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099")
        buf.write("\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00ab\2\3\2,\3\2\629\4\2ZZzz\5\2\62;CHch\4")
        buf.write("\2DDdd\3\2\62\63\3\2\63;\3\2\62;\4\2GGgg\4\2--//\t\2)")
        buf.write(")^^ddhhppttvv\b\2))^^ddhhttvv\6\2\f\f$$))^^\n\2$$))^^")
        buf.write("ddhhppttvv\6\2\62;C\\aac|\5\2C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"\6\3\n\f\16\17))^^\3\2,,\3\2\61\61\4\2CCcc\4\2EEee\4")
        buf.write("\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMm")
        buf.write("m\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2")
        buf.write("TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2[[{{\4")
        buf.write("\2\\\\||\2\u026f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3\u00ad\3")
        buf.write("\2\2\2\5\u00b4\3\2\2\2\7\u00ba\3\2\2\2\t\u00c3\3\2\2\2")
        buf.write("\13\u00c6\3\2\2\2\r\u00cd\3\2\2\2\17\u00d2\3\2\2\2\21")
        buf.write("\u00d8\3\2\2\2\23\u00e0\3\2\2\2\25\u00e3\3\2\2\2\27\u00ec")
        buf.write("\3\2\2\2\31\u00f2\3\2\2\2\33\u00f9\3\2\2\2\35\u00fb\3")
        buf.write("\2\2\2\37\u00fe\3\2\2\2!\u0102\3\2\2\2#\u0104\3\2\2\2")
        buf.write("%\u0106\3\2\2\2\'\u0108\3\2\2\2)\u010a\3\2\2\2+\u010c")
        buf.write("\3\2\2\2-\u010e\3\2\2\2/\u0111\3\2\2\2\61\u0114\3\2\2")
        buf.write("\2\63\u0117\3\2\2\2\65\u011a\3\2\2\2\67\u011c\3\2\2\2")
        buf.write("9\u011e\3\2\2\2;\u0121\3\2\2\2=\u0124\3\2\2\2?\u0127\3")
        buf.write("\2\2\2A\u0129\3\2\2\2C\u012b\3\2\2\2E\u012d\3\2\2\2G\u012f")
        buf.write("\3\2\2\2I\u0131\3\2\2\2K\u0133\3\2\2\2M\u0135\3\2\2\2")
        buf.write("O\u0137\3\2\2\2Q\u0161\3\2\2\2S\u0164\3\2\2\2U\u0173\3")
        buf.write("\2\2\2W\u017a\3\2\2\2Y\u0183\3\2\2\2[\u018d\3\2\2\2]\u019a")
        buf.write("\3\2\2\2_\u019c\3\2\2\2a\u01a4\3\2\2\2c\u01a9\3\2\2\2")
        buf.write("e\u01ab\3\2\2\2g\u01b5\3\2\2\2i\u01c3\3\2\2\2k\u0201\3")
        buf.write("\2\2\2m\u0203\3\2\2\2o\u020b\3\2\2\2q\u0211\3\2\2\2s\u021b")
        buf.write("\3\2\2\2u\u0227\3\2\2\2w\u0234\3\2\2\2y\u0237\3\2\2\2")
        buf.write("{\u0239\3\2\2\2}\u023b\3\2\2\2\177\u023d\3\2\2\2\u0081")
        buf.write("\u023f\3\2\2\2\u0083\u0241\3\2\2\2\u0085\u0243\3\2\2\2")
        buf.write("\u0087\u0245\3\2\2\2\u0089\u0247\3\2\2\2\u008b\u0249\3")
        buf.write("\2\2\2\u008d\u024b\3\2\2\2\u008f\u024d\3\2\2\2\u0091\u024f")
        buf.write("\3\2\2\2\u0093\u0251\3\2\2\2\u0095\u0253\3\2\2\2\u0097")
        buf.write("\u0255\3\2\2\2\u0099\u0257\3\2\2\2\u009b\u0259\3\2\2\2")
        buf.write("\u009d\u025b\3\2\2\2\u009f\u025d\3\2\2\2\u00a1\u025f\3")
        buf.write("\2\2\2\u00a3\u0261\3\2\2\2\u00a5\u0263\3\2\2\2\u00a7\u0265")
        buf.write("\3\2\2\2\u00a9\u0267\3\2\2\2\u00ab\u0269\3\2\2\2\u00ad")
        buf.write("\u00ae\7t\2\2\u00ae\u00af\5\u0081A\2\u00af\u00b0\5\u009f")
        buf.write("P\2\u00b0\u00b1\5\u00a1Q\2\u00b1\u00b2\5\u009bN\2\u00b2")
        buf.write("\u00b3\5\u0093J\2\u00b3\4\3\2\2\2\u00b4\u00b5\7d\2\2\u00b5")
        buf.write("\u00b6\5\u009bN\2\u00b6\u00b7\5\u0081A\2\u00b7\u00b8\5")
        buf.write("y=\2\u00b8\u00b9\5\u008dG\2\u00b9\6\3\2\2\2\u00ba\u00bb")
        buf.write("\7e\2\2\u00bb\u00bc\5\u0095K\2\u00bc\u00bd\5\u0093J\2")
        buf.write("\u00bd\u00be\5\u009fP\2\u00be\u00bf\5\u0089E\2\u00bf\u00c0")
        buf.write("\5\u0093J\2\u00c0\u00c1\5\u00a1Q\2\u00c1\u00c2\5\u0081")
        buf.write("A\2\u00c2\b\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\5\u0083")
        buf.write("B\2\u00c5\n\3\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\5\u008f")
        buf.write("H\2\u00c8\u00c9\5\u009dO\2\u00c9\u00ca\5\u0081A\2\u00ca")
        buf.write("\u00cb\5\u0089E\2\u00cb\u00cc\5\u0083B\2\u00cc\f\3\2\2")
        buf.write("\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\5\u008fH\2\u00cf\u00d0")
        buf.write("\5\u009dO\2\u00d0\u00d1\5\u0081A\2\u00d1\16\3\2\2\2\u00d2")
        buf.write("\u00d3\7y\2\2\u00d3\u00d4\5\u0087D\2\u00d4\u00d5\5\u0089")
        buf.write("E\2\u00d5\u00d6\5\u008fH\2\u00d6\u00d7\5\u0081A\2\u00d7")
        buf.write("\20\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da\5\u0095K\2")
        buf.write("\u00da\u00db\5\u009bN\2\u00db\u00dc\5\u0081A\2\u00dc\u00dd")
        buf.write("\5y=\2\u00dd\u00de\5}?\2\u00de\u00df\5\u0087D\2\u00df")
        buf.write("\22\3\2\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\5\u009dO\2")
        buf.write("\u00e2\24\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5\5\u00a1")
        buf.write("Q\2\u00e5\u00e6\5\u0093J\2\u00e6\u00e7\5}?\2\u00e7\u00e8")
        buf.write("\5\u009fP\2\u00e8\u00e9\5\u0089E\2\u00e9\u00ea\5\u0095")
        buf.write("K\2\u00ea\u00eb\5\u0093J\2\u00eb\26\3\2\2\2\u00ec\u00ed")
        buf.write("\7c\2\2\u00ed\u00ee\5\u009bN\2\u00ee\u00ef\5\u009bN\2")
        buf.write("\u00ef\u00f0\5y=\2\u00f0\u00f1\5\u00a9U\2\u00f1\30\3\2")
        buf.write("\2\2\u00f2\u00f3\7f\2\2\u00f3\u00f4\5\u0081A\2\u00f4\u00f5")
        buf.write("\5\u0083B\2\u00f5\u00f6\5\u0089E\2\u00f6\u00f7\5\u0093")
        buf.write("J\2\u00f7\u00f8\5\u0081A\2\u00f8\32\3\2\2\2\u00f9\u00fa")
        buf.write("\7?\2\2\u00fa\34\3\2\2\2\u00fb\u00fc\7-\2\2\u00fc\u00fd")
        buf.write("\7\60\2\2\u00fd\36\3\2\2\2\u00fe\u00ff\7?\2\2\u00ff\u0100")
        buf.write("\7?\2\2\u0100\u0101\7\60\2\2\u0101 \3\2\2\2\u0102\u0103")
        buf.write("\7-\2\2\u0103\"\3\2\2\2\u0104\u0105\7/\2\2\u0105$\3\2")
        buf.write("\2\2\u0106\u0107\7,\2\2\u0107&\3\2\2\2\u0108\u0109\7\61")
        buf.write("\2\2\u0109(\3\2\2\2\u010a\u010b\7\'\2\2\u010b*\3\2\2\2")
        buf.write("\u010c\u010d\7#\2\2\u010d,\3\2\2\2\u010e\u010f\7(\2\2")
        buf.write("\u010f\u0110\7(\2\2\u0110.\3\2\2\2\u0111\u0112\7~\2\2")
        buf.write("\u0112\u0113\7~\2\2\u0113\60\3\2\2\2\u0114\u0115\7?\2")
        buf.write("\2\u0115\u0116\7?\2\2\u0116\62\3\2\2\2\u0117\u0118\7#")
        buf.write("\2\2\u0118\u0119\7?\2\2\u0119\64\3\2\2\2\u011a\u011b\7")
        buf.write("@\2\2\u011b\66\3\2\2\2\u011c\u011d\7>\2\2\u011d8\3\2\2")
        buf.write("\2\u011e\u011f\7@\2\2\u011f\u0120\7?\2\2\u0120:\3\2\2")
        buf.write("\2\u0121\u0122\7>\2\2\u0122\u0123\7?\2\2\u0123<\3\2\2")
        buf.write("\2\u0124\u0125\7?\2\2\u0125\u0126\7@\2\2\u0126>\3\2\2")
        buf.write("\2\u0127\u0128\7*\2\2\u0128@\3\2\2\2\u0129\u012a\7+\2")
        buf.write("\2\u012aB\3\2\2\2\u012b\u012c\7]\2\2\u012cD\3\2\2\2\u012d")
        buf.write("\u012e\7_\2\2\u012eF\3\2\2\2\u012f\u0130\7<\2\2\u0130")
        buf.write("H\3\2\2\2\u0131\u0132\7.\2\2\u0132J\3\2\2\2\u0133\u0134")
        buf.write("\7=\2\2\u0134L\3\2\2\2\u0135\u0136\7}\2\2\u0136N\3\2\2")
        buf.write("\2\u0137\u0138\7\177\2\2\u0138P\3\2\2\2\u0139\u013b\7")
        buf.write("\62\2\2\u013a\u013c\t\2\2\2\u013b\u013a\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u0162\3\2\2\2\u013f\u0140\7\62\2\2\u0140\u0142")
        buf.write("\t\3\2\2\u0141\u0143\t\4\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0162\3\2\2\2\u0146\u0147\7\62\2\2\u0147\u0149")
        buf.write("\t\5\2\2\u0148\u014a\t\6\2\2\u0149\u0148\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2")
        buf.write("\u014c\u0162\3\2\2\2\u014d\u0151\t\7\2\2\u014e\u0150\t")
        buf.write("\b\2\2\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u015c\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0154\u0156\7a\2\2\u0155\u0157\t\b\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0154")
        buf.write("\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u0162\3\2\2\2\u015e\u015c\3\2\2\2")
        buf.write("\u015f\u0160\7\62\2\2\u0160\u0162\b)\2\2\u0161\u0139\3")
        buf.write("\2\2\2\u0161\u013f\3\2\2\2\u0161\u0146\3\2\2\2\u0161\u014d")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0162R\3\2\2\2\u0163\u0165")
        buf.write("\t\b\2\2\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0170\3\2\2\2")
        buf.write("\u0168\u016a\7a\2\2\u0169\u016b\t\b\2\2\u016a\u0169\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u0168\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171T\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0177\5[.\2")
        buf.write("\u0174\u0176\5S*\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2")
        buf.write("\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178V\3")
        buf.write("\2\2\2\u0179\u0177\3\2\2\2\u017a\u017c\t\t\2\2\u017b\u017d")
        buf.write("\t\n\2\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017f\3\2\2\2\u017e\u0180\5S*\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182X\3\2\2\2\u0183\u0189\5S*\2\u0184\u0186\5U+\2\u0185")
        buf.write("\u0187\5W,\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u018a\3\2\2\2\u0188\u018a\5W,\2\u0189\u0184\3\2\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\b-\3\2")
        buf.write("\u018cZ\3\2\2\2\u018d\u018e\7\60\2\2\u018e\\\3\2\2\2\u018f")
        buf.write("\u0190\7v\2\2\u0190\u0191\5\u009bN\2\u0191\u0192\5\u00a1")
        buf.write("Q\2\u0192\u0193\5\u0081A\2\u0193\u019b\3\2\2\2\u0194\u0195")
        buf.write("\7h\2\2\u0195\u0196\5y=\2\u0196\u0197\5\u008fH\2\u0197")
        buf.write("\u0198\5\u009dO\2\u0198\u0199\5\u0081A\2\u0199\u019b\3")
        buf.write("\2\2\2\u019a\u018f\3\2\2\2\u019a\u0194\3\2\2\2\u019b^")
        buf.write("\3\2\2\2\u019c\u019d\7^\2\2\u019d\u019e\t\13\2\2\u019e")
        buf.write("`\3\2\2\2\u019f\u01a0\7^\2\2\u01a0\u01a5\t\f\2\2\u01a1")
        buf.write("\u01a5\n\r\2\2\u01a2\u01a3\7)\2\2\u01a3\u01a5\7$\2\2\u01a4")
        buf.write("\u019f\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a5b\3\2\2\2\u01a6\u01a7\7^\2\2\u01a7\u01aa\n\16\2")
        buf.write("\2\u01a8\u01aa\7^\2\2\u01a9\u01a6\3\2\2\2\u01a9\u01a8")
        buf.write("\3\2\2\2\u01aad\3\2\2\2\u01ab\u01af\7$\2\2\u01ac\u01ae")
        buf.write("\5a\61\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b2\u01b3\7$\2\2\u01b3\u01b4\b")
        buf.write("\63\4\2\u01b4f\3\2\2\2\u01b5\u01b6\7\61\2\2\u01b6\u01b7")
        buf.write("\7,\2\2\u01b7\u01bb\3\2\2\2\u01b8\u01ba\13\2\2\2\u01b9")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3")
        buf.write("\2\2\2\u01be\u01bf\7,\2\2\u01bf\u01c0\7\61\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\b\64\5\2\u01c2h\3\2\2\2\u01c3\u01c7")
        buf.write("\7&\2\2\u01c4\u01c6\t\17\2\2\u01c5\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2")
        buf.write("\u01c8j\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01ce\7a\2\2")
        buf.write("\u01cb\u01cd\t\17\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0")
        buf.write("\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u0202\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2\7u\2\2")
        buf.write("\u01d2\u01d3\7v\2\2\u01d3\u01d4\7t\2\2\u01d4\u01d5\7\64")
        buf.write("\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7\7p\2\2\u01d7\u0202")
        buf.write("\7v\2\2\u01d8\u01d9\7k\2\2\u01d9\u01da\7p\2\2\u01da\u01db")
        buf.write("\7v\2\2\u01db\u01dc\7\64\2\2\u01dc\u01dd\7u\2\2\u01dd")
        buf.write("\u01de\7v\2\2\u01de\u0202\7t\2\2\u01df\u01e0\7u\2\2\u01e0")
        buf.write("\u01e1\7v\2\2\u01e1\u01e2\7t\2\2\u01e2\u01e3\7\64\2\2")
        buf.write("\u01e3\u01e4\7h\2\2\u01e4\u01e5\7n\2\2\u01e5\u01e6\7q")
        buf.write("\2\2\u01e6\u01e7\7c\2\2\u01e7\u0202\7v\2\2\u01e8\u01e9")
        buf.write("\7h\2\2\u01e9\u01ea\7n\2\2\u01ea\u01eb\7q\2\2\u01eb\u01ec")
        buf.write("\7c\2\2\u01ec\u01ed\7v\2\2\u01ed\u01ee\7\64\2\2\u01ee")
        buf.write("\u01ef\7u\2\2\u01ef\u01f0\7v\2\2\u01f0\u0202\7t\2\2\u01f1")
        buf.write("\u01f2\7u\2\2\u01f2\u01f3\7v\2\2\u01f3\u01f4\7t\2\2\u01f4")
        buf.write("\u01f5\7\64\2\2\u01f5\u01f6\7d\2\2\u01f6\u01f7\7q\2\2")
        buf.write("\u01f7\u01f8\7q\2\2\u01f8\u0202\7n\2\2\u01f9\u01fa\7d")
        buf.write("\2\2\u01fa\u01fb\7q\2\2\u01fb\u01fc\7q\2\2\u01fc\u01fd")
        buf.write("\7n\2\2\u01fd\u01fe\7\64\2\2\u01fe\u01ff\7u\2\2\u01ff")
        buf.write("\u0200\7v\2\2\u0200\u0202\7t\2\2\u0201\u01ca\3\2\2\2\u0201")
        buf.write("\u01d1\3\2\2\2\u0201\u01d8\3\2\2\2\u0201\u01df\3\2\2\2")
        buf.write("\u0201\u01e8\3\2\2\2\u0201\u01f1\3\2\2\2\u0201\u01f9\3")
        buf.write("\2\2\2\u0202l\3\2\2\2\u0203\u0207\t\20\2\2\u0204\u0206")
        buf.write("\t\17\2\2\u0205\u0204\3\2\2\2\u0206\u0209\3\2\2\2\u0207")
        buf.write("\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208n\3\2\2\2\u0209")
        buf.write("\u0207\3\2\2\2\u020a\u020c\t\21\2\2\u020b\u020a\3\2\2")
        buf.write("\2\u020c\u020d\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0210\b8\5\2\u0210")
        buf.write("p\3\2\2\2\u0211\u0215\7$\2\2\u0212\u0214\5a\61\2\u0213")
        buf.write("\u0212\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0215\u0216\3\2\2\2\u0216\u0218\3\2\2\2\u0217\u0215\3")
        buf.write("\2\2\2\u0218\u0219\5c\62\2\u0219\u021a\b9\6\2\u021ar\3")
        buf.write("\2\2\2\u021b\u021f\7$\2\2\u021c\u021e\5a\61\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d\3\2\2\2\u021f")
        buf.write("\u0220\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2")
        buf.write("\u0222\u0224\t\22\2\2\u0223\u0222\3\2\2\2\u0224\u0225")
        buf.write("\3\2\2\2\u0225\u0226\b:\7\2\u0226t\3\2\2\2\u0227\u0228")
        buf.write("\7\61\2\2\u0228\u0229\7,\2\2\u0229\u022d\3\2\2\2\u022a")
        buf.write("\u022c\13\2\2\2\u022b\u022a\3\2\2\2\u022c\u022f\3\2\2")
        buf.write("\2\u022d\u022e\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u0230")
        buf.write("\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0231\n\23\2\2\u0231")
        buf.write("\u0232\n\24\2\2\u0232\u0233\b;\b\2\u0233v\3\2\2\2\u0234")
        buf.write("\u0235\13\2\2\2\u0235\u0236\b<\t\2\u0236x\3\2\2\2\u0237")
        buf.write("\u0238\t\25\2\2\u0238z\3\2\2\2\u0239\u023a\t\5\2\2\u023a")
        buf.write("|\3\2\2\2\u023b\u023c\t\26\2\2\u023c~\3\2\2\2\u023d\u023e")
        buf.write("\t\27\2\2\u023e\u0080\3\2\2\2\u023f\u0240\t\t\2\2\u0240")
        buf.write("\u0082\3\2\2\2\u0241\u0242\t\30\2\2\u0242\u0084\3\2\2")
        buf.write("\2\u0243\u0244\t\31\2\2\u0244\u0086\3\2\2\2\u0245\u0246")
        buf.write("\t\32\2\2\u0246\u0088\3\2\2\2\u0247\u0248\t\33\2\2\u0248")
        buf.write("\u008a\3\2\2\2\u0249\u024a\t\34\2\2\u024a\u008c\3\2\2")
        buf.write("\2\u024b\u024c\t\35\2\2\u024c\u008e\3\2\2\2\u024d\u024e")
        buf.write("\t\36\2\2\u024e\u0090\3\2\2\2\u024f\u0250\t\37\2\2\u0250")
        buf.write("\u0092\3\2\2\2\u0251\u0252\t \2\2\u0252\u0094\3\2\2\2")
        buf.write("\u0253\u0254\t!\2\2\u0254\u0096\3\2\2\2\u0255\u0256\t")
        buf.write("\"\2\2\u0256\u0098\3\2\2\2\u0257\u0258\t#\2\2\u0258\u009a")
        buf.write("\3\2\2\2\u0259\u025a\t$\2\2\u025a\u009c\3\2\2\2\u025b")
        buf.write("\u025c\t%\2\2\u025c\u009e\3\2\2\2\u025d\u025e\t&\2\2\u025e")
        buf.write("\u00a0\3\2\2\2\u025f\u0260\t\'\2\2\u0260\u00a2\3\2\2\2")
        buf.write("\u0261\u0262\t(\2\2\u0262\u00a4\3\2\2\2\u0263\u0264\t")
        buf.write(")\2\2\u0264\u00a6\3\2\2\2\u0265\u0266\t\3\2\2\u0266\u00a8")
        buf.write("\3\2\2\2\u0267\u0268\t*\2\2\u0268\u00aa\3\2\2\2\u0269")
        buf.write("\u026a\t+\2\2\u026a\u00ac\3\2\2\2 \2\u013d\u0144\u014b")
        buf.write("\u0151\u0158\u015c\u0161\u0166\u016c\u0170\u0177\u017c")
        buf.write("\u0181\u0186\u0189\u019a\u01a4\u01a9\u01af\u01bb\u01c7")
        buf.write("\u01ce\u0201\u0207\u020d\u0215\u021f\u0223\u022d\n\3)")
        buf.write("\2\3-\3\3\63\4\b\2\2\39\5\3:\6\3;\7\3<\b")
        return buf.getvalue()


class D95Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    WHILE = 7
    FOREACH = 8
    AS = 9
    FUNCTION = 10
    ARRAY = 11
    DEFINE = 12
    ASSIGN = 13
    CONCATSTR = 14
    COMPSTR = 15
    ADD = 16
    MINUS = 17
    MUL = 18
    DIV = 19
    MOD = 20
    NOT = 21
    AND = 22
    OR = 23
    EQ = 24
    NEQ = 25
    GT = 26
    LT = 27
    GTE = 28
    LTE = 29
    ASSO = 30
    LP = 31
    RP = 32
    LSB = 33
    RSB = 34
    COLON = 35
    COMMA = 36
    SEMI = 37
    LCB = 38
    RCB = 39
    INTLIT = 40
    FLOATLIT = 41
    DOT = 42
    BOOLEAN = 43
    STRINGLIT = 44
    BLOCKCOMMENT = 45
    VAR_NAME = 46
    FUNCTION_NAME = 47
    CONSTANT_NAME = 48
    WS = 49
    ILLEGAL_ESCAPE = 50
    UNCLOSE_STRING = 51
    UNTERMINATED_COMMENT = 52
    ERROR_CHAR = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+.'", "'==.'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
            "'=>'", "'('", "')'", "'['", "']'", "':'", "','", "';'", "'{'", 
            "'}'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "WHILE", 
            "FOREACH", "AS", "FUNCTION", "ARRAY", "DEFINE", "ASSIGN", "CONCATSTR", 
            "COMPSTR", "ADD", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", 
            "OR", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "ASSO", "LP", "RP", 
            "LSB", "RSB", "COLON", "COMMA", "SEMI", "LCB", "RCB", "INTLIT", 
            "FLOATLIT", "DOT", "BOOLEAN", "STRINGLIT", "BLOCKCOMMENT", "VAR_NAME", 
            "FUNCTION_NAME", "CONSTANT_NAME", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "RETURN", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "WHILE", "FOREACH", "AS", "FUNCTION", "ARRAY", "DEFINE", 
                  "ASSIGN", "CONCATSTR", "COMPSTR", "ADD", "MINUS", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NEQ", "GT", "LT", 
                  "GTE", "LTE", "ASSO", "LP", "RP", "LSB", "RSB", "COLON", 
                  "COMMA", "SEMI", "LCB", "RCB", "INTLIT", "INTPART", "DECPART", 
                  "EXPOPART", "FLOATLIT", "DOT", "BOOLEAN", "ESC_SEQ", "STRINGCHAR", 
                  "ESC_ILLEGAL", "STRINGLIT", "BLOCKCOMMENT", "VAR_NAME", 
                  "FUNCTION_NAME", "CONSTANT_NAME", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR", 
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z" ]

    grammarFileName = "D95.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[39] = self.INTLIT_action 
            actions[43] = self.FLOATLIT_action 
            actions[49] = self.STRINGLIT_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.UNTERMINATED_COMMENT_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        y = str(self.text)
                        x = re.sub("_","",y)
                        self.text = x[0:]
                    
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                        y = str(self.text)
                        x = re.sub("_","",y)
                        self.text = x[0:]
                    
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise UncloseString(y[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    raise UnterminatedComment()
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            		raise ErrorToken(self.text)
            	
     


