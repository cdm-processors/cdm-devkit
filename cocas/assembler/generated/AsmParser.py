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
        4,1,45,416,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        3,2,143,8,2,1,3,1,3,1,3,4,3,148,8,3,11,3,12,3,149,1,4,1,4,1,4,4,
        4,155,8,4,11,4,12,4,156,1,5,1,5,1,5,4,5,162,8,5,11,5,12,5,163,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,175,8,7,10,7,12,7,178,9,7,
        1,8,1,8,1,8,1,8,3,8,184,8,8,1,8,4,8,187,8,8,11,8,12,8,188,1,8,1,
        8,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,4,11,203,8,11,11,11,
        12,11,204,1,12,1,12,4,12,209,8,12,11,12,12,12,210,1,13,1,13,1,14,
        1,14,1,14,3,14,218,8,14,1,15,1,15,1,15,1,15,3,15,224,8,15,1,16,1,
        16,3,16,228,8,16,1,16,4,16,231,8,16,11,16,12,16,232,1,16,3,16,236,
        8,16,1,16,1,16,3,16,240,8,16,1,16,4,16,243,8,16,11,16,12,16,244,
        3,16,247,8,16,1,17,1,17,1,17,1,17,3,17,253,8,17,1,18,1,18,1,18,5,
        18,258,8,18,10,18,12,18,261,9,18,1,19,1,19,1,19,5,19,266,8,19,10,
        19,12,19,269,9,19,1,20,1,20,4,20,273,8,20,11,20,12,20,274,1,20,1,
        20,1,20,3,20,280,8,20,1,20,1,20,4,20,284,8,20,11,20,12,20,285,1,
        21,5,21,289,8,21,10,21,12,21,292,9,21,1,21,1,21,4,21,296,8,21,11,
        21,12,21,297,1,21,1,21,4,21,302,8,21,11,21,12,21,303,3,21,306,8,
        21,1,22,1,22,1,22,1,22,4,22,312,8,22,11,22,12,22,313,1,23,1,23,1,
        23,1,23,1,24,1,24,4,24,322,8,24,11,24,12,24,323,1,24,1,24,1,25,1,
        25,1,26,1,26,1,27,1,27,4,27,334,8,27,11,27,12,27,335,1,27,1,27,1,
        27,1,27,4,27,342,8,27,11,27,12,27,343,1,27,1,27,1,27,4,27,349,8,
        27,11,27,12,27,350,1,28,1,28,1,29,1,29,4,29,357,8,29,11,29,12,29,
        358,1,29,1,29,1,29,1,29,4,29,365,8,29,11,29,12,29,366,1,30,1,30,
        1,30,1,30,1,30,3,30,374,8,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,
        5,32,383,8,32,10,32,12,32,386,9,32,1,33,3,33,389,8,33,1,33,1,33,
        1,34,1,34,1,34,1,35,1,35,3,35,398,8,35,1,36,1,36,1,37,1,37,1,38,
        1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,43,0,0,
        44,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        0,3,1,0,24,25,1,0,36,38,2,0,1,20,34,35,429,0,91,1,0,0,0,2,111,1,
        0,0,0,4,142,1,0,0,0,6,144,1,0,0,0,8,151,1,0,0,0,10,158,1,0,0,0,12,
        165,1,0,0,0,14,176,1,0,0,0,16,179,1,0,0,0,18,196,1,0,0,0,20,198,
        1,0,0,0,22,200,1,0,0,0,24,206,1,0,0,0,26,212,1,0,0,0,28,217,1,0,
        0,0,30,223,1,0,0,0,32,246,1,0,0,0,34,248,1,0,0,0,36,254,1,0,0,0,
        38,262,1,0,0,0,40,270,1,0,0,0,42,290,1,0,0,0,44,307,1,0,0,0,46,315,
        1,0,0,0,48,319,1,0,0,0,50,327,1,0,0,0,52,329,1,0,0,0,54,331,1,0,
        0,0,56,352,1,0,0,0,58,354,1,0,0,0,60,373,1,0,0,0,62,375,1,0,0,0,
        64,380,1,0,0,0,66,388,1,0,0,0,68,392,1,0,0,0,70,397,1,0,0,0,72,399,
        1,0,0,0,74,401,1,0,0,0,76,403,1,0,0,0,78,405,1,0,0,0,80,407,1,0,
        0,0,82,409,1,0,0,0,84,411,1,0,0,0,86,413,1,0,0,0,88,90,5,41,0,0,
        89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,97,1,
        0,0,0,93,91,1,0,0,0,94,96,3,26,13,0,95,94,1,0,0,0,96,99,1,0,0,0,
        97,95,1,0,0,0,97,98,1,0,0,0,98,103,1,0,0,0,99,97,1,0,0,0,100,102,
        3,4,2,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,
        1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,6,0,0,107,1,1,
        0,0,0,108,110,5,41,0,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,
        0,0,0,111,112,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,114,116,3,
        16,8,0,115,114,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,
        0,0,0,118,122,1,0,0,0,119,121,3,26,13,0,120,119,1,0,0,0,121,124,
        1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,128,1,0,0,0,124,122,
        1,0,0,0,125,127,3,4,2,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,
        1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,
        5,6,0,0,132,3,1,0,0,0,133,134,3,6,3,0,134,135,3,12,6,0,135,143,1,
        0,0,0,136,137,3,8,4,0,137,138,3,12,6,0,138,143,1,0,0,0,139,140,3,
        10,5,0,140,141,3,12,6,0,141,143,1,0,0,0,142,133,1,0,0,0,142,136,
        1,0,0,0,142,139,1,0,0,0,143,5,1,0,0,0,144,145,5,1,0,0,145,147,3,
        84,42,0,146,148,5,41,0,0,147,146,1,0,0,0,148,149,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,7,1,0,0,0,151,152,5,14,0,0,152,154,3,
        86,43,0,153,155,5,41,0,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,
        1,0,0,0,156,157,1,0,0,0,157,9,1,0,0,0,158,159,5,17,0,0,159,161,3,
        86,43,0,160,162,5,41,0,0,161,160,1,0,0,0,162,163,1,0,0,0,163,161,
        1,0,0,0,163,164,1,0,0,0,164,11,1,0,0,0,165,166,3,14,7,0,166,13,1,
        0,0,0,167,175,3,22,11,0,168,175,3,24,12,0,169,175,3,32,16,0,170,
        175,3,40,20,0,171,175,3,54,27,0,172,175,3,58,29,0,173,175,3,16,8,
        0,174,167,1,0,0,0,174,168,1,0,0,0,174,169,1,0,0,0,174,170,1,0,0,
        0,174,171,1,0,0,0,174,172,1,0,0,0,174,173,1,0,0,0,175,178,1,0,0,
        0,176,174,1,0,0,0,176,177,1,0,0,0,177,15,1,0,0,0,178,176,1,0,0,0,
        179,180,5,32,0,0,180,181,3,18,9,0,181,183,3,20,10,0,182,184,5,34,
        0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,187,5,41,
        0,0,186,185,1,0,0,0,187,188,1,0,0,0,188,186,1,0,0,0,188,189,1,0,
        0,0,189,190,1,0,0,0,190,191,6,8,-1,0,191,192,6,8,-1,0,192,193,6,
        8,-1,0,193,194,6,8,-1,0,194,195,6,8,-1,0,195,17,1,0,0,0,196,197,
        5,36,0,0,197,19,1,0,0,0,198,199,5,44,0,0,199,21,1,0,0,0,200,202,
        5,2,0,0,201,203,5,41,0,0,202,201,1,0,0,0,203,204,1,0,0,0,204,202,
        1,0,0,0,204,205,1,0,0,0,205,23,1,0,0,0,206,208,5,3,0,0,207,209,5,
        41,0,0,208,207,1,0,0,0,209,210,1,0,0,0,210,208,1,0,0,0,210,211,1,
        0,0,0,211,25,1,0,0,0,212,213,3,32,16,0,213,27,1,0,0,0,214,218,5,
        7,0,0,215,218,5,8,0,0,216,218,5,9,0,0,217,214,1,0,0,0,217,215,1,
        0,0,0,217,216,1,0,0,0,218,29,1,0,0,0,219,224,5,26,0,0,220,224,5,
        27,0,0,221,224,5,28,0,0,222,224,5,29,0,0,223,219,1,0,0,0,223,220,
        1,0,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,31,1,0,0,0,225,227,3,
        34,17,0,226,228,3,28,14,0,227,226,1,0,0,0,227,228,1,0,0,0,228,230,
        1,0,0,0,229,231,5,41,0,0,230,229,1,0,0,0,231,232,1,0,0,0,232,230,
        1,0,0,0,232,233,1,0,0,0,233,247,1,0,0,0,234,236,3,34,17,0,235,234,
        1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,0,237,239,3,76,38,0,238,240,
        3,38,19,0,239,238,1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,243,
        5,41,0,0,242,241,1,0,0,0,243,244,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,247,1,0,0,0,246,225,1,0,0,0,246,235,1,0,0,0,247,33,1,
        0,0,0,248,249,3,36,18,0,249,252,3,30,15,0,250,251,5,21,0,0,251,253,
        3,64,32,0,252,250,1,0,0,0,252,253,1,0,0,0,253,35,1,0,0,0,254,259,
        3,74,37,0,255,256,5,23,0,0,256,258,3,74,37,0,257,255,1,0,0,0,258,
        261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,37,1,0,0,0,261,259,
        1,0,0,0,262,267,3,60,30,0,263,264,5,23,0,0,264,266,3,60,30,0,265,
        263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,
        39,1,0,0,0,269,267,1,0,0,0,270,272,5,11,0,0,271,273,5,41,0,0,272,
        271,1,0,0,0,273,274,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,
        276,1,0,0,0,276,277,3,42,21,0,277,279,3,14,7,0,278,280,3,48,24,0,
        279,278,1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,283,5,10,0,0,
        282,284,5,41,0,0,283,282,1,0,0,0,284,285,1,0,0,0,285,283,1,0,0,0,
        285,286,1,0,0,0,286,41,1,0,0,0,287,289,3,44,22,0,288,287,1,0,0,0,
        289,292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,293,1,0,0,0,
        292,290,1,0,0,0,293,295,3,46,23,0,294,296,5,41,0,0,295,294,1,0,0,
        0,296,297,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,305,1,0,0,
        0,299,301,5,16,0,0,300,302,5,41,0,0,301,300,1,0,0,0,302,303,1,0,
        0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,306,1,0,0,0,305,299,1,0,
        0,0,305,306,1,0,0,0,306,43,1,0,0,0,307,308,3,46,23,0,308,309,5,23,
        0,0,309,311,3,52,26,0,310,312,5,41,0,0,311,310,1,0,0,0,312,313,1,
        0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,45,1,0,0,0,315,316,3,14,
        7,0,316,317,5,12,0,0,317,318,3,50,25,0,318,47,1,0,0,0,319,321,5,
        5,0,0,320,322,5,41,0,0,321,320,1,0,0,0,322,323,1,0,0,0,323,321,1,
        0,0,0,323,324,1,0,0,0,324,325,1,0,0,0,325,326,3,14,7,0,326,49,1,
        0,0,0,327,328,5,34,0,0,328,51,1,0,0,0,329,330,5,34,0,0,330,53,1,
        0,0,0,331,333,5,20,0,0,332,334,5,41,0,0,333,332,1,0,0,0,334,335,
        1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,337,1,0,0,0,337,338,
        3,56,28,0,338,339,5,15,0,0,339,341,3,50,25,0,340,342,5,41,0,0,341,
        340,1,0,0,0,342,343,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,
        345,1,0,0,0,345,346,3,14,7,0,346,348,5,19,0,0,347,349,5,41,0,0,348,
        347,1,0,0,0,349,350,1,0,0,0,350,348,1,0,0,0,350,351,1,0,0,0,351,
        55,1,0,0,0,352,353,3,14,7,0,353,57,1,0,0,0,354,356,5,4,0,0,355,357,
        5,41,0,0,356,355,1,0,0,0,357,358,1,0,0,0,358,356,1,0,0,0,358,359,
        1,0,0,0,359,360,1,0,0,0,360,361,3,14,7,0,361,362,5,18,0,0,362,364,
        3,50,25,0,363,365,5,41,0,0,364,363,1,0,0,0,365,366,1,0,0,0,366,364,
        1,0,0,0,366,367,1,0,0,0,367,59,1,0,0,0,368,374,3,82,41,0,369,374,
        3,78,39,0,370,374,3,80,40,0,371,374,3,64,32,0,372,374,3,62,31,0,
        373,368,1,0,0,0,373,369,1,0,0,0,373,370,1,0,0,0,373,371,1,0,0,0,
        373,372,1,0,0,0,374,61,1,0,0,0,375,376,3,72,36,0,376,377,5,30,0,
        0,377,378,3,64,32,0,378,379,5,31,0,0,379,63,1,0,0,0,380,384,3,66,
        33,0,381,383,3,68,34,0,382,381,1,0,0,0,383,386,1,0,0,0,384,382,1,
        0,0,0,384,385,1,0,0,0,385,65,1,0,0,0,386,384,1,0,0,0,387,389,7,0,
        0,0,388,387,1,0,0,0,388,389,1,0,0,0,389,390,1,0,0,0,390,391,3,70,
        35,0,391,67,1,0,0,0,392,393,7,0,0,0,393,394,3,70,35,0,394,69,1,0,
        0,0,395,398,3,84,42,0,396,398,3,74,37,0,397,395,1,0,0,0,397,396,
        1,0,0,0,398,71,1,0,0,0,399,400,3,86,43,0,400,73,1,0,0,0,401,402,
        3,86,43,0,402,75,1,0,0,0,403,404,5,34,0,0,404,77,1,0,0,0,405,406,
        5,39,0,0,406,79,1,0,0,0,407,408,5,33,0,0,408,81,1,0,0,0,409,410,
        5,40,0,0,410,83,1,0,0,0,411,412,7,1,0,0,412,85,1,0,0,0,413,414,7,
        2,0,0,414,87,1,0,0,0,46,91,97,103,111,117,122,128,142,149,156,163,
        174,176,183,188,204,210,217,223,227,232,235,239,244,246,252,259,
        267,274,279,285,290,297,303,305,313,323,335,343,350,358,366,373,
        384,388,397
    ]

