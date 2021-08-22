# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u01b7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\3\2\3\2\6\2b\n\2\r\2\16\2c\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u0086\n\6\3\7\3\7\3\b\3\b\3\b\5\b\u008d\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\7\t\u0095\n\t\f\t\16\t\u0098\13\t")
        buf.write("\3\t\3\t\7\t\u009c\n\t\f\t\16\t\u009f\13\t\3\t\5\t\u00a2")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00aa\n\n\f\n\16\n\u00ad")
        buf.write("\13\n\3\n\3\n\3\13\3\13\3\13\7\13\u00b4\n\13\f\13\16\13")
        buf.write("\u00b7\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\7\f\u00c5\n\f\f\f\16\f\u00c8\13\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\7\r\u00d2\n\r\f\r\16\r\u00d5\13\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\5\21\u00e7\n\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u00f0\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00f7\n\23\3\24\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u00fe\n\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0106")
        buf.write("\n\25\f\25\16\25\u0109\13\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\7\26\u0111\n\26\f\26\16\26\u0114\13\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\7\27\u011c\n\27\f\27\16\27\u011f")
        buf.write("\13\27\3\30\3\30\3\30\5\30\u0124\n\30\3\31\3\31\3\31\5")
        buf.write("\31\u0129\n\31\3\32\3\32\3\32\3\32\3\32\6\32\u0130\n\32")
        buf.write("\r\32\16\32\u0131\7\32\u0134\n\32\f\32\16\32\u0137\13")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u013f\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0146\n\34\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u014c\n\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\7\37\u0156\n\37\f\37\16\37\u0159\13\37\3\37\5\37")
        buf.write("\u015c\n\37\3 \3 \3 \3 \3!\3!\6!\u0164\n!\r!\16!\u0165")
        buf.write("\3\"\3\"\3\"\7\"\u016b\n\"\f\"\16\"\u016e\13\"\3\"\5\"")
        buf.write("\u0171\n\"\3#\6#\u0174\n#\r#\16#\u0175\3$\3$\5$\u017a")
        buf.write("\n$\3%\3%\3&\3&\3\'\3\'\3\'\5\'\u0183\n\'\3(\3(\3(\3(")
        buf.write("\3(\3)\3)\3)\7)\u018d\n)\f)\16)\u0190\13)\3*\3*\3*\3*")
        buf.write("\3*\7*\u0197\n*\f*\16*\u019a\13*\3*\3*\3+\3+\3+\3+\3,")
        buf.write("\3,\3,\3,\3,\7,\u01a7\n,\f,\16,\u01aa\13,\3,\3,\3-\3-")
        buf.write("\3-\5-\u01b1\n-\3.\3.\3/\3/\3/\2\6(*,\62\60\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\\2\13\3\2\20\21\3\2\32\37\3\2\30\31\3")
        buf.write("\2\22\23\3\2\24\26\3\2\60\62\4\2*+-.\4\2**..\4\2\60\60")
        buf.write("\62\62\2\u01b9\2a\3\2\2\2\4g\3\2\2\2\6l\3\2\2\2\bt\3\2")
        buf.write("\2\2\n\u0085\3\2\2\2\f\u0087\3\2\2\2\16\u008c\3\2\2\2")
        buf.write("\20\u008e\3\2\2\2\22\u00a3\3\2\2\2\24\u00b0\3\2\2\2\26")
        buf.write("\u00ba\3\2\2\2\30\u00cb\3\2\2\2\32\u00d8\3\2\2\2\34\u00db")
        buf.write("\3\2\2\2\36\u00de\3\2\2\2 \u00e4\3\2\2\2\"\u00ef\3\2\2")
        buf.write("\2$\u00f6\3\2\2\2&\u00fd\3\2\2\2(\u00ff\3\2\2\2*\u010a")
        buf.write("\3\2\2\2,\u0115\3\2\2\2.\u0123\3\2\2\2\60\u0128\3\2\2")
        buf.write("\2\62\u012a\3\2\2\2\64\u013e\3\2\2\2\66\u0145\3\2\2\2")
        buf.write("8\u014b\3\2\2\2:\u014d\3\2\2\2<\u015b\3\2\2\2>\u015d\3")
        buf.write("\2\2\2@\u0161\3\2\2\2B\u0170\3\2\2\2D\u0173\3\2\2\2F\u0179")
        buf.write("\3\2\2\2H\u017b\3\2\2\2J\u017d\3\2\2\2L\u0182\3\2\2\2")
        buf.write("N\u0184\3\2\2\2P\u0189\3\2\2\2R\u0191\3\2\2\2T\u019d\3")
        buf.write("\2\2\2V\u01a1\3\2\2\2X\u01b0\3\2\2\2Z\u01b2\3\2\2\2\\")
        buf.write("\u01b4\3\2\2\2^b\5\4\3\2_b\5\6\4\2`b\5\b\5\2a^\3\2\2\2")
        buf.write("a_\3\2\2\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2de\3")
        buf.write("\2\2\2ef\7\2\2\3f\3\3\2\2\2gh\5\16\b\2hi\7\17\2\2ij\5")
        buf.write("\"\22\2jk\7\'\2\2k\5\3\2\2\2lm\7\16\2\2mn\7!\2\2no\7\62")
        buf.write("\2\2op\7&\2\2pq\5\"\22\2qr\7\"\2\2rs\7\'\2\2s\7\3\2\2")
        buf.write("\2tu\7\f\2\2uv\7\61\2\2vw\7!\2\2wx\5B\"\2xy\7\"\2\2yz")
        buf.write("\7(\2\2z{\5D#\2{|\7)\2\2|\t\3\2\2\2}\u0086\5\f\7\2~\u0086")
        buf.write("\5\20\t\2\177\u0086\5\26\f\2\u0080\u0086\5\30\r\2\u0081")
        buf.write("\u0086\5\32\16\2\u0082\u0086\5\34\17\2\u0083\u0086\5\36")
        buf.write("\20\2\u0084\u0086\5 \21\2\u0085}\3\2\2\2\u0085~\3\2\2")
        buf.write("\2\u0085\177\3\2\2\2\u0085\u0080\3\2\2\2\u0085\u0081\3")
        buf.write("\2\2\2\u0085\u0082\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0084")
        buf.write("\3\2\2\2\u0086\13\3\2\2\2\u0087\u0088\5\4\3\2\u0088\r")
        buf.write("\3\2\2\2\u0089\u008d\7\60\2\2\u008a\u008d\7\62\2\2\u008b")
        buf.write("\u008d\5@!\2\u008c\u0089\3\2\2\2\u008c\u008a\3\2\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\17\3\2\2\2\u008e\u008f\7\6\2\2\u008f")
        buf.write("\u0090\7!\2\2\u0090\u0091\5\"\22\2\u0091\u0092\7\"\2\2")
        buf.write("\u0092\u0096\7(\2\2\u0093\u0095\5\n\6\2\u0094\u0093\3")
        buf.write("\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099")
        buf.write("\u009d\7)\2\2\u009a\u009c\5\22\n\2\u009b\u009a\3\2\2\2")
        buf.write("\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3")
        buf.write("\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2")
        buf.write("\5\24\13\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\21\3\2\2\2\u00a3\u00a4\7\7\2\2\u00a4\u00a5\7!\2\2\u00a5")
        buf.write("\u00a6\5\"\22\2\u00a6\u00a7\7\"\2\2\u00a7\u00ab\7(\2\2")
        buf.write("\u00a8\u00aa\5\n\6\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae")
        buf.write("\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\7)\2\2\u00af")
        buf.write("\23\3\2\2\2\u00b0\u00b1\7\b\2\2\u00b1\u00b5\7(\2\2\u00b2")
        buf.write("\u00b4\5\n\6\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3")
        buf.write("\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7)\2\2\u00b9\25")
        buf.write("\3\2\2\2\u00ba\u00bb\7\n\2\2\u00bb\u00bc\7!\2\2\u00bc")
        buf.write("\u00bd\5\\/\2\u00bd\u00be\7\13\2\2\u00be\u00bf\5\\/\2")
        buf.write("\u00bf\u00c0\7 \2\2\u00c0\u00c1\5\\/\2\u00c1\u00c2\7\"")
        buf.write("\2\2\u00c2\u00c6\7(\2\2\u00c3\u00c5\5\n\6\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c9\u00ca\7)\2\2\u00ca\27\3\2\2\2\u00cb\u00cc\7\t\2")
        buf.write("\2\u00cc\u00cd\7!\2\2\u00cd\u00ce\5\"\22\2\u00ce\u00cf")
        buf.write("\7\"\2\2\u00cf\u00d3\7(\2\2\u00d0\u00d2\5\n\6\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3")
        buf.write("\2\2\2\u00d6\u00d7\7)\2\2\u00d7\31\3\2\2\2\u00d8\u00d9")
        buf.write("\7\4\2\2\u00d9\u00da\7\'\2\2\u00da\33\3\2\2\2\u00db\u00dc")
        buf.write("\7\5\2\2\u00dc\u00dd\7\'\2\2\u00dd\35\3\2\2\2\u00de\u00df")
        buf.write("\7\61\2\2\u00df\u00e0\7!\2\2\u00e0\u00e1\5<\37\2\u00e1")
        buf.write("\u00e2\7\"\2\2\u00e2\u00e3\7\'\2\2\u00e3\37\3\2\2\2\u00e4")
        buf.write("\u00e6\7\3\2\2\u00e5\u00e7\5\"\22\2\u00e6\u00e5\3\2\2")
        buf.write("\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9")
        buf.write("\7\'\2\2\u00e9!\3\2\2\2\u00ea\u00eb\5$\23\2\u00eb\u00ec")
        buf.write("\7 \2\2\u00ec\u00ed\5$\23\2\u00ed\u00f0\3\2\2\2\u00ee")
        buf.write("\u00f0\5$\23\2\u00ef\u00ea\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0#\3\2\2\2\u00f1\u00f2\5&\24\2\u00f2\u00f3\t\2\2")
        buf.write("\2\u00f3\u00f4\5&\24\2\u00f4\u00f7\3\2\2\2\u00f5\u00f7")
        buf.write("\5&\24\2\u00f6\u00f1\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("%\3\2\2\2\u00f8\u00f9\5(\25\2\u00f9\u00fa\t\3\2\2\u00fa")
        buf.write("\u00fb\5(\25\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5(\25\2")
        buf.write("\u00fd\u00f8\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\'\3\2\2")
        buf.write("\2\u00ff\u0100\b\25\1\2\u0100\u0101\5*\26\2\u0101\u0107")
        buf.write("\3\2\2\2\u0102\u0103\f\4\2\2\u0103\u0104\t\4\2\2\u0104")
        buf.write("\u0106\5*\26\2\u0105\u0102\3\2\2\2\u0106\u0109\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108)\3\2\2")
        buf.write("\2\u0109\u0107\3\2\2\2\u010a\u010b\b\26\1\2\u010b\u010c")
        buf.write("\5,\27\2\u010c\u0112\3\2\2\2\u010d\u010e\f\4\2\2\u010e")
        buf.write("\u010f\t\5\2\2\u010f\u0111\5,\27\2\u0110\u010d\3\2\2\2")
        buf.write("\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3")
        buf.write("\2\2\2\u0113+\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116")
        buf.write("\b\27\1\2\u0116\u0117\5.\30\2\u0117\u011d\3\2\2\2\u0118")
        buf.write("\u0119\f\4\2\2\u0119\u011a\t\6\2\2\u011a\u011c\5.\30\2")
        buf.write("\u011b\u0118\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3")
        buf.write("\2\2\2\u011d\u011e\3\2\2\2\u011e-\3\2\2\2\u011f\u011d")
        buf.write("\3\2\2\2\u0120\u0121\7\27\2\2\u0121\u0124\5.\30\2\u0122")
        buf.write("\u0124\5\60\31\2\u0123\u0120\3\2\2\2\u0123\u0122\3\2\2")
        buf.write("\2\u0124/\3\2\2\2\u0125\u0126\7\23\2\2\u0126\u0129\5\60")
        buf.write("\31\2\u0127\u0129\5\62\32\2\u0128\u0125\3\2\2\2\u0128")
        buf.write("\u0127\3\2\2\2\u0129\61\3\2\2\2\u012a\u012b\b\32\1\2\u012b")
        buf.write("\u012c\5\64\33\2\u012c\u0135\3\2\2\2\u012d\u012f\f\4\2")
        buf.write("\2\u012e\u0130\5> \2\u012f\u012e\3\2\2\2\u0130\u0131\3")
        buf.write("\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134")
        buf.write("\3\2\2\2\u0133\u012d\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\63\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u0139\5\66\34\2\u0139\u013a\7!\2")
        buf.write("\2\u013a\u013b\5<\37\2\u013b\u013c\7\"\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013f\5\66\34\2\u013e\u0138\3\2\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013f\65\3\2\2\2\u0140\u0141\7!\2\2\u0141")
        buf.write("\u0142\5\"\22\2\u0142\u0143\7\"\2\2\u0143\u0146\3\2\2")
        buf.write("\2\u0144\u0146\58\35\2\u0145\u0140\3\2\2\2\u0145\u0144")
        buf.write("\3\2\2\2\u0146\67\3\2\2\2\u0147\u014c\5H%\2\u0148\u014c")
        buf.write("\5J&\2\u0149\u014c\5:\36\2\u014a\u014c\5L\'\2\u014b\u0147")
        buf.write("\3\2\2\2\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014c9\3\2\2\2\u014d\u014e\7\61\2\2\u014e")
        buf.write("\u014f\7!\2\2\u014f\u0150\5<\37\2\u0150\u0151\7\"\2\2")
        buf.write("\u0151;\3\2\2\2\u0152\u0157\5\"\22\2\u0153\u0154\7&\2")
        buf.write("\2\u0154\u0156\5\"\22\2\u0155\u0153\3\2\2\2\u0156\u0159")
        buf.write("\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("\u015c\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015c\3\2\2\2")
        buf.write("\u015b\u0152\3\2\2\2\u015b\u015a\3\2\2\2\u015c=\3\2\2")
        buf.write("\2\u015d\u015e\7#\2\2\u015e\u015f\5\"\22\2\u015f\u0160")
        buf.write("\7$\2\2\u0160?\3\2\2\2\u0161\u0163\5H%\2\u0162\u0164\5")
        buf.write("> \2\u0163\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166A\3\2\2\2\u0167\u016c")
        buf.write("\7\60\2\2\u0168\u0169\7&\2\2\u0169\u016b\7\60\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u0171\3\2\2\2\u016e\u016c\3")
        buf.write("\2\2\2\u016f\u0171\3\2\2\2\u0170\u0167\3\2\2\2\u0170\u016f")
        buf.write("\3\2\2\2\u0171C\3\2\2\2\u0172\u0174\5\n\6\2\u0173\u0172")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176E\3\2\2\2\u0177\u017a\5J&\2\u0178")
        buf.write("\u017a\5L\'\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2")
        buf.write("\u017aG\3\2\2\2\u017b\u017c\t\7\2\2\u017cI\3\2\2\2\u017d")
        buf.write("\u017e\t\b\2\2\u017eK\3\2\2\2\u017f\u0183\5N(\2\u0180")
        buf.write("\u0183\5R*\2\u0181\u0183\5V,\2\u0182\u017f\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183M\3\2\2\2\u0184")
        buf.write("\u0185\7\r\2\2\u0185\u0186\7!\2\2\u0186\u0187\5P)\2\u0187")
        buf.write("\u0188\7\"\2\2\u0188O\3\2\2\2\u0189\u018e\5J&\2\u018a")
        buf.write("\u018b\7&\2\2\u018b\u018d\5J&\2\u018c\u018a\3\2\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018fQ\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\7\r\2")
        buf.write("\2\u0192\u0193\7!\2\2\u0193\u0198\5T+\2\u0194\u0195\7")
        buf.write("&\2\2\u0195\u0197\5T+\2\u0196\u0194\3\2\2\2\u0197\u019a")
        buf.write("\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u019b\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7\"\2\2")
        buf.write("\u019cS\3\2\2\2\u019d\u019e\5Z.\2\u019e\u019f\7 \2\2\u019f")
        buf.write("\u01a0\5\"\22\2\u01a0U\3\2\2\2\u01a1\u01a2\7\r\2\2\u01a2")
        buf.write("\u01a3\7!\2\2\u01a3\u01a8\5X-\2\u01a4\u01a5\7&\2\2\u01a5")
        buf.write("\u01a7\5X-\2\u01a6\u01a4\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ac\7\"\2\2\u01acW\3\2\2")
        buf.write("\2\u01ad\u01b1\5N(\2\u01ae\u01b1\5R*\2\u01af\u01b1\5V")
        buf.write(",\2\u01b0\u01ad\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1Y\3\2\2\2\u01b2\u01b3\t\t\2\2\u01b3[\3\2")
        buf.write("\2\2\u01b4\u01b5\t\n\2\2\u01b5]\3\2\2\2\'ac\u0085\u008c")
        buf.write("\u0096\u009d\u00a1\u00ab\u00b5\u00c6\u00d3\u00e6\u00ef")
        buf.write("\u00f6\u00fd\u0107\u0112\u011d\u0123\u0128\u0131\u0135")
        buf.write("\u013e\u0145\u014b\u0157\u015b\u0165\u016c\u0170\u0175")
        buf.write("\u0179\u0182\u018e\u0198\u01a8\u01b0")
        return buf.getvalue()


class D95Parser ( Parser ):

    grammarFileName = "D95.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'+.'", "'==.'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'=>'", "'('", 
                     "')'", "'['", "']'", "':'", "','", "';'", "'{'", "'}'", 
                     "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "RETURN", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "WHILE", "FOREACH", "AS", "FUNCTION", 
                      "ARRAY", "DEFINE", "ASSIGN", "CONCATSTR", "COMPSTR", 
                      "ADD", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", 
                      "OR", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "ASSO", 
                      "LP", "RP", "LSB", "RSB", "COLON", "COMMA", "SEMI", 
                      "LCB", "RCB", "INTLIT", "FLOATLIT", "DOT", "BOOLEAN", 
                      "STRINGLIT", "BLOCKCOMMENT", "VAR_NAME", "FUNCTION_NAME", 
                      "CONSTANT_NAME", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_const_declare = 2
    RULE_func_declare = 3
    RULE_stmt = 4
    RULE_assign_stmt = 5
    RULE_assign_lhs = 6
    RULE_if_stmt = 7
    RULE_elif_part = 8
    RULE_else_part = 9
    RULE_foreach_stmt = 10
    RULE_while_stmt = 11
    RULE_break_stmt = 12
    RULE_continue_stmt = 13
    RULE_call_stmt = 14
    RULE_return_stmt = 15
    RULE_exp = 16
    RULE_exp1 = 17
    RULE_exp2 = 18
    RULE_exp3 = 19
    RULE_exp4 = 20
    RULE_exp5 = 21
    RULE_exp6 = 22
    RULE_exp7 = 23
    RULE_exp8 = 24
    RULE_exp9 = 25
    RULE_exp10 = 26
    RULE_operands = 27
    RULE_func_call = 28
    RULE_func_params = 29
    RULE_index_exp = 30
    RULE_index_opr = 31
    RULE_params = 32
    RULE_body = 33
    RULE_literal = 34
    RULE_identifier = 35
    RULE_primitive_lit = 36
    RULE_array_lit = 37
    RULE_index_arr = 38
    RULE_index_arr_body = 39
    RULE_asso_arr = 40
    RULE_asso_ele = 41
    RULE_multidim_arr = 42
    RULE_multidim_arr_ele = 43
    RULE_asso_key = 44
    RULE_fe_id = 45

    ruleNames =  [ "program", "var_declare", "const_declare", "func_declare", 
                   "stmt", "assign_stmt", "assign_lhs", "if_stmt", "elif_part", 
                   "else_part", "foreach_stmt", "while_stmt", "break_stmt", 
                   "continue_stmt", "call_stmt", "return_stmt", "exp", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", 
                   "exp9", "exp10", "operands", "func_call", "func_params", 
                   "index_exp", "index_opr", "params", "body", "literal", 
                   "identifier", "primitive_lit", "array_lit", "index_arr", 
                   "index_arr_body", "asso_arr", "asso_ele", "multidim_arr", 
                   "multidim_arr_ele", "asso_key", "fe_id" ]

    EOF = Token.EOF
    RETURN=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    WHILE=7
    FOREACH=8
    AS=9
    FUNCTION=10
    ARRAY=11
    DEFINE=12
    ASSIGN=13
    CONCATSTR=14
    COMPSTR=15
    ADD=16
    MINUS=17
    MUL=18
    DIV=19
    MOD=20
    NOT=21
    AND=22
    OR=23
    EQ=24
    NEQ=25
    GT=26
    LT=27
    GTE=28
    LTE=29
    ASSO=30
    LP=31
    RP=32
    LSB=33
    RSB=34
    COLON=35
    COMMA=36
    SEMI=37
    LCB=38
    RCB=39
    INTLIT=40
    FLOATLIT=41
    DOT=42
    BOOLEAN=43
    STRINGLIT=44
    BLOCKCOMMENT=45
    VAR_NAME=46
    FUNCTION_NAME=47
    CONSTANT_NAME=48
    WS=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    UNTERMINATED_COMMENT=52
    ERROR_CHAR=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D95Parser.EOF, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Var_declareContext)
            else:
                return self.getTypedRuleContext(D95Parser.Var_declareContext,i)


        def const_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Const_declareContext)
            else:
                return self.getTypedRuleContext(D95Parser.Const_declareContext,i)


        def func_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Func_declareContext)
            else:
                return self.getTypedRuleContext(D95Parser.Func_declareContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D95Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 95
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D95Parser.VAR_NAME, D95Parser.FUNCTION_NAME, D95Parser.CONSTANT_NAME]:
                    self.state = 92
                    self.var_declare()
                    pass
                elif token in [D95Parser.DEFINE]:
                    self.state = 93
                    self.const_declare()
                    pass
                elif token in [D95Parser.FUNCTION]:
                    self.state = 94
                    self.func_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.FUNCTION) | (1 << D95Parser.DEFINE) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0)):
                    break

            self.state = 99
            self.match(D95Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D95Parser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(D95Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = D95Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.assign_lhs()
            self.state = 102
            self.match(D95Parser.ASSIGN)
            self.state = 103
            self.exp()
            self.state = 104
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(D95Parser.DEFINE, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def CONSTANT_NAME(self):
            return self.getToken(D95Parser.CONSTANT_NAME, 0)

        def COMMA(self):
            return self.getToken(D95Parser.COMMA, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_const_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declare" ):
                return visitor.visitConst_declare(self)
            else:
                return visitor.visitChildren(self)




    def const_declare(self):

        localctx = D95Parser.Const_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_const_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(D95Parser.DEFINE)
            self.state = 107
            self.match(D95Parser.LP)
            self.state = 108
            self.match(D95Parser.CONSTANT_NAME)
            self.state = 109
            self.match(D95Parser.COMMA)
            self.state = 110
            self.exp()
            self.state = 111
            self.match(D95Parser.RP)
            self.state = 112
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(D95Parser.FUNCTION, 0)

        def FUNCTION_NAME(self):
            return self.getToken(D95Parser.FUNCTION_NAME, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def params(self):
            return self.getTypedRuleContext(D95Parser.ParamsContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LCB(self):
            return self.getToken(D95Parser.LCB, 0)

        def body(self):
            return self.getTypedRuleContext(D95Parser.BodyContext,0)


        def RCB(self):
            return self.getToken(D95Parser.RCB, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = D95Parser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(D95Parser.FUNCTION)
            self.state = 115
            self.match(D95Parser.FUNCTION_NAME)
            self.state = 116
            self.match(D95Parser.LP)
            self.state = 117
            self.params()
            self.state = 118
            self.match(D95Parser.RP)
            self.state = 119
            self.match(D95Parser.LCB)
            self.state = 120
            self.body()
            self.state = 121
            self.match(D95Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(D95Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D95Parser.If_stmtContext,0)


        def foreach_stmt(self):
            return self.getTypedRuleContext(D95Parser.Foreach_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(D95Parser.While_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D95Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D95Parser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(D95Parser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D95Parser.Return_stmtContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D95Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.foreach_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 129
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 130
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(D95Parser.Var_declareContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D95Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.var_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(D95Parser.VAR_NAME, 0)

        def CONSTANT_NAME(self):
            return self.getToken(D95Parser.CONSTANT_NAME, 0)

        def index_opr(self):
            return self.getTypedRuleContext(D95Parser.Index_oprContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D95Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign_lhs)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(D95Parser.VAR_NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(D95Parser.CONSTANT_NAME)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.index_opr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D95Parser.IF, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LCB(self):
            return self.getToken(D95Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D95Parser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D95Parser.StmtContext,i)


        def elif_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Elif_partContext)
            else:
                return self.getTypedRuleContext(D95Parser.Elif_partContext,i)


        def else_part(self):
            return self.getTypedRuleContext(D95Parser.Else_partContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D95Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(D95Parser.IF)
            self.state = 141
            self.match(D95Parser.LP)
            self.state = 142
            self.exp()
            self.state = 143
            self.match(D95Parser.RP)
            self.state = 144
            self.match(D95Parser.LCB)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.RETURN) | (1 << D95Parser.BREAK) | (1 << D95Parser.CONTINUE) | (1 << D95Parser.IF) | (1 << D95Parser.WHILE) | (1 << D95Parser.FOREACH) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0):
                self.state = 145
                self.stmt()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(D95Parser.RCB)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D95Parser.ELSEIF:
                self.state = 152
                self.elif_part()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D95Parser.ELSE:
                self.state = 158
                self.else_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D95Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LCB(self):
            return self.getToken(D95Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D95Parser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D95Parser.StmtContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_elif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_part" ):
                return visitor.visitElif_part(self)
            else:
                return visitor.visitChildren(self)




    def elif_part(self):

        localctx = D95Parser.Elif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elif_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(D95Parser.ELSEIF)
            self.state = 162
            self.match(D95Parser.LP)
            self.state = 163
            self.exp()
            self.state = 164
            self.match(D95Parser.RP)
            self.state = 165
            self.match(D95Parser.LCB)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.RETURN) | (1 << D95Parser.BREAK) | (1 << D95Parser.CONTINUE) | (1 << D95Parser.IF) | (1 << D95Parser.WHILE) | (1 << D95Parser.FOREACH) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0):
                self.state = 166
                self.stmt()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(D95Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D95Parser.ELSE, 0)

        def LCB(self):
            return self.getToken(D95Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D95Parser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D95Parser.StmtContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = D95Parser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_else_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(D95Parser.ELSE)
            self.state = 175
            self.match(D95Parser.LCB)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.RETURN) | (1 << D95Parser.BREAK) | (1 << D95Parser.CONTINUE) | (1 << D95Parser.IF) | (1 << D95Parser.WHILE) | (1 << D95Parser.FOREACH) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0):
                self.state = 176
                self.stmt()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(D95Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D95Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def fe_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Fe_idContext)
            else:
                return self.getTypedRuleContext(D95Parser.Fe_idContext,i)


        def AS(self):
            return self.getToken(D95Parser.AS, 0)

        def ASSO(self):
            return self.getToken(D95Parser.ASSO, 0)

        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LCB(self):
            return self.getToken(D95Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D95Parser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D95Parser.StmtContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_foreach_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_stmt" ):
                return visitor.visitForeach_stmt(self)
            else:
                return visitor.visitChildren(self)




    def foreach_stmt(self):

        localctx = D95Parser.Foreach_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_foreach_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(D95Parser.FOREACH)
            self.state = 185
            self.match(D95Parser.LP)
            self.state = 186
            self.fe_id()
            self.state = 187
            self.match(D95Parser.AS)
            self.state = 188
            self.fe_id()
            self.state = 189
            self.match(D95Parser.ASSO)
            self.state = 190
            self.fe_id()
            self.state = 191
            self.match(D95Parser.RP)
            self.state = 192
            self.match(D95Parser.LCB)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.RETURN) | (1 << D95Parser.BREAK) | (1 << D95Parser.CONTINUE) | (1 << D95Parser.IF) | (1 << D95Parser.WHILE) | (1 << D95Parser.FOREACH) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0):
                self.state = 193
                self.stmt()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(D95Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(D95Parser.WHILE, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LCB(self):
            return self.getToken(D95Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D95Parser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D95Parser.StmtContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = D95Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(D95Parser.WHILE)
            self.state = 202
            self.match(D95Parser.LP)
            self.state = 203
            self.exp()
            self.state = 204
            self.match(D95Parser.RP)
            self.state = 205
            self.match(D95Parser.LCB)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.RETURN) | (1 << D95Parser.BREAK) | (1 << D95Parser.CONTINUE) | (1 << D95Parser.IF) | (1 << D95Parser.WHILE) | (1 << D95Parser.FOREACH) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0):
                self.state = 206
                self.stmt()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(D95Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D95Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D95Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(D95Parser.BREAK)
            self.state = 215
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D95Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D95Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(D95Parser.CONTINUE)
            self.state = 218
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_NAME(self):
            return self.getToken(D95Parser.FUNCTION_NAME, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def func_params(self):
            return self.getTypedRuleContext(D95Parser.Func_paramsContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = D95Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(D95Parser.FUNCTION_NAME)
            self.state = 221
            self.match(D95Parser.LP)
            self.state = 222
            self.func_params()
            self.state = 223
            self.match(D95Parser.RP)
            self.state = 224
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D95Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D95Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(D95Parser.RETURN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.ARRAY) | (1 << D95Parser.MINUS) | (1 << D95Parser.NOT) | (1 << D95Parser.LP) | (1 << D95Parser.INTLIT) | (1 << D95Parser.FLOATLIT) | (1 << D95Parser.BOOLEAN) | (1 << D95Parser.STRINGLIT) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0):
                self.state = 227
                self.exp()


            self.state = 230
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D95Parser.Exp1Context,i)


        def ASSO(self):
            return self.getToken(D95Parser.ASSO, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D95Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.exp1()
                self.state = 233
                self.match(D95Parser.ASSO)
                self.state = 234
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D95Parser.Exp2Context,i)


        def CONCATSTR(self):
            return self.getToken(D95Parser.CONCATSTR, 0)

        def COMPSTR(self):
            return self.getToken(D95Parser.COMPSTR, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = D95Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.exp2()
                self.state = 240
                _la = self._input.LA(1)
                if not(_la==D95Parser.CONCATSTR or _la==D95Parser.COMPSTR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 241
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Exp3Context)
            else:
                return self.getTypedRuleContext(D95Parser.Exp3Context,i)


        def EQ(self):
            return self.getToken(D95Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(D95Parser.NEQ, 0)

        def GT(self):
            return self.getToken(D95Parser.GT, 0)

        def LT(self):
            return self.getToken(D95Parser.LT, 0)

        def GTE(self):
            return self.getToken(D95Parser.GTE, 0)

        def LTE(self):
            return self.getToken(D95Parser.LTE, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = D95Parser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.exp3(0)
                self.state = 247
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.EQ) | (1 << D95Parser.NEQ) | (1 << D95Parser.GT) | (1 << D95Parser.LT) | (1 << D95Parser.GTE) | (1 << D95Parser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.exp3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D95Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D95Parser.Exp3Context,0)


        def AND(self):
            return self.getToken(D95Parser.AND, 0)

        def OR(self):
            return self.getToken(D95Parser.OR, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D95Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D95Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    _la = self._input.LA(1)
                    if not(_la==D95Parser.AND or _la==D95Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.exp4(0) 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D95Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D95Parser.Exp4Context,0)


        def ADD(self):
            return self.getToken(D95Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(D95Parser.MINUS, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D95Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D95Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    _la = self._input.LA(1)
                    if not(_la==D95Parser.ADD or _la==D95Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 269
                    self.exp5(0) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(D95Parser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(D95Parser.Exp5Context,0)


        def MUL(self):
            return self.getToken(D95Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D95Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D95Parser.MOD, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D95Parser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D95Parser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.MUL) | (1 << D95Parser.DIV) | (1 << D95Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 280
                    self.exp6() 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D95Parser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(D95Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D95Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D95Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D95Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp6)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(D95Parser.NOT)
                self.state = 287
                self.exp6()
                pass
            elif token in [D95Parser.ARRAY, D95Parser.MINUS, D95Parser.LP, D95Parser.INTLIT, D95Parser.FLOATLIT, D95Parser.BOOLEAN, D95Parser.STRINGLIT, D95Parser.VAR_NAME, D95Parser.FUNCTION_NAME, D95Parser.CONSTANT_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D95Parser.MINUS, 0)

        def exp7(self):
            return self.getTypedRuleContext(D95Parser.Exp7Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D95Parser.Exp8Context,0)


        def getRuleIndex(self):
            return D95Parser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = D95Parser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp7)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(D95Parser.MINUS)
                self.state = 292
                self.exp7()
                pass
            elif token in [D95Parser.ARRAY, D95Parser.LP, D95Parser.INTLIT, D95Parser.FLOATLIT, D95Parser.BOOLEAN, D95Parser.STRINGLIT, D95Parser.VAR_NAME, D95Parser.FUNCTION_NAME, D95Parser.CONSTANT_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.exp8(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D95Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D95Parser.Exp8Context,0)


        def index_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Index_expContext)
            else:
                return self.getTypedRuleContext(D95Parser.Index_expContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D95Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D95Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 301 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 300
                            self.index_exp()

                        else:
                            raise NoViableAltException(self)
                        self.state = 303 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
             
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D95Parser.Exp10Context,0)


        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def func_params(self):
            return self.getTypedRuleContext(D95Parser.Func_paramsContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = D95Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp9)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.exp10()
                self.state = 311
                self.match(D95Parser.LP)
                self.state = 312
                self.func_params()
                self.state = 313
                self.match(D95Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def operands(self):
            return self.getTypedRuleContext(D95Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D95Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp10)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(D95Parser.LP)
                self.state = 319
                self.exp()
                self.state = 320
                self.match(D95Parser.RP)
                pass
            elif token in [D95Parser.ARRAY, D95Parser.INTLIT, D95Parser.FLOATLIT, D95Parser.BOOLEAN, D95Parser.STRINGLIT, D95Parser.VAR_NAME, D95Parser.FUNCTION_NAME, D95Parser.CONSTANT_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D95Parser.IdentifierContext,0)


        def primitive_lit(self):
            return self.getTypedRuleContext(D95Parser.Primitive_litContext,0)


        def func_call(self):
            return self.getTypedRuleContext(D95Parser.Func_callContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(D95Parser.Array_litContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D95Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_operands)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.primitive_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.array_lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_NAME(self):
            return self.getToken(D95Parser.FUNCTION_NAME, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def func_params(self):
            return self.getTypedRuleContext(D95Parser.Func_paramsContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = D95Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(D95Parser.FUNCTION_NAME)
            self.state = 332
            self.match(D95Parser.LP)
            self.state = 333
            self.func_params()
            self.state = 334
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D95Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D95Parser.COMMA)
            else:
                return self.getToken(D95Parser.COMMA, i)

        def getRuleIndex(self):
            return D95Parser.RULE_func_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_params" ):
                return visitor.visitFunc_params(self)
            else:
                return visitor.visitChildren(self)




    def func_params(self):

        localctx = D95Parser.Func_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_params)
        self._la = 0 # Token type
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.ARRAY, D95Parser.MINUS, D95Parser.NOT, D95Parser.LP, D95Parser.INTLIT, D95Parser.FLOATLIT, D95Parser.BOOLEAN, D95Parser.STRINGLIT, D95Parser.VAR_NAME, D95Parser.FUNCTION_NAME, D95Parser.CONSTANT_NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.exp()
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D95Parser.COMMA:
                    self.state = 337
                    self.match(D95Parser.COMMA)
                    self.state = 338
                    self.exp()
                    self.state = 343
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D95Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D95Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D95Parser.RSB, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp" ):
                return visitor.visitIndex_exp(self)
            else:
                return visitor.visitChildren(self)




    def index_exp(self):

        localctx = D95Parser.Index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(D95Parser.LSB)
            self.state = 348
            self.exp()
            self.state = 349
            self.match(D95Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_oprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D95Parser.IdentifierContext,0)


        def index_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Index_expContext)
            else:
                return self.getTypedRuleContext(D95Parser.Index_expContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_index_opr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_opr" ):
                return visitor.visitIndex_opr(self)
            else:
                return visitor.visitChildren(self)




    def index_opr(self):

        localctx = D95Parser.Index_oprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_index_opr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.identifier()
            self.state = 353 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 352
                self.index_exp()
                self.state = 355 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D95Parser.LSB):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(D95Parser.VAR_NAME)
            else:
                return self.getToken(D95Parser.VAR_NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D95Parser.COMMA)
            else:
                return self.getToken(D95Parser.COMMA, i)

        def getRuleIndex(self):
            return D95Parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = D95Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.VAR_NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(D95Parser.VAR_NAME)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D95Parser.COMMA:
                    self.state = 358
                    self.match(D95Parser.COMMA)
                    self.state = 359
                    self.match(D95Parser.VAR_NAME)
                    self.state = 364
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D95Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D95Parser.StmtContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = D95Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 368
                self.stmt()
                self.state = 371 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.RETURN) | (1 << D95Parser.BREAK) | (1 << D95Parser.CONTINUE) | (1 << D95Parser.IF) | (1 << D95Parser.WHILE) | (1 << D95Parser.FOREACH) | (1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_lit(self):
            return self.getTypedRuleContext(D95Parser.Primitive_litContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(D95Parser.Array_litContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D95Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_literal)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.INTLIT, D95Parser.FLOATLIT, D95Parser.BOOLEAN, D95Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.primitive_lit()
                pass
            elif token in [D95Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(D95Parser.VAR_NAME, 0)

        def FUNCTION_NAME(self):
            return self.getToken(D95Parser.FUNCTION_NAME, 0)

        def CONSTANT_NAME(self):
            return self.getToken(D95Parser.CONSTANT_NAME, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = D95Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.VAR_NAME) | (1 << D95Parser.FUNCTION_NAME) | (1 << D95Parser.CONSTANT_NAME))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D95Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D95Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D95Parser.STRINGLIT, 0)

        def BOOLEAN(self):
            return self.getToken(D95Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_primitive_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_lit" ):
                return visitor.visitPrimitive_lit(self)
            else:
                return visitor.visitChildren(self)




    def primitive_lit(self):

        localctx = D95Parser.Primitive_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primitive_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.INTLIT) | (1 << D95Parser.FLOATLIT) | (1 << D95Parser.BOOLEAN) | (1 << D95Parser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_arr(self):
            return self.getTypedRuleContext(D95Parser.Index_arrContext,0)


        def asso_arr(self):
            return self.getTypedRuleContext(D95Parser.Asso_arrContext,0)


        def multidim_arr(self):
            return self.getTypedRuleContext(D95Parser.Multidim_arrContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = D95Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_array_lit)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.index_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.asso_arr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.multidim_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D95Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def index_arr_body(self):
            return self.getTypedRuleContext(D95Parser.Index_arr_bodyContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_index_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr" ):
                return visitor.visitIndex_arr(self)
            else:
                return visitor.visitChildren(self)




    def index_arr(self):

        localctx = D95Parser.Index_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_index_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(D95Parser.ARRAY)
            self.state = 387
            self.match(D95Parser.LP)
            self.state = 388
            self.index_arr_body()
            self.state = 389
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_arr_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Primitive_litContext)
            else:
                return self.getTypedRuleContext(D95Parser.Primitive_litContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D95Parser.COMMA)
            else:
                return self.getToken(D95Parser.COMMA, i)

        def getRuleIndex(self):
            return D95Parser.RULE_index_arr_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr_body" ):
                return visitor.visitIndex_arr_body(self)
            else:
                return visitor.visitChildren(self)




    def index_arr_body(self):

        localctx = D95Parser.Index_arr_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index_arr_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.primitive_lit()
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D95Parser.COMMA:
                self.state = 392
                self.match(D95Parser.COMMA)
                self.state = 393
                self.primitive_lit()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asso_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D95Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def asso_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Asso_eleContext)
            else:
                return self.getTypedRuleContext(D95Parser.Asso_eleContext,i)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D95Parser.COMMA)
            else:
                return self.getToken(D95Parser.COMMA, i)

        def getRuleIndex(self):
            return D95Parser.RULE_asso_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsso_arr" ):
                return visitor.visitAsso_arr(self)
            else:
                return visitor.visitChildren(self)




    def asso_arr(self):

        localctx = D95Parser.Asso_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_asso_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(D95Parser.ARRAY)
            self.state = 400
            self.match(D95Parser.LP)
            self.state = 401
            self.asso_ele()
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D95Parser.COMMA:
                self.state = 402
                self.match(D95Parser.COMMA)
                self.state = 403
                self.asso_ele()
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 409
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asso_eleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asso_key(self):
            return self.getTypedRuleContext(D95Parser.Asso_keyContext,0)


        def ASSO(self):
            return self.getToken(D95Parser.ASSO, 0)

        def exp(self):
            return self.getTypedRuleContext(D95Parser.ExpContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_asso_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsso_ele" ):
                return visitor.visitAsso_ele(self)
            else:
                return visitor.visitChildren(self)




    def asso_ele(self):

        localctx = D95Parser.Asso_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_asso_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.asso_key()
            self.state = 412
            self.match(D95Parser.ASSO)
            self.state = 413
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multidim_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D95Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def multidim_arr_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Multidim_arr_eleContext)
            else:
                return self.getTypedRuleContext(D95Parser.Multidim_arr_eleContext,i)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D95Parser.COMMA)
            else:
                return self.getToken(D95Parser.COMMA, i)

        def getRuleIndex(self):
            return D95Parser.RULE_multidim_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultidim_arr" ):
                return visitor.visitMultidim_arr(self)
            else:
                return visitor.visitChildren(self)




    def multidim_arr(self):

        localctx = D95Parser.Multidim_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_multidim_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(D95Parser.ARRAY)
            self.state = 416
            self.match(D95Parser.LP)
            self.state = 417
            self.multidim_arr_ele()
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D95Parser.COMMA:
                self.state = 418
                self.match(D95Parser.COMMA)
                self.state = 419
                self.multidim_arr_ele()
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 425
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multidim_arr_eleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_arr(self):
            return self.getTypedRuleContext(D95Parser.Index_arrContext,0)


        def asso_arr(self):
            return self.getTypedRuleContext(D95Parser.Asso_arrContext,0)


        def multidim_arr(self):
            return self.getTypedRuleContext(D95Parser.Multidim_arrContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_multidim_arr_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultidim_arr_ele" ):
                return visitor.visitMultidim_arr_ele(self)
            else:
                return visitor.visitChildren(self)




    def multidim_arr_ele(self):

        localctx = D95Parser.Multidim_arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_multidim_arr_ele)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.index_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.asso_arr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.multidim_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asso_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D95Parser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D95Parser.STRINGLIT, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_asso_key

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsso_key" ):
                return visitor.visitAsso_key(self)
            else:
                return visitor.visitChildren(self)




    def asso_key(self):

        localctx = D95Parser.Asso_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_asso_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            _la = self._input.LA(1)
            if not(_la==D95Parser.INTLIT or _la==D95Parser.STRINGLIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fe_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(D95Parser.VAR_NAME, 0)

        def CONSTANT_NAME(self):
            return self.getToken(D95Parser.CONSTANT_NAME, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_fe_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFe_id" ):
                return visitor.visitFe_id(self)
            else:
                return visitor.visitChildren(self)




    def fe_id(self):

        localctx = D95Parser.Fe_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_fe_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            _la = self._input.LA(1)
            if not(_la==D95Parser.VAR_NAME or _la==D95Parser.CONSTANT_NAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.exp3_sempred
        self._predicates[20] = self.exp4_sempred
        self._predicates[21] = self.exp5_sempred
        self._predicates[24] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




