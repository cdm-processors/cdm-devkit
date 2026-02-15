# Generated from assembler/grammar/AsmParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from base64 import b64decode

def serializedATN():
    return [
        4,1,43,423,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,5,0,90,8,0,10,0,12,0,
        93,9,0,1,0,5,0,96,8,0,10,0,12,0,99,9,0,1,0,5,0,102,8,0,10,0,12,0,
        105,9,0,1,0,1,0,1,1,5,1,110,8,1,10,1,12,1,113,9,1,1,1,4,1,116,8,
        1,11,1,12,1,117,1,1,5,1,121,8,1,10,1,12,1,124,9,1,1,1,5,1,127,8,
        1,10,1,12,1,130,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,143,8,2,1,3,1,3,1,4,1,4,1,4,1,4,5,4,151,8,4,10,4,12,4,154,9,
        4,3,4,156,8,4,1,4,1,4,1,5,1,5,3,5,162,8,5,1,5,1,5,4,5,166,8,5,11,
        5,12,5,167,1,6,1,6,3,6,172,8,6,1,6,1,6,4,6,176,8,6,11,6,12,6,177,
        1,7,1,7,1,7,4,7,183,8,7,11,7,12,7,184,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,5,9,196,8,9,10,9,12,9,199,9,9,1,10,1,10,1,10,1,10,3,10,
        205,8,10,1,10,4,10,208,8,10,11,10,12,10,209,1,10,1,10,1,10,1,10,
        1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,4,13,224,8,13,11,13,12,13,
        225,1,14,1,14,4,14,230,8,14,11,14,12,14,231,1,15,1,15,1,16,1,16,
        3,16,238,8,16,1,16,4,16,241,8,16,11,16,12,16,242,1,16,3,16,246,8,
        16,1,16,1,16,3,16,250,8,16,1,16,4,16,253,8,16,11,16,12,16,254,3,
        16,257,8,16,1,17,1,17,1,17,1,18,1,18,1,18,5,18,265,8,18,10,18,12,
        18,268,9,18,1,19,1,19,1,19,5,19,273,8,19,10,19,12,19,276,9,19,1,
        20,1,20,4,20,280,8,20,11,20,12,20,281,1,20,1,20,1,20,3,20,287,8,
        20,1,20,1,20,4,20,291,8,20,11,20,12,20,292,1,21,5,21,296,8,21,10,
        21,12,21,299,9,21,1,21,1,21,4,21,303,8,21,11,21,12,21,304,1,21,1,
        21,4,21,309,8,21,11,21,12,21,310,3,21,313,8,21,1,22,1,22,1,22,1,
        22,4,22,319,8,22,11,22,12,22,320,1,23,1,23,1,23,1,23,1,24,1,24,4,
        24,329,8,24,11,24,12,24,330,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,
        27,4,27,341,8,27,11,27,12,27,342,1,27,1,27,1,27,1,27,4,27,349,8,
        27,11,27,12,27,350,1,27,1,27,1,27,4,27,356,8,27,11,27,12,27,357,
        1,28,1,28,1,29,1,29,4,29,364,8,29,11,29,12,29,365,1,29,1,29,1,29,
        1,29,4,29,372,8,29,11,29,12,29,373,1,30,1,30,1,30,1,30,1,30,3,30,
        381,8,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,5,32,390,8,32,10,32,
        12,32,393,9,32,1,33,3,33,396,8,33,1,33,1,33,1,34,1,34,1,34,1,35,
        1,35,3,35,405,8,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,40,
        1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,43,0,0,44,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,0,4,2,0,23,23,25,25,1,
        0,21,22,1,0,34,36,2,0,1,18,32,33,434,0,91,1,0,0,0,2,111,1,0,0,0,
        4,142,1,0,0,0,6,144,1,0,0,0,8,146,1,0,0,0,10,159,1,0,0,0,12,169,
        1,0,0,0,14,179,1,0,0,0,16,186,1,0,0,0,18,197,1,0,0,0,20,200,1,0,
        0,0,22,217,1,0,0,0,24,219,1,0,0,0,26,221,1,0,0,0,28,227,1,0,0,0,
        30,233,1,0,0,0,32,256,1,0,0,0,34,258,1,0,0,0,36,261,1,0,0,0,38,269,
        1,0,0,0,40,277,1,0,0,0,42,297,1,0,0,0,44,314,1,0,0,0,46,322,1,0,
        0,0,48,326,1,0,0,0,50,334,1,0,0,0,52,336,1,0,0,0,54,338,1,0,0,0,
        56,359,1,0,0,0,58,361,1,0,0,0,60,380,1,0,0,0,62,382,1,0,0,0,64,387,
        1,0,0,0,66,395,1,0,0,0,68,399,1,0,0,0,70,404,1,0,0,0,72,406,1,0,
        0,0,74,408,1,0,0,0,76,410,1,0,0,0,78,412,1,0,0,0,80,414,1,0,0,0,
        82,416,1,0,0,0,84,418,1,0,0,0,86,420,1,0,0,0,88,90,5,39,0,0,89,88,
        1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,97,1,0,0,0,
        93,91,1,0,0,0,94,96,3,30,15,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,
        1,0,0,0,97,98,1,0,0,0,98,103,1,0,0,0,99,97,1,0,0,0,100,102,3,4,2,
        0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,
        0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,6,0,0,107,1,1,0,0,0,
        108,110,5,39,0,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,
        111,112,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,114,116,3,20,10,
        0,115,114,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,
        0,118,122,1,0,0,0,119,121,3,30,15,0,120,119,1,0,0,0,121,124,1,0,
        0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,128,1,0,0,0,124,122,1,0,
        0,0,125,127,3,4,2,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,
        0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,5,6,
        0,0,132,3,1,0,0,0,133,134,3,10,5,0,134,135,3,16,8,0,135,143,1,0,
        0,0,136,137,3,12,6,0,137,138,3,16,8,0,138,143,1,0,0,0,139,140,3,
        14,7,0,140,141,3,16,8,0,141,143,1,0,0,0,142,133,1,0,0,0,142,136,
        1,0,0,0,142,139,1,0,0,0,143,5,1,0,0,0,144,145,5,32,0,0,145,7,1,0,
        0,0,146,155,5,29,0,0,147,152,3,6,3,0,148,149,5,20,0,0,149,151,3,
        6,3,0,150,148,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,
        0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,155,147,1,0,0,0,155,156,1,
        0,0,0,156,157,1,0,0,0,157,158,5,30,0,0,158,9,1,0,0,0,159,161,5,1,
        0,0,160,162,3,8,4,0,161,160,1,0,0,0,161,162,1,0,0,0,162,163,1,0,
        0,0,163,165,3,84,42,0,164,166,5,39,0,0,165,164,1,0,0,0,166,167,1,
        0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,11,1,0,0,0,169,171,5,12,
        0,0,170,172,3,8,4,0,171,170,1,0,0,0,171,172,1,0,0,0,172,173,1,0,
        0,0,173,175,3,86,43,0,174,176,5,39,0,0,175,174,1,0,0,0,176,177,1,
        0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,13,1,0,0,0,179,180,5,15,
        0,0,180,182,3,86,43,0,181,183,5,39,0,0,182,181,1,0,0,0,183,184,1,
        0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,15,1,0,0,0,186,187,3,18,
        9,0,187,17,1,0,0,0,188,196,3,26,13,0,189,196,3,28,14,0,190,196,3,
        32,16,0,191,196,3,40,20,0,192,196,3,54,27,0,193,196,3,58,29,0,194,
        196,3,20,10,0,195,188,1,0,0,0,195,189,1,0,0,0,195,190,1,0,0,0,195,
        191,1,0,0,0,195,192,1,0,0,0,195,193,1,0,0,0,195,194,1,0,0,0,196,
        199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,19,1,0,0,0,199,197,
        1,0,0,0,200,201,5,28,0,0,201,202,3,22,11,0,202,204,3,24,12,0,203,
        205,5,32,0,0,204,203,1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,
        208,5,39,0,0,207,206,1,0,0,0,208,209,1,0,0,0,209,207,1,0,0,0,209,
        210,1,0,0,0,210,211,1,0,0,0,211,212,6,10,-1,0,212,213,6,10,-1,0,
        213,214,6,10,-1,0,214,215,6,10,-1,0,215,216,6,10,-1,0,216,21,1,0,
        0,0,217,218,5,34,0,0,218,23,1,0,0,0,219,220,5,42,0,0,220,25,1,0,
        0,0,221,223,5,2,0,0,222,224,5,39,0,0,223,222,1,0,0,0,224,225,1,0,
        0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,27,1,0,0,0,227,229,5,3,0,
        0,228,230,5,39,0,0,229,228,1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,
        0,231,232,1,0,0,0,232,29,1,0,0,0,233,234,3,32,16,0,234,31,1,0,0,
        0,235,237,3,34,17,0,236,238,5,7,0,0,237,236,1,0,0,0,237,238,1,0,
        0,0,238,240,1,0,0,0,239,241,5,39,0,0,240,239,1,0,0,0,241,242,1,0,
        0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,257,1,0,0,0,244,246,3,34,
        17,0,245,244,1,0,0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,249,3,76,
        38,0,248,250,3,38,19,0,249,248,1,0,0,0,249,250,1,0,0,0,250,252,1,
        0,0,0,251,253,5,39,0,0,252,251,1,0,0,0,253,254,1,0,0,0,254,252,1,
        0,0,0,254,255,1,0,0,0,255,257,1,0,0,0,256,235,1,0,0,0,256,245,1,
        0,0,0,257,33,1,0,0,0,258,259,3,36,18,0,259,260,7,0,0,0,260,35,1,
        0,0,0,261,266,3,74,37,0,262,263,5,20,0,0,263,265,3,74,37,0,264,262,
        1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,37,1,
        0,0,0,268,266,1,0,0,0,269,274,3,60,30,0,270,271,5,20,0,0,271,273,
        3,60,30,0,272,270,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,
        1,0,0,0,275,39,1,0,0,0,276,274,1,0,0,0,277,279,5,9,0,0,278,280,5,
        39,0,0,279,278,1,0,0,0,280,281,1,0,0,0,281,279,1,0,0,0,281,282,1,
        0,0,0,282,283,1,0,0,0,283,284,3,42,21,0,284,286,3,18,9,0,285,287,
        3,48,24,0,286,285,1,0,0,0,286,287,1,0,0,0,287,288,1,0,0,0,288,290,
        5,8,0,0,289,291,5,39,0,0,290,289,1,0,0,0,291,292,1,0,0,0,292,290,
        1,0,0,0,292,293,1,0,0,0,293,41,1,0,0,0,294,296,3,44,22,0,295,294,
        1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,300,
        1,0,0,0,299,297,1,0,0,0,300,302,3,46,23,0,301,303,5,39,0,0,302,301,
        1,0,0,0,303,304,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,312,
        1,0,0,0,306,308,5,14,0,0,307,309,5,39,0,0,308,307,1,0,0,0,309,310,
        1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,313,1,0,0,0,312,306,
        1,0,0,0,312,313,1,0,0,0,313,43,1,0,0,0,314,315,3,46,23,0,315,316,
        5,20,0,0,316,318,3,52,26,0,317,319,5,39,0,0,318,317,1,0,0,0,319,
        320,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,45,1,0,0,0,322,323,
        3,18,9,0,323,324,5,10,0,0,324,325,3,50,25,0,325,47,1,0,0,0,326,328,
        5,5,0,0,327,329,5,39,0,0,328,327,1,0,0,0,329,330,1,0,0,0,330,328,
        1,0,0,0,330,331,1,0,0,0,331,332,1,0,0,0,332,333,3,18,9,0,333,49,
        1,0,0,0,334,335,5,32,0,0,335,51,1,0,0,0,336,337,5,32,0,0,337,53,
        1,0,0,0,338,340,5,18,0,0,339,341,5,39,0,0,340,339,1,0,0,0,341,342,
        1,0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,344,1,0,0,0,344,345,
        3,56,28,0,345,346,5,13,0,0,346,348,3,50,25,0,347,349,5,39,0,0,348,
        347,1,0,0,0,349,350,1,0,0,0,350,348,1,0,0,0,350,351,1,0,0,0,351,
        352,1,0,0,0,352,353,3,18,9,0,353,355,5,17,0,0,354,356,5,39,0,0,355,
        354,1,0,0,0,356,357,1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,
        55,1,0,0,0,359,360,3,18,9,0,360,57,1,0,0,0,361,363,5,4,0,0,362,364,
        5,39,0,0,363,362,1,0,0,0,364,365,1,0,0,0,365,363,1,0,0,0,365,366,
        1,0,0,0,366,367,1,0,0,0,367,368,3,18,9,0,368,369,5,16,0,0,369,371,
        3,50,25,0,370,372,5,39,0,0,371,370,1,0,0,0,372,373,1,0,0,0,373,371,
        1,0,0,0,373,374,1,0,0,0,374,59,1,0,0,0,375,381,3,82,41,0,376,381,
        3,78,39,0,377,381,3,80,40,0,378,381,3,64,32,0,379,381,3,62,31,0,
        380,375,1,0,0,0,380,376,1,0,0,0,380,377,1,0,0,0,380,378,1,0,0,0,
        380,379,1,0,0,0,381,61,1,0,0,0,382,383,3,72,36,0,383,384,5,26,0,
        0,384,385,3,64,32,0,385,386,5,27,0,0,386,63,1,0,0,0,387,391,3,66,
        33,0,388,390,3,68,34,0,389,388,1,0,0,0,390,393,1,0,0,0,391,389,1,
        0,0,0,391,392,1,0,0,0,392,65,1,0,0,0,393,391,1,0,0,0,394,396,7,1,
        0,0,395,394,1,0,0,0,395,396,1,0,0,0,396,397,1,0,0,0,397,398,3,70,
        35,0,398,67,1,0,0,0,399,400,7,1,0,0,400,401,3,70,35,0,401,69,1,0,
        0,0,402,405,3,84,42,0,403,405,3,74,37,0,404,402,1,0,0,0,404,403,
        1,0,0,0,405,71,1,0,0,0,406,407,3,86,43,0,407,73,1,0,0,0,408,409,
        3,86,43,0,409,75,1,0,0,0,410,411,5,32,0,0,411,77,1,0,0,0,412,413,
        5,37,0,0,413,79,1,0,0,0,414,415,5,31,0,0,415,81,1,0,0,0,416,417,
        5,38,0,0,417,83,1,0,0,0,418,419,7,2,0,0,419,85,1,0,0,0,420,421,7,
        3,0,0,421,87,1,0,0,0,47,91,97,103,111,117,122,128,142,152,155,161,
        167,171,177,184,195,197,204,209,225,231,237,242,245,249,254,256,
        266,274,281,286,292,297,304,310,312,320,330,342,350,357,365,373,
        380,391,395,404
    ]

