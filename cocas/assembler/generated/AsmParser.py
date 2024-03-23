# Generated from assembler/grammar/AsmParser.g4 by ANTLR 4.13.1
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
        4,1,40,405,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,1,0,5,0,88,8,0,10,0,12,0,91,9,0,1,
        0,1,0,5,0,95,8,0,10,0,12,0,98,9,0,1,0,1,0,1,1,5,1,103,8,1,10,1,12,
        1,106,9,1,1,1,4,1,109,8,1,11,1,12,1,110,1,1,1,1,5,1,115,8,1,10,1,
        12,1,118,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,131,
        8,2,1,3,1,3,1,3,4,3,136,8,3,11,3,12,3,137,1,4,1,4,1,4,4,4,143,8,
        4,11,4,12,4,144,1,5,1,5,1,5,4,5,150,8,5,11,5,12,5,151,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,163,8,7,10,7,12,7,166,9,7,1,8,1,8,
        1,8,1,8,3,8,172,8,8,1,8,4,8,175,8,8,11,8,12,8,176,1,8,1,8,1,8,1,
        8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,4,11,191,8,11,11,11,12,11,
        192,1,12,1,12,4,12,197,8,12,11,12,12,12,198,1,13,1,13,3,13,203,8,
        13,1,13,4,13,206,8,13,11,13,12,13,207,1,13,3,13,211,8,13,1,13,1,
        13,3,13,215,8,13,1,13,4,13,218,8,13,11,13,12,13,219,3,13,222,8,13,
        1,14,1,14,1,14,4,14,227,8,14,11,14,12,14,228,5,14,231,8,14,10,14,
        12,14,234,9,14,1,15,1,15,1,15,1,16,1,16,1,16,5,16,242,8,16,10,16,
        12,16,245,9,16,1,17,1,17,1,17,5,17,250,8,17,10,17,12,17,253,9,17,
        1,18,1,18,4,18,257,8,18,11,18,12,18,258,1,18,1,18,1,18,3,18,264,
        8,18,1,18,1,18,4,18,268,8,18,11,18,12,18,269,1,19,5,19,273,8,19,
        10,19,12,19,276,9,19,1,19,1,19,4,19,280,8,19,11,19,12,19,281,1,19,
        1,19,4,19,286,8,19,11,19,12,19,287,3,19,290,8,19,1,20,1,20,1,20,
        1,20,4,20,296,8,20,11,20,12,20,297,1,21,1,21,1,21,1,21,1,22,1,22,
        4,22,306,8,22,11,22,12,22,307,1,22,1,22,1,23,1,23,1,24,1,24,1,25,
        1,25,4,25,318,8,25,11,25,12,25,319,1,25,1,25,1,25,1,25,4,25,326,
        8,25,11,25,12,25,327,1,25,1,25,1,25,4,25,333,8,25,11,25,12,25,334,
        1,26,1,26,1,27,1,27,4,27,341,8,27,11,27,12,27,342,1,27,1,27,1,27,
        1,27,4,27,349,8,27,11,27,12,27,350,1,28,1,28,1,28,1,28,1,28,3,28,
        358,8,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,5,30,367,8,30,10,30,
        12,30,370,9,30,1,31,3,31,373,8,31,1,31,1,31,1,32,1,32,1,32,1,33,
        1,33,1,33,3,33,383,8,33,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,
        1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,42,
        0,0,43,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        0,4,2,0,23,23,25,25,1,0,21,22,1,0,31,33,2,0,1,18,30,30,414,0,89,
        1,0,0,0,2,104,1,0,0,0,4,130,1,0,0,0,6,132,1,0,0,0,8,139,1,0,0,0,
        10,146,1,0,0,0,12,153,1,0,0,0,14,164,1,0,0,0,16,167,1,0,0,0,18,184,
        1,0,0,0,20,186,1,0,0,0,22,188,1,0,0,0,24,194,1,0,0,0,26,221,1,0,
        0,0,28,232,1,0,0,0,30,235,1,0,0,0,32,238,1,0,0,0,34,246,1,0,0,0,
        36,254,1,0,0,0,38,274,1,0,0,0,40,291,1,0,0,0,42,299,1,0,0,0,44,303,
        1,0,0,0,46,311,1,0,0,0,48,313,1,0,0,0,50,315,1,0,0,0,52,336,1,0,
        0,0,54,338,1,0,0,0,56,357,1,0,0,0,58,359,1,0,0,0,60,364,1,0,0,0,
        62,372,1,0,0,0,64,376,1,0,0,0,66,382,1,0,0,0,68,384,1,0,0,0,70,386,
        1,0,0,0,72,390,1,0,0,0,74,392,1,0,0,0,76,394,1,0,0,0,78,396,1,0,
        0,0,80,398,1,0,0,0,82,400,1,0,0,0,84,402,1,0,0,0,86,88,5,36,0,0,
        87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,
        0,0,0,91,89,1,0,0,0,92,96,3,28,14,0,93,95,3,4,2,0,94,93,1,0,0,0,
        95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,
        0,0,0,99,100,5,6,0,0,100,1,1,0,0,0,101,103,5,36,0,0,102,101,1,0,
        0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,108,1,0,
        0,0,106,104,1,0,0,0,107,109,3,16,8,0,108,107,1,0,0,0,109,110,1,0,
        0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,116,3,28,
        14,0,113,115,3,4,2,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,
        0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,116,1,0,0,0,119,120,5,6,
        0,0,120,3,1,0,0,0,121,122,3,6,3,0,122,123,3,12,6,0,123,131,1,0,0,
        0,124,125,3,8,4,0,125,126,3,12,6,0,126,131,1,0,0,0,127,128,3,10,
        5,0,128,129,3,12,6,0,129,131,1,0,0,0,130,121,1,0,0,0,130,124,1,0,
        0,0,130,127,1,0,0,0,131,5,1,0,0,0,132,133,5,1,0,0,133,135,3,82,41,
        0,134,136,5,36,0,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,1,0,0,
        0,137,138,1,0,0,0,138,7,1,0,0,0,139,140,5,12,0,0,140,142,3,84,42,
        0,141,143,5,36,0,0,142,141,1,0,0,0,143,144,1,0,0,0,144,142,1,0,0,
        0,144,145,1,0,0,0,145,9,1,0,0,0,146,147,5,15,0,0,147,149,3,84,42,
        0,148,150,5,36,0,0,149,148,1,0,0,0,150,151,1,0,0,0,151,149,1,0,0,
        0,151,152,1,0,0,0,152,11,1,0,0,0,153,154,3,14,7,0,154,13,1,0,0,0,
        155,163,3,22,11,0,156,163,3,24,12,0,157,163,3,26,13,0,158,163,3,
        36,18,0,159,163,3,50,25,0,160,163,3,54,27,0,161,163,3,16,8,0,162,
        155,1,0,0,0,162,156,1,0,0,0,162,157,1,0,0,0,162,158,1,0,0,0,162,
        159,1,0,0,0,162,160,1,0,0,0,162,161,1,0,0,0,163,166,1,0,0,0,164,
        162,1,0,0,0,164,165,1,0,0,0,165,15,1,0,0,0,166,164,1,0,0,0,167,168,
        5,28,0,0,168,169,3,18,9,0,169,171,3,20,10,0,170,172,5,30,0,0,171,
        170,1,0,0,0,171,172,1,0,0,0,172,174,1,0,0,0,173,175,5,36,0,0,174,
        173,1,0,0,0,175,176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,
        178,1,0,0,0,178,179,6,8,-1,0,179,180,6,8,-1,0,180,181,6,8,-1,0,181,
        182,6,8,-1,0,182,183,6,8,-1,0,183,17,1,0,0,0,184,185,5,31,0,0,185,
        19,1,0,0,0,186,187,5,39,0,0,187,21,1,0,0,0,188,190,5,2,0,0,189,191,
        5,36,0,0,190,189,1,0,0,0,191,192,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,23,1,0,0,0,194,196,5,3,0,0,195,197,5,36,0,0,196,195,
        1,0,0,0,197,198,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,25,1,
        0,0,0,200,202,3,30,15,0,201,203,5,7,0,0,202,201,1,0,0,0,202,203,
        1,0,0,0,203,205,1,0,0,0,204,206,5,36,0,0,205,204,1,0,0,0,206,207,
        1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,222,1,0,0,0,209,211,
        3,30,15,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,214,
        3,74,37,0,213,215,3,34,17,0,214,213,1,0,0,0,214,215,1,0,0,0,215,
        217,1,0,0,0,216,218,5,36,0,0,217,216,1,0,0,0,218,219,1,0,0,0,219,
        217,1,0,0,0,219,220,1,0,0,0,220,222,1,0,0,0,221,200,1,0,0,0,221,
        210,1,0,0,0,222,27,1,0,0,0,223,224,3,30,15,0,224,226,5,7,0,0,225,
        227,5,36,0,0,226,225,1,0,0,0,227,228,1,0,0,0,228,226,1,0,0,0,228,
        229,1,0,0,0,229,231,1,0,0,0,230,223,1,0,0,0,231,234,1,0,0,0,232,
        230,1,0,0,0,232,233,1,0,0,0,233,29,1,0,0,0,234,232,1,0,0,0,235,236,
        3,32,16,0,236,237,7,0,0,0,237,31,1,0,0,0,238,243,3,72,36,0,239,240,
        5,20,0,0,240,242,3,72,36,0,241,239,1,0,0,0,242,245,1,0,0,0,243,241,
        1,0,0,0,243,244,1,0,0,0,244,33,1,0,0,0,245,243,1,0,0,0,246,251,3,
        56,28,0,247,248,5,20,0,0,248,250,3,56,28,0,249,247,1,0,0,0,250,253,
        1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,35,1,0,0,0,253,251,1,
        0,0,0,254,256,5,9,0,0,255,257,5,36,0,0,256,255,1,0,0,0,257,258,1,
        0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,0,260,261,3,
        38,19,0,261,263,3,14,7,0,262,264,3,44,22,0,263,262,1,0,0,0,263,264,
        1,0,0,0,264,265,1,0,0,0,265,267,5,8,0,0,266,268,5,36,0,0,267,266,
        1,0,0,0,268,269,1,0,0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,37,1,
        0,0,0,271,273,3,40,20,0,272,271,1,0,0,0,273,276,1,0,0,0,274,272,
        1,0,0,0,274,275,1,0,0,0,275,277,1,0,0,0,276,274,1,0,0,0,277,279,
        3,42,21,0,278,280,5,36,0,0,279,278,1,0,0,0,280,281,1,0,0,0,281,279,
        1,0,0,0,281,282,1,0,0,0,282,289,1,0,0,0,283,285,5,14,0,0,284,286,
        5,36,0,0,285,284,1,0,0,0,286,287,1,0,0,0,287,285,1,0,0,0,287,288,
        1,0,0,0,288,290,1,0,0,0,289,283,1,0,0,0,289,290,1,0,0,0,290,39,1,
        0,0,0,291,292,3,42,21,0,292,293,5,20,0,0,293,295,3,48,24,0,294,296,
        5,36,0,0,295,294,1,0,0,0,296,297,1,0,0,0,297,295,1,0,0,0,297,298,
        1,0,0,0,298,41,1,0,0,0,299,300,3,14,7,0,300,301,5,10,0,0,301,302,
        3,46,23,0,302,43,1,0,0,0,303,305,5,5,0,0,304,306,5,36,0,0,305,304,
        1,0,0,0,306,307,1,0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,309,
        1,0,0,0,309,310,3,14,7,0,310,45,1,0,0,0,311,312,5,30,0,0,312,47,
        1,0,0,0,313,314,5,30,0,0,314,49,1,0,0,0,315,317,5,18,0,0,316,318,
        5,36,0,0,317,316,1,0,0,0,318,319,1,0,0,0,319,317,1,0,0,0,319,320,
        1,0,0,0,320,321,1,0,0,0,321,322,3,52,26,0,322,323,5,13,0,0,323,325,
        3,46,23,0,324,326,5,36,0,0,325,324,1,0,0,0,326,327,1,0,0,0,327,325,
        1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,0,329,330,3,14,7,0,330,332,
        5,17,0,0,331,333,5,36,0,0,332,331,1,0,0,0,333,334,1,0,0,0,334,332,
        1,0,0,0,334,335,1,0,0,0,335,51,1,0,0,0,336,337,3,14,7,0,337,53,1,
        0,0,0,338,340,5,4,0,0,339,341,5,36,0,0,340,339,1,0,0,0,341,342,1,
        0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,344,1,0,0,0,344,345,3,
        14,7,0,345,346,5,16,0,0,346,348,3,46,23,0,347,349,5,36,0,0,348,347,
        1,0,0,0,349,350,1,0,0,0,350,348,1,0,0,0,350,351,1,0,0,0,351,55,1,
        0,0,0,352,358,3,80,40,0,353,358,3,76,38,0,354,358,3,78,39,0,355,
        358,3,60,30,0,356,358,3,58,29,0,357,352,1,0,0,0,357,353,1,0,0,0,
        357,354,1,0,0,0,357,355,1,0,0,0,357,356,1,0,0,0,358,57,1,0,0,0,359,
        360,3,68,34,0,360,361,5,26,0,0,361,362,3,60,30,0,362,363,5,27,0,
        0,363,59,1,0,0,0,364,368,3,62,31,0,365,367,3,64,32,0,366,365,1,0,
        0,0,367,370,1,0,0,0,368,366,1,0,0,0,368,369,1,0,0,0,369,61,1,0,0,
        0,370,368,1,0,0,0,371,373,7,1,0,0,372,371,1,0,0,0,372,373,1,0,0,
        0,373,374,1,0,0,0,374,375,3,66,33,0,375,63,1,0,0,0,376,377,7,1,0,
        0,377,378,3,66,33,0,378,65,1,0,0,0,379,383,3,82,41,0,380,383,3,70,
        35,0,381,383,3,72,36,0,382,379,1,0,0,0,382,380,1,0,0,0,382,381,1,
        0,0,0,383,67,1,0,0,0,384,385,3,84,42,0,385,69,1,0,0,0,386,387,3,
        84,42,0,387,388,5,19,0,0,388,389,3,84,42,0,389,71,1,0,0,0,390,391,
        3,84,42,0,391,73,1,0,0,0,392,393,5,30,0,0,393,75,1,0,0,0,394,395,
        5,34,0,0,395,77,1,0,0,0,396,397,5,29,0,0,397,79,1,0,0,0,398,399,
        5,35,0,0,399,81,1,0,0,0,400,401,7,2,0,0,401,83,1,0,0,0,402,403,7,
        3,0,0,403,85,1,0,0,0,43,89,96,104,110,116,130,137,144,151,162,164,
        171,176,192,198,202,207,210,214,219,221,228,232,243,251,258,263,
        269,274,281,287,289,297,307,319,327,334,342,350,357,368,372,382
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
                     "'-'", "':'", "'*'", "'>'", "'('", "')'", "'-|'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Do", "Else", 
                      "End", "Ext", "Fi", "If", "Is", "Macro", "Rsect", 
                      "Stays", "Then", "Tplate", "Until", "Wend", "While", 
                      "DOT", "COMMA", "PLUS", "MINUS", "COLON", "ASTERISK", 
                      "ANGLE_BRACKET", "OPEN_PAREN", "CLOSE_PAREN", "LINE_MARK_MARKER", 
                      "REGISTER", "WORD", "DECIMAL_NUMBER", "BINARY_NUMBER", 
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
    RULE_line = 13
    RULE_shared_externals = 14
    RULE_labels_declaration = 15
    RULE_labels = 16
    RULE_arguments = 17
    RULE_conditional = 18
    RULE_conditions = 19
    RULE_connective_condition = 20
    RULE_condition = 21
    RULE_else_clause = 22
    RULE_branch_mnemonic = 23
    RULE_conjunction = 24
    RULE_while_loop = 25
    RULE_while_condition = 26
    RULE_until_loop = 27
    RULE_argument = 28
    RULE_byte_expr = 29
    RULE_addr_expr = 30
    RULE_first_term = 31
    RULE_add_term = 32
    RULE_term = 33
    RULE_byte_specifier = 34
    RULE_template_field = 35
    RULE_label = 36
    RULE_instruction = 37
    RULE_string = 38
    RULE_register = 39
    RULE_character = 40
    RULE_number = 41
    RULE_name = 42

    ruleNames =  [ "program_nomacros", "program", "section", "asect_header", 
                   "rsect_header", "tplate_header", "section_body", "code_block", 
                   "line_mark", "line_number", "filepath", "break_statement", 
                   "continue_statement", "line", "shared_externals", "labels_declaration", 
                   "labels", "arguments", "conditional", "conditions", "connective_condition", 
                   "condition", "else_clause", "branch_mnemonic", "conjunction", 
                   "while_loop", "while_condition", "until_loop", "argument", 
                   "byte_expr", "addr_expr", "first_term", "add_term", "term", 
                   "byte_specifier", "template_field", "label", "instruction", 
                   "string", "register", "character", "number", "name" ]

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
    REGISTER=29
    WORD=30
    DECIMAL_NUMBER=31
    BINARY_NUMBER=32
    HEX_NUMBER=33
    STRING=34
    CHAR=35
    NEWLINE=36
    COMMENT=37
    WS=38
    BASE64=39
    UNEXPECTED_TOKEN=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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

        def shared_externals(self):
            return self.getTypedRuleContext(AsmParser.Shared_externalsContext,0)


        def End(self):
            return self.getToken(AsmParser.End, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

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
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 86
                self.match(AsmParser.NEWLINE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.shared_externals()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36866) != 0):
                self.state = 93
                self.section()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
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

        def shared_externals(self):
            return self.getTypedRuleContext(AsmParser.Shared_externalsContext,0)


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
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 101
                self.match(AsmParser.NEWLINE)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self.line_mark()
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
                    break

            self.state = 112
            self.shared_externals()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36866) != 0):
                self.state = 113
                self.section()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
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
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.asect_header()
                self.state = 122
                self.section_body()
                pass
            elif token in [12]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.rsect_header()
                self.state = 125
                self.section_body()
                pass
            elif token in [15]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.tplate_header()
                self.state = 128
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
            self.state = 132
            self.match(AsmParser.Asect)
            self.state = 133
            self.number()
            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.match(AsmParser.NEWLINE)
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
            self.state = 139
            self.match(AsmParser.Rsect)
            self.state = 140
            self.name()
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 141
                self.match(AsmParser.NEWLINE)
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
            self.state = 146
            self.match(AsmParser.Tplate)
            self.state = 147
            self.name()
            self.state = 149 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 148
                self.match(AsmParser.NEWLINE)
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
            self.state = 153
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
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 155
                        self.break_statement()
                        pass

                    elif la_ == 2:
                        self.state = 156
                        self.continue_statement()
                        pass

                    elif la_ == 3:
                        self.state = 157
                        self.line()
                        pass

                    elif la_ == 4:
                        self.state = 158
                        self.conditional()
                        pass

                    elif la_ == 5:
                        self.state = 159
                        self.while_loop()
                        pass

                    elif la_ == 6:
                        self.state = 160
                        self.until_loop()
                        pass

                    elif la_ == 7:
                        self.state = 161
                        self.line_mark()
                        pass

             
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            self.state = 167
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 168
            localctx._line_number = self.line_number()
            self.state = 169
            localctx._filepath = self.filepath()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 170
                self.match(AsmParser.WORD)


            self.state = 174 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 173
                self.match(AsmParser.NEWLINE)
                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
            self.state = 184
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
            self.state = 186
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
            self.state = 188
            self.match(AsmParser.Break)
            self.state = 190 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 189
                self.match(AsmParser.NEWLINE)
                self.state = 192 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
            self.state = 194
            self.match(AsmParser.Continue)
            self.state = 196 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 195
                self.match(AsmParser.NEWLINE)
                self.state = 198 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

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
        self.enterRule(localctx, 26, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = AsmParser.StandaloneLabelsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.labels_declaration()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 201
                    self.match(AsmParser.Ext)


                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 204
                    self.match(AsmParser.NEWLINE)
                    self.state = 207 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==36):
                        break

                pass

            elif la_ == 2:
                localctx = AsmParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 209
                    self.labels_declaration()


                self.state = 212
                self.instruction()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68189421566) != 0):
                    self.state = 213
                    self.arguments()


                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 216
                    self.match(AsmParser.NEWLINE)
                    self.state = 219 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==36):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shared_externalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labels_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Labels_declarationContext)
            else:
                return self.getTypedRuleContext(AsmParser.Labels_declarationContext,i)


        def Ext(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.Ext)
            else:
                return self.getToken(AsmParser.Ext, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_shared_externals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShared_externals" ):
                return visitor.visitShared_externals(self)
            else:
                return visitor.visitChildren(self)




    def shared_externals(self):

        localctx = AsmParser.Shared_externalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_shared_externals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 223
                    self.labels_declaration()
                    self.state = 224
                    self.match(AsmParser.Ext)
                    self.state = 226 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 225
                        self.match(AsmParser.NEWLINE)
                        self.state = 228 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==36):
                            break
             
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_labels_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.labels()
            self.state = 236
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
        self.enterRule(localctx, 32, self.RULE_labels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.label()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 239
                self.match(AsmParser.COMMA)
                self.state = 240
                self.label()
                self.state = 245
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
        self.enterRule(localctx, 34, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.argument()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 247
                self.match(AsmParser.COMMA)
                self.state = 248
                self.argument()
                self.state = 253
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
        self.enterRule(localctx, 36, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(AsmParser.If)
            self.state = 256 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 255
                self.match(AsmParser.NEWLINE)
                self.state = 258 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 260
            self.conditions()
            self.state = 261
            self.code_block()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 262
                self.else_clause()


            self.state = 265
            self.match(AsmParser.Fi)
            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 266
                self.match(AsmParser.NEWLINE)
                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
        self.enterRule(localctx, 38, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 271
                    self.connective_condition() 
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 277
            self.condition()
            self.state = 279 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.match(AsmParser.NEWLINE)
                self.state = 281 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 283
                self.match(AsmParser.Then)
                self.state = 285 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 284
                    self.match(AsmParser.NEWLINE)
                    self.state = 287 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==36):
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
        self.enterRule(localctx, 40, self.RULE_connective_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.condition()
            self.state = 292
            self.match(AsmParser.COMMA)
            self.state = 293
            self.conjunction()
            self.state = 295 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 294
                self.match(AsmParser.NEWLINE)
                self.state = 297 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
        self.enterRule(localctx, 42, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.code_block()
            self.state = 300
            self.match(AsmParser.Is)
            self.state = 301
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
        self.enterRule(localctx, 44, self.RULE_else_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(AsmParser.Else)
            self.state = 305 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 304
                self.match(AsmParser.NEWLINE)
                self.state = 307 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 309
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
        self.enterRule(localctx, 46, self.RULE_branch_mnemonic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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
        self.enterRule(localctx, 48, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
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
        self.enterRule(localctx, 50, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(AsmParser.While)
            self.state = 317 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 316
                self.match(AsmParser.NEWLINE)
                self.state = 319 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 321
            self.while_condition()
            self.state = 322
            self.match(AsmParser.Stays)
            self.state = 323
            self.branch_mnemonic()
            self.state = 325 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 324
                self.match(AsmParser.NEWLINE)
                self.state = 327 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 329
            self.code_block()
            self.state = 330
            self.match(AsmParser.Wend)
            self.state = 332 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 331
                self.match(AsmParser.NEWLINE)
                self.state = 334 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
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
        self.enterRule(localctx, 52, self.RULE_while_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
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
        self.enterRule(localctx, 54, self.RULE_until_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(AsmParser.Do)
            self.state = 340 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 339
                self.match(AsmParser.NEWLINE)
                self.state = 342 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 344
            self.code_block()
            self.state = 345
            self.match(AsmParser.Until)
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
                if not (_la==36):
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
        self.enterRule(localctx, 56, self.RULE_argument)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 356
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
        self.enterRule(localctx, 58, self.RULE_byte_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.byte_specifier()
            self.state = 360
            self.match(AsmParser.OPEN_PAREN)
            self.state = 361
            self.addr_expr()
            self.state = 362
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
        self.enterRule(localctx, 60, self.RULE_addr_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.first_term()
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 365
                self.add_term()
                self.state = 370
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
        self.enterRule(localctx, 62, self.RULE_first_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21 or _la==22:
                self.state = 371
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 374
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
        self.enterRule(localctx, 64, self.RULE_add_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 377
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


        def template_field(self):
            return self.getTypedRuleContext(AsmParser.Template_fieldContext,0)


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
        self.enterRule(localctx, 66, self.RULE_term)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.template_field()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.label()
                pass


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
        self.enterRule(localctx, 68, self.RULE_byte_specifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Template_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.NameContext)
            else:
                return self.getTypedRuleContext(AsmParser.NameContext,i)


        def DOT(self):
            return self.getToken(AsmParser.DOT, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_template_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplate_field" ):
                return visitor.visitTemplate_field(self)
            else:
                return visitor.visitChildren(self)




    def template_field(self):

        localctx = AsmParser.Template_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_template_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.name()
            self.state = 387
            self.match(AsmParser.DOT)
            self.state = 388
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
        self.enterRule(localctx, 72, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
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
        self.enterRule(localctx, 74, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
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
        self.enterRule(localctx, 76, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
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
        self.enterRule(localctx, 78, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
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
        self.enterRule(localctx, 80, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
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
        self.enterRule(localctx, 82, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
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

        def getRuleIndex(self):
            return AsmParser.RULE_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = AsmParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1074266110) != 0)):
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