class AsmParser ( Parser ):

    grammarFileName = "AsmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'asect'", "'break'", "'continue'", "'do'", 
                     "'else'", "'end'", "'ext'", "'file'", "'weak'", "'fi'", 
                     "'if'", "'is'", "'macro'", "'rsect'", "'stays'", "'then'", 
                     "'tplate'", "'until'", "'wend'", "'while'", "'='", 
                     "'.'", "','", "'+'", "'-'", "':'", "'>'", "':>'", "'~>'", 
                     "'('", "')'", "'-|'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Do", "Else", 
                      "End", "Ext", "File", "Weak", "Fi", "If", "Is", "Macro", 
                      "Rsect", "Stays", "Then", "Tplate", "Until", "Wend", 
                      "While", "Equals", "DOT", "COMMA", "PLUS", "MINUS", 
                      "COLON", "ANGLE_BRACKET", "COLON_ANGLE", "TILDE_ANGLE", 
                      "OPEN_PAREN", "CLOSE_PAREN", "LINE_MARK_MARKER", "REGISTER", 
                      "WORD", "WORD_WITH_DOTS", "DECIMAL_NUMBER", "BINARY_NUMBER", 
                      "HEX_NUMBER", "STRING", "CHAR", "NEWLINE", "COMMENT", 
                      "WS", "BASE64", "UNEXPECTED_TOKEN" ]

    RULE_program_nomacros = 0
    RULE_program = 1
    RULE_section = 2
    RULE_asect_header = 3
    RULE_rsect_header = 4
    RULE_tplate_header = 5
    RULE_section_body = 6
    RULE_code_block = 7
    RULE_line_mark = 8
    RULE_line_number = 9
    RULE_filepath = 10
    RULE_break_statement = 11
    RULE_continue_statement = 12
    RULE_top_line = 13
    RULE_ext_type = 14
    RULE_label_suffix = 15
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

    ruleNames =  [ "program_nomacros", "program", "section", "asect_header", 
                   "rsect_header", "tplate_header", "section_body", "code_block", 
                   "line_mark", "line_number", "filepath", "break_statement", 
                   "continue_statement", "top_line", "ext_type", "label_suffix", 
                   "line", "labels_declaration", "labels", "arguments", 
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
    File=8
    Weak=9
    Fi=10
    If=11
    Is=12
    Macro=13
    Rsect=14
    Stays=15
    Then=16
    Tplate=17
    Until=18
    Wend=19
    While=20
    Equals=21
    DOT=22
    COMMA=23
    PLUS=24
    MINUS=25
    COLON=26
    ANGLE_BRACKET=27
    COLON_ANGLE=28
    TILDE_ANGLE=29
    OPEN_PAREN=30
    CLOSE_PAREN=31
    LINE_MARK_MARKER=32
    REGISTER=33
    WORD=34
    WORD_WITH_DOTS=35
    DECIMAL_NUMBER=36
    BINARY_NUMBER=37
    HEX_NUMBER=38
    STRING=39
    CHAR=40
    NEWLINE=41
    COMMENT=42
    WS=43
    BASE64=44
    UNEXPECTED_TOKEN=45

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
            while _la==41:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 147458) != 0):
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
            while _la==41:
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
                if not (_la==32):
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 147458) != 0):
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
            elif token in [14]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.rsect_header()
                self.state = 137
                self.section_body()
                pass
            elif token in [17]:
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


    class Asect_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asect(self):
            return self.getToken(AsmParser.Asect, 0)

        def number(self):
            return self.getTypedRuleContext(AsmParser.NumberContext,0)


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
        self.enterRule(localctx, 6, self.RULE_asect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(AsmParser.Asect)
            self.state = 145
            self.number()
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.match(AsmParser.NEWLINE)
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
        self.enterRule(localctx, 8, self.RULE_rsect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(AsmParser.Rsect)
            self.state = 152
            self.name()
            self.state = 154 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 153
                self.match(AsmParser.NEWLINE)
                self.state = 156 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
        self.enterRule(localctx, 10, self.RULE_tplate_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(AsmParser.Tplate)
            self.state = 159
            self.name()
            self.state = 161 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 160
                self.match(AsmParser.NEWLINE)
                self.state = 163 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
        self.enterRule(localctx, 12, self.RULE_section_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
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
        self.enterRule(localctx, 14, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        self.state = 167
                        self.break_statement()
                        pass

                    elif la_ == 2:
                        self.state = 168
                        self.continue_statement()
                        pass

                    elif la_ == 3:
                        self.state = 169
                        self.line()
                        pass

                    elif la_ == 4:
                        self.state = 170
                        self.conditional()
                        pass

                    elif la_ == 5:
                        self.state = 171
                        self.while_loop()
                        pass

                    elif la_ == 6:
                        self.state = 172
                        self.until_loop()
                        pass

                    elif la_ == 7:
                        self.state = 173
                        self.line_mark()
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_line_mark)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 180
            localctx._line_number = self.line_number()
            self.state = 181
            localctx._filepath = self.filepath()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 182
                self.match(AsmParser.WORD)


            self.state = 186 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 185
                self.match(AsmParser.NEWLINE)
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
        self.enterRule(localctx, 18, self.RULE_line_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
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
        self.enterRule(localctx, 20, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 22, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(AsmParser.Break)
            self.state = 202 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 201
                self.match(AsmParser.NEWLINE)
                self.state = 204 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
        self.enterRule(localctx, 24, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(AsmParser.Continue)
            self.state = 208 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 207
                self.match(AsmParser.NEWLINE)
                self.state = 210 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
        self.enterRule(localctx, 26, self.RULE_top_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ext_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsmParser.RULE_ext_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WeakExtTypeContext(Ext_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.Ext_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Weak(self):
            return self.getToken(AsmParser.Weak, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeakExtType" ):
                return visitor.visitWeakExtType(self)
            else:
                return visitor.visitChildren(self)


    class GlobalExtTypeContext(Ext_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.Ext_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Ext(self):
            return self.getToken(AsmParser.Ext, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalExtType" ):
                return visitor.visitGlobalExtType(self)
            else:
                return visitor.visitChildren(self)


    class FileExtTypeContext(Ext_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.Ext_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def File(self):
            return self.getToken(AsmParser.File, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileExtType" ):
                return visitor.visitFileExtType(self)
            else:
                return visitor.visitChildren(self)



    def ext_type(self):

        localctx = AsmParser.Ext_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ext_type)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = AsmParser.GlobalExtTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(AsmParser.Ext)
                pass
            elif token in [8]:
                localctx = AsmParser.FileExtTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(AsmParser.File)
                pass
            elif token in [9]:
                localctx = AsmParser.WeakExtTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.match(AsmParser.Weak)
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


    class Label_suffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsmParser.RULE_label_suffix

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LocalLabelSuffixContext(Label_suffixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.Label_suffixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(AsmParser.COLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalLabelSuffix" ):
                return visitor.visitLocalLabelSuffix(self)
            else:
                return visitor.visitChildren(self)


    class WeakLabelSuffixContext(Label_suffixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.Label_suffixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TILDE_ANGLE(self):
            return self.getToken(AsmParser.TILDE_ANGLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeakLabelSuffix" ):
                return visitor.visitWeakLabelSuffix(self)
            else:
                return visitor.visitChildren(self)


    class GlobalLabelSuffixContext(Label_suffixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.Label_suffixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ANGLE_BRACKET(self):
            return self.getToken(AsmParser.ANGLE_BRACKET, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalLabelSuffix" ):
                return visitor.visitGlobalLabelSuffix(self)
            else:
                return visitor.visitChildren(self)


    class FileLabelSuffixContext(Label_suffixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.Label_suffixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COLON_ANGLE(self):
            return self.getToken(AsmParser.COLON_ANGLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileLabelSuffix" ):
                return visitor.visitFileLabelSuffix(self)
            else:
                return visitor.visitChildren(self)



    def label_suffix(self):

        localctx = AsmParser.Label_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_label_suffix)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = AsmParser.LocalLabelSuffixContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(AsmParser.COLON)
                pass
            elif token in [27]:
                localctx = AsmParser.GlobalLabelSuffixContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(AsmParser.ANGLE_BRACKET)
                pass
            elif token in [28]:
                localctx = AsmParser.FileLabelSuffixContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(AsmParser.COLON_ANGLE)
                pass
            elif token in [29]:
                localctx = AsmParser.WeakLabelSuffixContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(AsmParser.TILDE_ANGLE)
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

        def ext_type(self):
            return self.getTypedRuleContext(AsmParser.Ext_typeContext,0)

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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = AsmParser.StandaloneLabelsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.labels_declaration()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                    self.state = 226
                    self.ext_type()


                self.state = 230 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 229
                    self.match(AsmParser.NEWLINE)
                    self.state = 232 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==41):
                        break

                pass

            elif la_ == 2:
                localctx = AsmParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 234
                    self.labels_declaration()


                self.state = 237
                self.instruction()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2190485749758) != 0):
                    self.state = 238
                    self.arguments()


                self.state = 242 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 241
                    self.match(AsmParser.NEWLINE)
                    self.state = 244 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==41):
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


        def label_suffix(self):
            return self.getTypedRuleContext(AsmParser.Label_suffixContext,0)


        def Equals(self):
            return self.getToken(AsmParser.Equals, 0)

        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


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
            self.state = 248
            self.labels()
            self.state = 249
            self.label_suffix()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 250
                self.match(AsmParser.Equals)
                self.state = 251
                self.addr_expr()


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
            self.state = 254
            self.label()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 255
                self.match(AsmParser.COMMA)
                self.state = 256
                self.label()
                self.state = 261
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
            self.state = 262
            self.argument()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 263
                self.match(AsmParser.COMMA)
                self.state = 264
                self.argument()
                self.state = 269
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
            self.state = 270
            self.match(AsmParser.If)
            self.state = 272 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 271
                self.match(AsmParser.NEWLINE)
                self.state = 274 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
                    break

            self.state = 276
            self.conditions()
            self.state = 277
            self.code_block()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 278
                self.else_clause()


            self.state = 281
            self.match(AsmParser.Fi)
            self.state = 283 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 282
                self.match(AsmParser.NEWLINE)
                self.state = 285 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 287
                    self.connective_condition() 
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 293
            self.condition()
            self.state = 295 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 294
                self.match(AsmParser.NEWLINE)
                self.state = 297 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
                    break

            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 299
                self.match(AsmParser.Then)
                self.state = 301 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 300
                    self.match(AsmParser.NEWLINE)
                    self.state = 303 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==41):
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
            self.state = 307
            self.condition()
            self.state = 308
            self.match(AsmParser.COMMA)
            self.state = 309
            self.conjunction()
            self.state = 311 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 310
                self.match(AsmParser.NEWLINE)
                self.state = 313 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
            self.state = 315
            self.code_block()
            self.state = 316
            self.match(AsmParser.Is)
            self.state = 317
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
            self.state = 319
            self.match(AsmParser.Else)
            self.state = 321 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 320
                self.match(AsmParser.NEWLINE)
                self.state = 323 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
                    break

            self.state = 325
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
            self.state = 327
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
            self.state = 329
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
            self.state = 331
            self.match(AsmParser.While)
            self.state = 333 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 332
                self.match(AsmParser.NEWLINE)
                self.state = 335 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
                    break

            self.state = 337
            self.while_condition()
            self.state = 338
            self.match(AsmParser.Stays)
            self.state = 339
            self.branch_mnemonic()
            self.state = 341 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 340
                self.match(AsmParser.NEWLINE)
                self.state = 343 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
                    break

            self.state = 345
            self.code_block()
            self.state = 346
            self.match(AsmParser.Wend)
            self.state = 348 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 347
                self.match(AsmParser.NEWLINE)
                self.state = 350 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
            self.state = 352
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
            self.state = 354
            self.match(AsmParser.Do)
            self.state = 356 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 355
                self.match(AsmParser.NEWLINE)
                self.state = 358 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
                    break

            self.state = 360
            self.code_block()
            self.state = 361
            self.match(AsmParser.Until)
            self.state = 362
            self.branch_mnemonic()
            self.state = 364 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 363
                self.match(AsmParser.NEWLINE)
                self.state = 366 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
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
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 371
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 372
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
            self.state = 375
            self.byte_specifier()
            self.state = 376
            self.match(AsmParser.OPEN_PAREN)
            self.state = 377
            self.addr_expr()
            self.state = 378
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
            self.state = 380
            self.first_term()
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 381
                self.add_term()
                self.state = 386
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
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24 or _la==25:
                self.state = 387
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 390
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
            self.state = 392
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 393
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
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.number()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
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
            self.state = 399
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
            self.state = 401
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
            self.state = 403
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
            self.state = 405
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
            self.state = 407
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
            self.state = 409
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
            self.state = 411
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
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

        def File(self):
            return self.getToken(AsmParser.File, 0)

        def Weak(self):
            return self.getToken(AsmParser.Weak, 0)

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
            self.state = 413
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 51541704702) != 0)):
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