class AsmParser ( Parser ):

    grammarFileName = "AsmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'asect'", "'break'", "'continue'", "'do'", 
                     "'else'", "'end'", "'ext'", "'fi'", "'if'", "'is'", 
                     "'macro'", "'rsect'", "'stays'", "'then'", "'tplate'", 
                     "'until'", "'wend'", "'while'", "'.'", "','", "'+'", 
                     "'-'", "':'", "'*'", "'>'", "'('", "')'", "'-|'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Do", "Else", 
                      "End", "Ext", "Fi", "If", "Is", "Macro", "Rsect", 
                      "Stays", "Then", "Tplate", "Until", "Wend", "While", 
                      "DOT", "COMMA", "PLUS", "MINUS", "COLON", "ASTERISK", 
                      "ANGLE_BRACKET", "OPEN_PAREN", "CLOSE_PAREN", "LINE_MARK_MARKER", 
                      "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", "REGISTER", 
                      "WORD", "WORD_WITH_DOTS", "DECIMAL_NUMBER", "BINARY_NUMBER", 
                      "HEX_NUMBER", "STRING", "CHAR", "NEWLINE", "COMMENT", 
                      "WS", "BASE64", "UNEXPECTED_TOKEN" ]

    RULE_program_nomacros = 0
    RULE_program = 1
    RULE_section = 2
    RULE_section_attr = 3
    RULE_section_attrs = 4
    RULE_asect_header = 5
    RULE_rsect_header = 6
    RULE_tplate_header = 7
    RULE_section_body = 8
    RULE_code_block = 9
    RULE_line_mark = 10
    RULE_line_number = 11
    RULE_filepath = 12
    RULE_break_statement = 13
    RULE_continue_statement = 14
    RULE_top_line = 15
    RULE_line = 16
    RULE_labels_declaration = 17
    RULE_labels = 18
    RULE_arguments = 19
    RULE_conditional = 20
    RULE_conditions = 21
    RULE_connective_condition = 22
    RULE_condition = 23
    RULE_else_clause = 24
    RULE_branch_mnemonic = 25
    RULE_conjunction = 26
    RULE_while_loop = 27
    RULE_while_condition = 28
    RULE_until_loop = 29
    RULE_argument = 30
    RULE_byte_expr = 31
    RULE_addr_expr = 32
    RULE_first_term = 33
    RULE_add_term = 34
    RULE_term = 35
    RULE_byte_specifier = 36
    RULE_label = 37
    RULE_instruction = 38
    RULE_string = 39
    RULE_register = 40
    RULE_character = 41
    RULE_number = 42
    RULE_name = 43

    ruleNames =  [ "program_nomacros", "program", "section", "section_attr", 
                   "section_attrs", "asect_header", "rsect_header", "tplate_header", 
                   "section_body", "code_block", "line_mark", "line_number", 
                   "filepath", "break_statement", "continue_statement", 
                   "top_line", "line", "labels_declaration", "labels", "arguments", 
                   "conditional", "conditions", "connective_condition", 
                   "condition", "else_clause", "branch_mnemonic", "conjunction", 
                   "while_loop", "while_condition", "until_loop", "argument", 
                   "byte_expr", "addr_expr", "first_term", "add_term", "term", 
                   "byte_specifier", "label", "instruction", "string", "register", 
                   "character", "number", "name" ]

    EOF = Token.EOF
    Asect=1
    Break=2
    Continue=3
    Do=4
    Else=5
    End=6
    Ext=7
    Fi=8
    If=9
    Is=10
    Macro=11
    Rsect=12
    Stays=13
    Then=14
    Tplate=15
    Until=16
    Wend=17
    While=18
    DOT=19
    COMMA=20
    PLUS=21
    MINUS=22
    COLON=23
    ASTERISK=24
    ANGLE_BRACKET=25
    OPEN_PAREN=26
    CLOSE_PAREN=27
    LINE_MARK_MARKER=28
    OPEN_SQUARE_BRACKET=29
    CLOSE_SQUARE_BRACKET=30
    REGISTER=31
    WORD=32
    WORD_WITH_DOTS=33
    DECIMAL_NUMBER=34
    BINARY_NUMBER=35
    HEX_NUMBER=36
    STRING=37
    CHAR=38
    NEWLINE=39
    COMMENT=40
    WS=41
    BASE64=42
    UNEXPECTED_TOKEN=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.current_file = ''
        self.current_line = 0
        self.current_offset = 0



    class Program_nomacrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def End(self):
            return self.getToken(AsmParser.End, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def top_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Top_lineContext)
            else:
                return self.getTypedRuleContext(AsmParser.Top_lineContext,i)


        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.SectionContext)
            else:
                return self.getTypedRuleContext(AsmParser.SectionContext,i)


        def getRuleIndex(self):
            return AsmParser.RULE_program_nomacros

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_nomacros" ):
                return visitor.visitProgram_nomacros(self)
            else:
                return visitor.visitChildren(self)




    def program_nomacros(self):

        localctx = AsmParser.Program_nomacrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program_nomacros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 88
                self.match(AsmParser.NEWLINE)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.top_line() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36866) != 0):
                self.state = 100
                self.section()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(AsmParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def End(self):
            return self.getToken(AsmParser.End, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def line_mark(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Line_markContext)
            else:
                return self.getTypedRuleContext(AsmParser.Line_markContext,i)


        def top_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Top_lineContext)
            else:
                return self.getTypedRuleContext(AsmParser.Top_lineContext,i)


        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.SectionContext)
            else:
                return self.getTypedRuleContext(AsmParser.SectionContext,i)


        def getRuleIndex(self):
            return AsmParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AsmParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 108
                self.match(AsmParser.NEWLINE)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.line_mark()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
                    break

            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    self.top_line() 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36866) != 0):
                self.state = 125
                self.section()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(AsmParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsmParser.RULE_section

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AbsoluteSectionContext(SectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.SectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asect_header(self):
            return self.getTypedRuleContext(AsmParser.Asect_headerContext,0)

        def section_body(self):
            return self.getTypedRuleContext(AsmParser.Section_bodyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbsoluteSection" ):
                return visitor.visitAbsoluteSection(self)
            else:
                return visitor.visitChildren(self)


    class TemplateSectionContext(SectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.SectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tplate_header(self):
            return self.getTypedRuleContext(AsmParser.Tplate_headerContext,0)

        def section_body(self):
            return self.getTypedRuleContext(AsmParser.Section_bodyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateSection" ):
                return visitor.visitTemplateSection(self)
            else:
                return visitor.visitChildren(self)


    class RelocatableSectionContext(SectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.SectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rsect_header(self):
            return self.getTypedRuleContext(AsmParser.Rsect_headerContext,0)

        def section_body(self):
            return self.getTypedRuleContext(AsmParser.Section_bodyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelocatableSection" ):
                return visitor.visitRelocatableSection(self)
            else:
                return visitor.visitChildren(self)



    def section(self):

        localctx = AsmParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_section)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.asect_header()
                self.state = 134
                self.section_body()
                pass
            elif token in [12]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.rsect_header()
                self.state = 137
                self.section_body()
                pass
            elif token in [15]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.tplate_header()
                self.state = 140
                self.section_body()
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


    class Section_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_section_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection_attr" ):
                return visitor.visitSection_attr(self)
            else:
                return visitor.visitChildren(self)




    def section_attr(self):

        localctx = AsmParser.Section_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_section_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(AsmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_attrsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(AsmParser.OPEN_SQUARE_BRACKET, 0)

        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(AsmParser.CLOSE_SQUARE_BRACKET, 0)

        def section_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Section_attrContext)
            else:
                return self.getTypedRuleContext(AsmParser.Section_attrContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.COMMA)
            else:
                return self.getToken(AsmParser.COMMA, i)

        def getRuleIndex(self):
            return AsmParser.RULE_section_attrs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection_attrs" ):
                return visitor.visitSection_attrs(self)
            else:
                return visitor.visitChildren(self)




    def section_attrs(self):

        localctx = AsmParser.Section_attrsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_section_attrs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(AsmParser.OPEN_SQUARE_BRACKET)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 147
                self.section_attr()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 148
                    self.match(AsmParser.COMMA)
                    self.state = 149
                    self.section_attr()
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 157
            self.match(AsmParser.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asect_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asect(self):
            return self.getToken(AsmParser.Asect, 0)

        def number(self):
            return self.getTypedRuleContext(AsmParser.NumberContext,0)


        def section_attrs(self):
            return self.getTypedRuleContext(AsmParser.Section_attrsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_asect_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsect_header" ):
                return visitor.visitAsect_header(self)
            else:
                return visitor.visitChildren(self)




    def asect_header(self):

        localctx = AsmParser.Asect_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(AsmParser.Asect)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 160
                self.section_attrs()


            self.state = 163
            self.number()
            self.state = 165 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 164
                self.match(AsmParser.NEWLINE)
                self.state = 167 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rsect_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Rsect(self):
            return self.getToken(AsmParser.Rsect, 0)

        def name(self):
            return self.getTypedRuleContext(AsmParser.NameContext,0)


        def section_attrs(self):
            return self.getTypedRuleContext(AsmParser.Section_attrsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_rsect_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRsect_header" ):
                return visitor.visitRsect_header(self)
            else:
                return visitor.visitChildren(self)




    def rsect_header(self):

        localctx = AsmParser.Rsect_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rsect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(AsmParser.Rsect)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 170
                self.section_attrs()


            self.state = 173
            self.name()
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self.match(AsmParser.NEWLINE)
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tplate_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Tplate(self):
            return self.getToken(AsmParser.Tplate, 0)

        def name(self):
            return self.getTypedRuleContext(AsmParser.NameContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_tplate_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTplate_header" ):
                return visitor.visitTplate_header(self)
            else:
                return visitor.visitChildren(self)




    def tplate_header(self):

        localctx = AsmParser.Tplate_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tplate_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(AsmParser.Tplate)
            self.state = 180
            self.name()
            self.state = 182 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 181
                self.match(AsmParser.NEWLINE)
                self.state = 184 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_section_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection_body" ):
                return visitor.visitSection_body(self)
            else:
                return visitor.visitChildren(self)




    def section_body(self):

        localctx = AsmParser.Section_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_section_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def break_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Break_statementContext)
            else:
                return self.getTypedRuleContext(AsmParser.Break_statementContext,i)


        def continue_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Continue_statementContext)
            else:
                return self.getTypedRuleContext(AsmParser.Continue_statementContext,i)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.LineContext)
            else:
                return self.getTypedRuleContext(AsmParser.LineContext,i)


        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(AsmParser.ConditionalContext,i)


        def while_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.While_loopContext)
            else:
                return self.getTypedRuleContext(AsmParser.While_loopContext,i)


        def until_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Until_loopContext)
            else:
                return self.getTypedRuleContext(AsmParser.Until_loopContext,i)


        def line_mark(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Line_markContext)
            else:
                return self.getTypedRuleContext(AsmParser.Line_markContext,i)


        def getRuleIndex(self):
            return AsmParser.RULE_code_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = AsmParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        self.state = 188
                        self.break_statement()
                        pass

                    elif la_ == 2:
                        self.state = 189
                        self.continue_statement()
                        pass

                    elif la_ == 3:
                        self.state = 190
                        self.line()
                        pass

                    elif la_ == 4:
                        self.state = 191
                        self.conditional()
                        pass

                    elif la_ == 5:
                        self.state = 192
                        self.while_loop()
                        pass

                    elif la_ == 6:
                        self.state = 193
                        self.until_loop()
                        pass

                    elif la_ == 7:
                        self.state = 194
                        self.line_mark()
                        pass

             
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_markContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.source_file = ''
            self.source_line = 0
            self._line_number = None # Line_numberContext
            self._filepath = None # FilepathContext

        def LINE_MARK_MARKER(self):
            return self.getToken(AsmParser.LINE_MARK_MARKER, 0)

        def line_number(self):
            return self.getTypedRuleContext(AsmParser.Line_numberContext,0)


        def filepath(self):
            return self.getTypedRuleContext(AsmParser.FilepathContext,0)


        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_line_mark

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_mark" ):
                return visitor.visitLine_mark(self)
            else:
                return visitor.visitChildren(self)




    def line_mark(self):

        localctx = AsmParser.Line_markContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_line_mark)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 201
            localctx._line_number = self.line_number()
            self.state = 202
            localctx._filepath = self.filepath()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 203
                self.match(AsmParser.WORD)


            self.state = 207 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self.match(AsmParser.NEWLINE)
                self.state = 209 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.current_line = int((None if localctx._line_number is None else self._input.getText(localctx._line_number.start,localctx._line_number.stop)))
            self.current_file =  b64decode((None if localctx._filepath is None else self._input.getText(localctx._filepath.start,localctx._filepath.stop))[3:]).decode()
            localctx.source_file = self.current_file
            localctx.source_line = self.current_line
            self.current_offset = (None if localctx._line_number is None else localctx._line_number.start).line - self.current_line + 1
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_NUMBER(self):
            return self.getToken(AsmParser.DECIMAL_NUMBER, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_line_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_number" ):
                return visitor.visitLine_number(self)
            else:
                return visitor.visitChildren(self)




    def line_number(self):

        localctx = AsmParser.Line_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_line_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(AsmParser.DECIMAL_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilepathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BASE64(self):
            return self.getToken(AsmParser.BASE64, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_filepath

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilepath" ):
                return visitor.visitFilepath(self)
            else:
                return visitor.visitChildren(self)




    def filepath(self):

        localctx = AsmParser.FilepathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(AsmParser.BASE64)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(AsmParser.Break, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = AsmParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(AsmParser.Break)
            self.state = 223 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 222
                self.match(AsmParser.NEWLINE)
                self.state = 225 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(AsmParser.Continue, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = AsmParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(AsmParser.Continue)
            self.state = 229 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 228
                self.match(AsmParser.NEWLINE)
                self.state = 231 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Top_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self):
            return self.getTypedRuleContext(AsmParser.LineContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_top_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTop_line" ):
                return visitor.visitTop_line(self)
            else:
                return visitor.visitChildren(self)




    def top_line(self):

        localctx = AsmParser.Top_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_top_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsmParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstructionLineContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruction(self):
            return self.getTypedRuleContext(AsmParser.InstructionContext,0)

        def labels_declaration(self):
            return self.getTypedRuleContext(AsmParser.Labels_declarationContext,0)

        def arguments(self):
            return self.getTypedRuleContext(AsmParser.ArgumentsContext,0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionLine" ):
                return visitor.visitInstructionLine(self)
            else:
                return visitor.visitChildren(self)


    class StandaloneLabelsContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def labels_declaration(self):
            return self.getTypedRuleContext(AsmParser.Labels_declarationContext,0)

        def Ext(self):
            return self.getToken(AsmParser.Ext, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandaloneLabels" ):
                return visitor.visitStandaloneLabels(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = AsmParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = AsmParser.StandaloneLabelsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.labels_declaration()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 236
                    self.match(AsmParser.Ext)


                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 239
                    self.match(AsmParser.NEWLINE)
                    self.state = 242 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 2:
                localctx = AsmParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 244
                    self.labels_declaration()


                self.state = 247
                self.instruction()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 547615145982) != 0):
                    self.state = 248
                    self.arguments()


                self.state = 252 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 251
                    self.match(AsmParser.NEWLINE)
                    self.state = 254 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Labels_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labels(self):
            return self.getTypedRuleContext(AsmParser.LabelsContext,0)


        def COLON(self):
            return self.getToken(AsmParser.COLON, 0)

        def ANGLE_BRACKET(self):
            return self.getToken(AsmParser.ANGLE_BRACKET, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_labels_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabels_declaration" ):
                return visitor.visitLabels_declaration(self)
            else:
                return visitor.visitChildren(self)




    def labels_declaration(self):

        localctx = AsmParser.Labels_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_labels_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.labels()
            self.state = 259
            _la = self._input.LA(1)
            if not(_la==23 or _la==25):
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


    class LabelsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.LabelContext)
            else:
                return self.getTypedRuleContext(AsmParser.LabelContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.COMMA)
            else:
                return self.getToken(AsmParser.COMMA, i)

        def getRuleIndex(self):
            return AsmParser.RULE_labels

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabels" ):
                return visitor.visitLabels(self)
            else:
                return visitor.visitChildren(self)




    def labels(self):

        localctx = AsmParser.LabelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_labels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.label()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 262
                self.match(AsmParser.COMMA)
                self.state = 263
                self.label()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(AsmParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.COMMA)
            else:
                return self.getToken(AsmParser.COMMA, i)

        def getRuleIndex(self):
            return AsmParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = AsmParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.argument()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 270
                self.match(AsmParser.COMMA)
                self.state = 271
                self.argument()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(AsmParser.If, 0)

        def conditions(self):
            return self.getTypedRuleContext(AsmParser.ConditionsContext,0)


        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Fi(self):
            return self.getToken(AsmParser.Fi, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def else_clause(self):
            return self.getTypedRuleContext(AsmParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = AsmParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(AsmParser.If)
            self.state = 279 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.match(AsmParser.NEWLINE)
                self.state = 281 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 283
            self.conditions()
            self.state = 284
            self.code_block()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 285
                self.else_clause()


            self.state = 288
            self.match(AsmParser.Fi)
            self.state = 290 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 289
                self.match(AsmParser.NEWLINE)
                self.state = 292 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AsmParser.ConditionContext,0)


        def connective_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Connective_conditionContext)
            else:
                return self.getTypedRuleContext(AsmParser.Connective_conditionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def Then(self):
            return self.getToken(AsmParser.Then, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_conditions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditions" ):
                return visitor.visitConditions(self)
            else:
                return visitor.visitChildren(self)




    def conditions(self):

        localctx = AsmParser.ConditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 294
                    self.connective_condition() 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 300
            self.condition()
            self.state = 302 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 301
                self.match(AsmParser.NEWLINE)
                self.state = 304 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 306
                self.match(AsmParser.Then)
                self.state = 308 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 307
                    self.match(AsmParser.NEWLINE)
                    self.state = 310 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Connective_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AsmParser.ConditionContext,0)


        def COMMA(self):
            return self.getToken(AsmParser.COMMA, 0)

        def conjunction(self):
            return self.getTypedRuleContext(AsmParser.ConjunctionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_connective_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnective_condition" ):
                return visitor.visitConnective_condition(self)
            else:
                return visitor.visitChildren(self)




    def connective_condition(self):

        localctx = AsmParser.Connective_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_connective_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.condition()
            self.state = 315
            self.match(AsmParser.COMMA)
            self.state = 316
            self.conjunction()
            self.state = 318 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 317
                self.match(AsmParser.NEWLINE)
                self.state = 320 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Is(self):
            return self.getToken(AsmParser.Is, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = AsmParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.code_block()
            self.state = 323
            self.match(AsmParser.Is)
            self.state = 324
            self.branch_mnemonic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else(self):
            return self.getToken(AsmParser.Else, 0)

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_else_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = AsmParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(AsmParser.Else)
            self.state = 328 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 327
                self.match(AsmParser.NEWLINE)
                self.state = 330 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 332
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Branch_mnemonicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_branch_mnemonic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch_mnemonic" ):
                return visitor.visitBranch_mnemonic(self)
            else:
                return visitor.visitChildren(self)




    def branch_mnemonic(self):

        localctx = AsmParser.Branch_mnemonicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_branch_mnemonic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(AsmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_conjunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)




    def conjunction(self):

        localctx = AsmParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(AsmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(AsmParser.While, 0)

        def while_condition(self):
            return self.getTypedRuleContext(AsmParser.While_conditionContext,0)


        def Stays(self):
            return self.getToken(AsmParser.Stays, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Wend(self):
            return self.getToken(AsmParser.Wend, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_while_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = AsmParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(AsmParser.While)
            self.state = 340 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 339
                self.match(AsmParser.NEWLINE)
                self.state = 342 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 344
            self.while_condition()
            self.state = 345
            self.match(AsmParser.Stays)
            self.state = 346
            self.branch_mnemonic()
            self.state = 348 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 347
                self.match(AsmParser.NEWLINE)
                self.state = 350 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 352
            self.code_block()
            self.state = 353
            self.match(AsmParser.Wend)
            self.state = 355 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 354
                self.match(AsmParser.NEWLINE)
                self.state = 357 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_while_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_condition" ):
                return visitor.visitWhile_condition(self)
            else:
                return visitor.visitChildren(self)




    def while_condition(self):

        localctx = AsmParser.While_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_while_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Until_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Do(self):
            return self.getToken(AsmParser.Do, 0)

        def code_block(self):
            return self.getTypedRuleContext(AsmParser.Code_blockContext,0)


        def Until(self):
            return self.getToken(AsmParser.Until, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_until_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntil_loop" ):
                return visitor.visitUntil_loop(self)
            else:
                return visitor.visitChildren(self)




    def until_loop(self):

        localctx = AsmParser.Until_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_until_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(AsmParser.Do)
            self.state = 363 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 362
                self.match(AsmParser.NEWLINE)
                self.state = 365 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 367
            self.code_block()
            self.state = 368
            self.match(AsmParser.Until)
            self.state = 369
            self.branch_mnemonic()
            self.state = 371 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 370
                self.match(AsmParser.NEWLINE)
                self.state = 373 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def character(self):
            return self.getTypedRuleContext(AsmParser.CharacterContext,0)


        def string(self):
            return self.getTypedRuleContext(AsmParser.StringContext,0)


        def register(self):
            return self.getTypedRuleContext(AsmParser.RegisterContext,0)


        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


        def byte_expr(self):
            return self.getTypedRuleContext(AsmParser.Byte_exprContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = AsmParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_argument)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                self.byte_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Byte_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def byte_specifier(self):
            return self.getTypedRuleContext(AsmParser.Byte_specifierContext,0)


        def OPEN_PAREN(self):
            return self.getToken(AsmParser.OPEN_PAREN, 0)

        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(AsmParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_byte_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByte_expr" ):
                return visitor.visitByte_expr(self)
            else:
                return visitor.visitChildren(self)




    def byte_expr(self):

        localctx = AsmParser.Byte_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_byte_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.byte_specifier()
            self.state = 383
            self.match(AsmParser.OPEN_PAREN)
            self.state = 384
            self.addr_expr()
            self.state = 385
            self.match(AsmParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Addr_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def first_term(self):
            return self.getTypedRuleContext(AsmParser.First_termContext,0)


        def add_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Add_termContext)
            else:
                return self.getTypedRuleContext(AsmParser.Add_termContext,i)


        def getRuleIndex(self):
            return AsmParser.RULE_addr_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddr_expr" ):
                return visitor.visitAddr_expr(self)
            else:
                return visitor.visitChildren(self)




    def addr_expr(self):

        localctx = AsmParser.Addr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_addr_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.first_term()
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 388
                self.add_term()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class First_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AsmParser.TermContext,0)


        def PLUS(self):
            return self.getToken(AsmParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AsmParser.MINUS, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_first_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFirst_term" ):
                return visitor.visitFirst_term(self)
            else:
                return visitor.visitChildren(self)




    def first_term(self):

        localctx = AsmParser.First_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_first_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21 or _la==22:
                self.state = 394
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 397
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AsmParser.TermContext,0)


        def PLUS(self):
            return self.getToken(AsmParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AsmParser.MINUS, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_add_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_term" ):
                return visitor.visitAdd_term(self)
            else:
                return visitor.visitChildren(self)




    def add_term(self):

        localctx = AsmParser.Add_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_add_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 400
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(AsmParser.NumberContext,0)


        def label(self):
            return self.getTypedRuleContext(AsmParser.LabelContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = AsmParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_term)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.number()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.label()
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


    class Byte_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(AsmParser.NameContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_byte_specifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByte_specifier" ):
                return visitor.visitByte_specifier(self)
            else:
                return visitor.visitChildren(self)




    def byte_specifier(self):

        localctx = AsmParser.Byte_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_byte_specifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(AsmParser.NameContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = AsmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = AsmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(AsmParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AsmParser.STRING, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = AsmParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(AsmParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegisterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGISTER(self):
            return self.getToken(AsmParser.REGISTER, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_register

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegister" ):
                return visitor.visitRegister(self)
            else:
                return visitor.visitChildren(self)




    def register(self):

        localctx = AsmParser.RegisterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(AsmParser.REGISTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(AsmParser.CHAR, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_character

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacter" ):
                return visitor.visitCharacter(self)
            else:
                return visitor.visitChildren(self)




    def character(self):

        localctx = AsmParser.CharacterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(AsmParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_NUMBER(self):
            return self.getToken(AsmParser.DECIMAL_NUMBER, 0)

        def HEX_NUMBER(self):
            return self.getToken(AsmParser.HEX_NUMBER, 0)

        def BINARY_NUMBER(self):
            return self.getToken(AsmParser.BINARY_NUMBER, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = AsmParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
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


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asect(self):
            return self.getToken(AsmParser.Asect, 0)

        def Break(self):
            return self.getToken(AsmParser.Break, 0)

        def Continue(self):
            return self.getToken(AsmParser.Continue, 0)

        def Do(self):
            return self.getToken(AsmParser.Do, 0)

        def Else(self):
            return self.getToken(AsmParser.Else, 0)

        def End(self):
            return self.getToken(AsmParser.End, 0)

        def Ext(self):
            return self.getToken(AsmParser.Ext, 0)

        def Fi(self):
            return self.getToken(AsmParser.Fi, 0)

        def If(self):
            return self.getToken(AsmParser.If, 0)

        def Is(self):
            return self.getToken(AsmParser.Is, 0)

        def Macro(self):
            return self.getToken(AsmParser.Macro, 0)

        def Rsect(self):
            return self.getToken(AsmParser.Rsect, 0)

        def Stays(self):
            return self.getToken(AsmParser.Stays, 0)

        def Then(self):
            return self.getToken(AsmParser.Then, 0)

        def Tplate(self):
            return self.getToken(AsmParser.Tplate, 0)

        def Until(self):
            return self.getToken(AsmParser.Until, 0)

        def Wend(self):
            return self.getToken(AsmParser.Wend, 0)

        def While(self):
            return self.getToken(AsmParser.While, 0)

        def WORD(self):
            return self.getToken(AsmParser.WORD, 0)

        def WORD_WITH_DOTS(self):
            return self.getToken(AsmParser.WORD_WITH_DOTS, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = AsmParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12885426174) != 0)):
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





