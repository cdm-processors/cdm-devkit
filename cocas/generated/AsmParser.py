# Generated from AsmParser.g4 by ANTLR 4.11.1
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
        4,1,43,381,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,0,4,0,92,8,
        0,11,0,12,0,93,1,0,5,0,97,8,0,10,0,12,0,100,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,113,8,1,1,2,1,2,1,2,4,2,118,8,2,
        11,2,12,2,119,1,3,1,3,1,3,4,3,125,8,3,11,3,12,3,126,1,4,1,4,1,4,
        4,4,132,8,4,11,4,12,4,133,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,5,6,146,8,6,10,6,12,6,149,9,6,1,7,1,7,1,7,1,7,3,7,155,8,7,1,7,
        4,7,158,8,7,11,7,12,7,159,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,
        9,1,10,1,10,4,10,174,8,10,11,10,12,10,175,1,11,1,11,4,11,180,8,11,
        11,11,12,11,181,1,12,1,12,3,12,186,8,12,1,12,4,12,189,8,12,11,12,
        12,12,190,1,12,3,12,194,8,12,1,12,1,12,3,12,198,8,12,1,12,4,12,201,
        8,12,11,12,12,12,202,3,12,205,8,12,1,13,1,13,1,13,1,14,1,14,1,14,
        5,14,213,8,14,10,14,12,14,216,9,14,1,15,1,15,4,15,220,8,15,11,15,
        12,15,221,1,15,1,15,1,15,3,15,227,8,15,1,15,1,15,4,15,231,8,15,11,
        15,12,15,232,1,16,5,16,236,8,16,10,16,12,16,239,9,16,1,16,1,16,4,
        16,243,8,16,11,16,12,16,244,1,16,1,16,4,16,249,8,16,11,16,12,16,
        250,3,16,253,8,16,1,17,1,17,1,17,1,17,4,17,259,8,17,11,17,12,17,
        260,1,18,1,18,1,18,1,18,1,19,1,19,4,19,269,8,19,11,19,12,19,270,
        1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,4,22,281,8,22,11,22,12,22,
        282,1,22,1,22,1,22,1,22,4,22,289,8,22,11,22,12,22,290,1,22,1,22,
        1,22,4,22,296,8,22,11,22,12,22,297,1,23,1,23,1,24,1,24,4,24,304,
        8,24,11,24,12,24,305,1,24,1,24,1,24,1,24,4,24,312,8,24,11,24,12,
        24,313,1,25,1,25,1,25,1,25,1,25,4,25,321,8,25,11,25,12,25,322,1,
        26,1,26,3,26,327,8,26,1,27,1,27,1,27,1,27,1,27,3,27,334,8,27,1,28,
        1,28,1,28,1,28,1,28,1,29,1,29,5,29,343,8,29,10,29,12,29,346,9,29,
        1,30,3,30,349,8,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,3,32,
        359,8,32,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,36,1,36,1,37,
        1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,41,0,0,42,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,0,5,2,0,26,26,28,
        28,1,0,24,25,1,0,20,21,1,0,34,36,2,0,1,21,33,33,389,0,87,1,0,0,0,
        2,112,1,0,0,0,4,114,1,0,0,0,6,121,1,0,0,0,8,128,1,0,0,0,10,135,1,
        0,0,0,12,147,1,0,0,0,14,150,1,0,0,0,16,167,1,0,0,0,18,169,1,0,0,
        0,20,171,1,0,0,0,22,177,1,0,0,0,24,204,1,0,0,0,26,206,1,0,0,0,28,
        209,1,0,0,0,30,217,1,0,0,0,32,237,1,0,0,0,34,254,1,0,0,0,36,262,
        1,0,0,0,38,266,1,0,0,0,40,274,1,0,0,0,42,276,1,0,0,0,44,278,1,0,
        0,0,46,299,1,0,0,0,48,301,1,0,0,0,50,315,1,0,0,0,52,326,1,0,0,0,
        54,333,1,0,0,0,56,335,1,0,0,0,58,340,1,0,0,0,60,348,1,0,0,0,62,352,
        1,0,0,0,64,358,1,0,0,0,66,360,1,0,0,0,68,362,1,0,0,0,70,366,1,0,
        0,0,72,368,1,0,0,0,74,370,1,0,0,0,76,372,1,0,0,0,78,374,1,0,0,0,
        80,376,1,0,0,0,82,378,1,0,0,0,84,86,5,39,0,0,85,84,1,0,0,0,86,89,
        1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,
        90,92,3,14,7,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,
        0,0,0,94,98,1,0,0,0,95,97,3,2,1,0,96,95,1,0,0,0,97,100,1,0,0,0,98,
        96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,5,
        6,0,0,102,1,1,0,0,0,103,104,3,4,2,0,104,105,3,10,5,0,105,113,1,0,
        0,0,106,107,3,6,3,0,107,108,3,10,5,0,108,113,1,0,0,0,109,110,3,8,
        4,0,110,111,3,10,5,0,111,113,1,0,0,0,112,103,1,0,0,0,112,106,1,0,
        0,0,112,109,1,0,0,0,113,3,1,0,0,0,114,115,5,1,0,0,115,117,3,80,40,
        0,116,118,5,39,0,0,117,116,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,
        0,119,120,1,0,0,0,120,5,1,0,0,0,121,122,5,13,0,0,122,124,3,82,41,
        0,123,125,5,39,0,0,124,123,1,0,0,0,125,126,1,0,0,0,126,124,1,0,0,
        0,126,127,1,0,0,0,127,7,1,0,0,0,128,129,5,16,0,0,129,131,3,82,41,
        0,130,132,5,39,0,0,131,130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,
        0,133,134,1,0,0,0,134,9,1,0,0,0,135,136,3,12,6,0,136,11,1,0,0,0,
        137,146,3,20,10,0,138,146,3,22,11,0,139,146,3,24,12,0,140,146,3,
        30,15,0,141,146,3,44,22,0,142,146,3,48,24,0,143,146,3,50,25,0,144,
        146,3,14,7,0,145,137,1,0,0,0,145,138,1,0,0,0,145,139,1,0,0,0,145,
        140,1,0,0,0,145,141,1,0,0,0,145,142,1,0,0,0,145,143,1,0,0,0,145,
        144,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,
        13,1,0,0,0,149,147,1,0,0,0,150,151,5,31,0,0,151,152,3,16,8,0,152,
        154,3,18,9,0,153,155,5,33,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,
        157,1,0,0,0,156,158,5,39,0,0,157,156,1,0,0,0,158,159,1,0,0,0,159,
        157,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,162,6,7,-1,0,162,
        163,6,7,-1,0,163,164,6,7,-1,0,164,165,6,7,-1,0,165,166,6,7,-1,0,
        166,15,1,0,0,0,167,168,5,34,0,0,168,17,1,0,0,0,169,170,5,42,0,0,
        170,19,1,0,0,0,171,173,5,2,0,0,172,174,5,39,0,0,173,172,1,0,0,0,
        174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,21,1,0,0,0,177,
        179,5,3,0,0,178,180,5,39,0,0,179,178,1,0,0,0,180,181,1,0,0,0,181,
        179,1,0,0,0,181,182,1,0,0,0,182,23,1,0,0,0,183,185,3,26,13,0,184,
        186,5,7,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,
        189,5,39,0,0,188,187,1,0,0,0,189,190,1,0,0,0,190,188,1,0,0,0,190,
        191,1,0,0,0,191,205,1,0,0,0,192,194,3,26,13,0,193,192,1,0,0,0,193,
        194,1,0,0,0,194,195,1,0,0,0,195,197,3,72,36,0,196,198,3,28,14,0,
        197,196,1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,201,5,39,0,0,
        200,199,1,0,0,0,201,202,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,
        203,205,1,0,0,0,204,183,1,0,0,0,204,193,1,0,0,0,205,25,1,0,0,0,206,
        207,3,70,35,0,207,208,7,0,0,0,208,27,1,0,0,0,209,214,3,54,27,0,210,
        211,5,23,0,0,211,213,3,54,27,0,212,210,1,0,0,0,213,216,1,0,0,0,214,
        212,1,0,0,0,214,215,1,0,0,0,215,29,1,0,0,0,216,214,1,0,0,0,217,219,
        5,10,0,0,218,220,5,39,0,0,219,218,1,0,0,0,220,221,1,0,0,0,221,219,
        1,0,0,0,221,222,1,0,0,0,222,223,1,0,0,0,223,224,3,32,16,0,224,226,
        3,12,6,0,225,227,3,38,19,0,226,225,1,0,0,0,226,227,1,0,0,0,227,228,
        1,0,0,0,228,230,5,8,0,0,229,231,5,39,0,0,230,229,1,0,0,0,231,232,
        1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,31,1,0,0,0,234,236,3,
        34,17,0,235,234,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,
        1,0,0,0,238,240,1,0,0,0,239,237,1,0,0,0,240,242,3,36,18,0,241,243,
        5,39,0,0,242,241,1,0,0,0,243,244,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,252,1,0,0,0,246,248,5,15,0,0,247,249,5,39,0,0,248,247,
        1,0,0,0,249,250,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,253,
        1,0,0,0,252,246,1,0,0,0,252,253,1,0,0,0,253,33,1,0,0,0,254,255,3,
        36,18,0,255,256,5,23,0,0,256,258,3,42,21,0,257,259,5,39,0,0,258,
        257,1,0,0,0,259,260,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,
        35,1,0,0,0,262,263,3,12,6,0,263,264,5,11,0,0,264,265,3,40,20,0,265,
        37,1,0,0,0,266,268,5,5,0,0,267,269,5,39,0,0,268,267,1,0,0,0,269,
        270,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,272,1,0,0,0,272,
        273,3,12,6,0,273,39,1,0,0,0,274,275,5,33,0,0,275,41,1,0,0,0,276,
        277,5,33,0,0,277,43,1,0,0,0,278,280,5,19,0,0,279,281,5,39,0,0,280,
        279,1,0,0,0,281,282,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,
        284,1,0,0,0,284,285,3,46,23,0,285,286,5,14,0,0,286,288,3,40,20,0,
        287,289,5,39,0,0,288,287,1,0,0,0,289,290,1,0,0,0,290,288,1,0,0,0,
        290,291,1,0,0,0,291,292,1,0,0,0,292,293,3,12,6,0,293,295,5,18,0,
        0,294,296,5,39,0,0,295,294,1,0,0,0,296,297,1,0,0,0,297,295,1,0,0,
        0,297,298,1,0,0,0,298,45,1,0,0,0,299,300,3,12,6,0,300,47,1,0,0,0,
        301,303,5,4,0,0,302,304,5,39,0,0,303,302,1,0,0,0,304,305,1,0,0,0,
        305,303,1,0,0,0,305,306,1,0,0,0,306,307,1,0,0,0,307,308,3,12,6,0,
        308,309,5,17,0,0,309,311,3,40,20,0,310,312,5,39,0,0,311,310,1,0,
        0,0,312,313,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,49,1,0,0,
        0,315,316,5,9,0,0,316,317,3,40,20,0,317,318,5,23,0,0,318,320,3,52,
        26,0,319,321,5,39,0,0,320,319,1,0,0,0,321,322,1,0,0,0,322,320,1,
        0,0,0,322,323,1,0,0,0,323,51,1,0,0,0,324,327,3,58,29,0,325,327,3,
        56,28,0,326,324,1,0,0,0,326,325,1,0,0,0,327,53,1,0,0,0,328,334,3,
        78,39,0,329,334,3,74,37,0,330,334,3,76,38,0,331,334,3,58,29,0,332,
        334,3,56,28,0,333,328,1,0,0,0,333,329,1,0,0,0,333,330,1,0,0,0,333,
        331,1,0,0,0,333,332,1,0,0,0,334,55,1,0,0,0,335,336,3,66,33,0,336,
        337,5,29,0,0,337,338,3,58,29,0,338,339,5,30,0,0,339,57,1,0,0,0,340,
        344,3,60,30,0,341,343,3,62,31,0,342,341,1,0,0,0,343,346,1,0,0,0,
        344,342,1,0,0,0,344,345,1,0,0,0,345,59,1,0,0,0,346,344,1,0,0,0,347,
        349,7,1,0,0,348,347,1,0,0,0,348,349,1,0,0,0,349,350,1,0,0,0,350,
        351,3,64,32,0,351,61,1,0,0,0,352,353,7,1,0,0,353,354,3,64,32,0,354,
        63,1,0,0,0,355,359,3,80,40,0,356,359,3,68,34,0,357,359,3,70,35,0,
        358,355,1,0,0,0,358,356,1,0,0,0,358,357,1,0,0,0,359,65,1,0,0,0,360,
        361,7,2,0,0,361,67,1,0,0,0,362,363,3,82,41,0,363,364,5,22,0,0,364,
        365,3,82,41,0,365,69,1,0,0,0,366,367,3,82,41,0,367,71,1,0,0,0,368,
        369,5,33,0,0,369,73,1,0,0,0,370,371,5,37,0,0,371,75,1,0,0,0,372,
        373,5,32,0,0,373,77,1,0,0,0,374,375,5,38,0,0,375,79,1,0,0,0,376,
        377,7,3,0,0,377,81,1,0,0,0,378,379,7,4,0,0,379,83,1,0,0,0,40,87,
        93,98,112,119,126,133,145,147,154,159,175,181,185,190,193,197,202,
        204,214,221,226,232,237,244,250,252,260,270,282,290,297,305,313,
        322,326,333,344,348,358
    ]

class AsmParser ( Parser ):

    grammarFileName = "AsmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'asect'", "'break'", "'continue'", "'do'", 
                     "'else'", "'end'", "'ext'", "'fi'", "'goto'", "'if'", 
                     "'is'", "'macro'", "'rsect'", "'stays'", "'then'", 
                     "'tplate'", "'until'", "'wend'", "'while'", "'low'", 
                     "'high'", "'.'", "','", "'+'", "'-'", "':'", "'*'", 
                     "'>'", "'('", "')'", "'-|'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Do", "Else", 
                      "End", "Ext", "Fi", "Goto", "If", "Is", "Macro", "Rsect", 
                      "Stays", "Then", "Tplate", "Until", "Wend", "While", 
                      "Low", "High", "DOT", "COMMA", "PLUS", "MINUS", "COLON", 
                      "ASTERISK", "ANGLE_BRACKET", "OPEN_PAREN", "CLOSE_PAREN", 
                      "LINE_MARK_MARKER", "REGISTER", "WORD", "DECIMAL_NUMBER", 
                      "BINARY_NUMBER", "HEX_NUMBER", "STRING", "CHAR", "NEWLINE", 
                      "COMMENT", "WS", "BASE64", "UNEXPECTED_TOKEN" ]

    RULE_program = 0
    RULE_section = 1
    RULE_asect_header = 2
    RULE_rsect_header = 3
    RULE_tplate_header = 4
    RULE_section_body = 5
    RULE_code_block = 6
    RULE_line_mark = 7
    RULE_line_number = 8
    RULE_filepath = 9
    RULE_break_statement = 10
    RULE_continue_statement = 11
    RULE_line = 12
    RULE_label_declaration = 13
    RULE_arguments = 14
    RULE_conditional = 15
    RULE_conditions = 16
    RULE_connective_condition = 17
    RULE_condition = 18
    RULE_else_clause = 19
    RULE_branch_mnemonic = 20
    RULE_conjunction = 21
    RULE_while_loop = 22
    RULE_while_condition = 23
    RULE_until_loop = 24
    RULE_goto_statement = 25
    RULE_goto_argument = 26
    RULE_argument = 27
    RULE_byte_expr = 28
    RULE_addr_expr = 29
    RULE_first_term = 30
    RULE_add_term = 31
    RULE_term = 32
    RULE_byte_specifier = 33
    RULE_template_field = 34
    RULE_label = 35
    RULE_instruction = 36
    RULE_string = 37
    RULE_register = 38
    RULE_character = 39
    RULE_number = 40
    RULE_name = 41

    ruleNames =  [ "program", "section", "asect_header", "rsect_header", 
                   "tplate_header", "section_body", "code_block", "line_mark", 
                   "line_number", "filepath", "break_statement", "continue_statement", 
                   "line", "label_declaration", "arguments", "conditional", 
                   "conditions", "connective_condition", "condition", "else_clause", 
                   "branch_mnemonic", "conjunction", "while_loop", "while_condition", 
                   "until_loop", "goto_statement", "goto_argument", "argument", 
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
    Goto=9
    If=10
    Is=11
    Macro=12
    Rsect=13
    Stays=14
    Then=15
    Tplate=16
    Until=17
    Wend=18
    While=19
    Low=20
    High=21
    DOT=22
    COMMA=23
    PLUS=24
    MINUS=25
    COLON=26
    ASTERISK=27
    ANGLE_BRACKET=28
    OPEN_PAREN=29
    CLOSE_PAREN=30
    LINE_MARK_MARKER=31
    REGISTER=32
    WORD=33
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
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.current_file = ''
        self.current_line = 0
        self.current_offset = 0



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
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 84
                self.match(AsmParser.NEWLINE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self.line_mark()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 73730) != 0:
                self.state = 95
                self.section()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
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
        self.enterRule(localctx, 2, self.RULE_section)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.asect_header()
                self.state = 104
                self.section_body()
                pass
            elif token in [13]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.rsect_header()
                self.state = 107
                self.section_body()
                pass
            elif token in [16]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.tplate_header()
                self.state = 110
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
        self.enterRule(localctx, 4, self.RULE_asect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(AsmParser.Asect)
            self.state = 115
            self.number()
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.match(AsmParser.NEWLINE)
                self.state = 119 
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
        self.enterRule(localctx, 6, self.RULE_rsect_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(AsmParser.Rsect)
            self.state = 122
            self.name()
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 123
                self.match(AsmParser.NEWLINE)
                self.state = 126 
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
        self.enterRule(localctx, 8, self.RULE_tplate_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(AsmParser.Tplate)
            self.state = 129
            self.name()
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.match(AsmParser.NEWLINE)
                self.state = 133 
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
        self.enterRule(localctx, 10, self.RULE_section_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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


        def goto_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsmParser.Goto_statementContext)
            else:
                return self.getTypedRuleContext(AsmParser.Goto_statementContext,i)


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
        self.enterRule(localctx, 12, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 145
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 137
                        self.break_statement()
                        pass

                    elif la_ == 2:
                        self.state = 138
                        self.continue_statement()
                        pass

                    elif la_ == 3:
                        self.state = 139
                        self.line()
                        pass

                    elif la_ == 4:
                        self.state = 140
                        self.conditional()
                        pass

                    elif la_ == 5:
                        self.state = 141
                        self.while_loop()
                        pass

                    elif la_ == 6:
                        self.state = 142
                        self.until_loop()
                        pass

                    elif la_ == 7:
                        self.state = 143
                        self.goto_statement()
                        pass

                    elif la_ == 8:
                        self.state = 144
                        self.line_mark()
                        pass

             
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_line_mark)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 151
            localctx._line_number = self.line_number()
            self.state = 152
            localctx._filepath = self.filepath()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 153
                self.match(AsmParser.WORD)


            self.state = 157 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 156
                self.match(AsmParser.NEWLINE)
                self.state = 159 
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
        self.enterRule(localctx, 16, self.RULE_line_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 18, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
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
        self.enterRule(localctx, 20, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(AsmParser.Break)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.match(AsmParser.NEWLINE)
                self.state = 175 
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
        self.enterRule(localctx, 22, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(AsmParser.Continue)
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.match(AsmParser.NEWLINE)
                self.state = 181 
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


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsmParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StandaloneLabelContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label_declaration(self):
            return self.getTypedRuleContext(AsmParser.Label_declarationContext,0)

        def Ext(self):
            return self.getToken(AsmParser.Ext, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandaloneLabel" ):
                return visitor.visitStandaloneLabel(self)
            else:
                return visitor.visitChildren(self)


    class InstructionLineContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AsmParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruction(self):
            return self.getTypedRuleContext(AsmParser.InstructionContext,0)

        def label_declaration(self):
            return self.getTypedRuleContext(AsmParser.Label_declarationContext,0)

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



    def line(self):

        localctx = AsmParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = AsmParser.StandaloneLabelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.label_declaration()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 184
                    self.match(AsmParser.Ext)


                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 187
                    self.match(AsmParser.NEWLINE)
                    self.state = 190 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==39):
                        break

                pass

            elif la_ == 2:
                localctx = AsmParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 192
                    self.label_declaration()


                self.state = 195
                self.instruction()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 545515372542) != 0:
                    self.state = 196
                    self.arguments()


                self.state = 200 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 199
                    self.match(AsmParser.NEWLINE)
                    self.state = 202 
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


    class Label_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(AsmParser.LabelContext,0)


        def COLON(self):
            return self.getToken(AsmParser.COLON, 0)

        def ANGLE_BRACKET(self):
            return self.getToken(AsmParser.ANGLE_BRACKET, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_label_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel_declaration" ):
                return visitor.visitLabel_declaration(self)
            else:
                return visitor.visitChildren(self)




    def label_declaration(self):

        localctx = AsmParser.Label_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_label_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.label()
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==26 or _la==28):
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
        self.enterRule(localctx, 28, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.argument()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 210
                self.match(AsmParser.COMMA)
                self.state = 211
                self.argument()
                self.state = 216
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
        self.enterRule(localctx, 30, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(AsmParser.If)
            self.state = 219 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 218
                self.match(AsmParser.NEWLINE)
                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 223
            self.conditions()
            self.state = 224
            self.code_block()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 225
                self.else_clause()


            self.state = 228
            self.match(AsmParser.Fi)
            self.state = 230 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 229
                self.match(AsmParser.NEWLINE)
                self.state = 232 
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
        self.enterRule(localctx, 32, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 234
                    self.connective_condition() 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 240
            self.condition()
            self.state = 242 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 241
                self.match(AsmParser.NEWLINE)
                self.state = 244 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 246
                self.match(AsmParser.Then)
                self.state = 248 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 247
                    self.match(AsmParser.NEWLINE)
                    self.state = 250 
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
        self.enterRule(localctx, 34, self.RULE_connective_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.condition()
            self.state = 255
            self.match(AsmParser.COMMA)
            self.state = 256
            self.conjunction()
            self.state = 258 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 257
                self.match(AsmParser.NEWLINE)
                self.state = 260 
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
        self.enterRule(localctx, 36, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.code_block()
            self.state = 263
            self.match(AsmParser.Is)
            self.state = 264
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
        self.enterRule(localctx, 38, self.RULE_else_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(AsmParser.Else)
            self.state = 268 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 267
                self.match(AsmParser.NEWLINE)
                self.state = 270 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 272
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
        self.enterRule(localctx, 40, self.RULE_branch_mnemonic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
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
        self.enterRule(localctx, 42, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
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
        self.enterRule(localctx, 44, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(AsmParser.While)
            self.state = 280 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 279
                self.match(AsmParser.NEWLINE)
                self.state = 282 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 284
            self.while_condition()
            self.state = 285
            self.match(AsmParser.Stays)
            self.state = 286
            self.branch_mnemonic()
            self.state = 288 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 287
                self.match(AsmParser.NEWLINE)
                self.state = 290 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 292
            self.code_block()
            self.state = 293
            self.match(AsmParser.Wend)
            self.state = 295 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 294
                self.match(AsmParser.NEWLINE)
                self.state = 297 
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
        self.enterRule(localctx, 46, self.RULE_while_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
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
        self.enterRule(localctx, 48, self.RULE_until_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(AsmParser.Do)
            self.state = 303 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 302
                self.match(AsmParser.NEWLINE)
                self.state = 305 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 307
            self.code_block()
            self.state = 308
            self.match(AsmParser.Until)
            self.state = 309
            self.branch_mnemonic()
            self.state = 311 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 310
                self.match(AsmParser.NEWLINE)
                self.state = 313 
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


    class Goto_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Goto(self):
            return self.getToken(AsmParser.Goto, 0)

        def branch_mnemonic(self):
            return self.getTypedRuleContext(AsmParser.Branch_mnemonicContext,0)


        def COMMA(self):
            return self.getToken(AsmParser.COMMA, 0)

        def goto_argument(self):
            return self.getTypedRuleContext(AsmParser.Goto_argumentContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AsmParser.NEWLINE)
            else:
                return self.getToken(AsmParser.NEWLINE, i)

        def getRuleIndex(self):
            return AsmParser.RULE_goto_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto_statement" ):
                return visitor.visitGoto_statement(self)
            else:
                return visitor.visitChildren(self)




    def goto_statement(self):

        localctx = AsmParser.Goto_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_goto_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(AsmParser.Goto)
            self.state = 316
            self.branch_mnemonic()
            self.state = 317
            self.match(AsmParser.COMMA)
            self.state = 318
            self.goto_argument()
            self.state = 320 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 319
                self.match(AsmParser.NEWLINE)
                self.state = 322 
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


    class Goto_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addr_expr(self):
            return self.getTypedRuleContext(AsmParser.Addr_exprContext,0)


        def byte_expr(self):
            return self.getTypedRuleContext(AsmParser.Byte_exprContext,0)


        def getRuleIndex(self):
            return AsmParser.RULE_goto_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto_argument" ):
                return visitor.visitGoto_argument(self)
            else:
                return visitor.visitChildren(self)




    def goto_argument(self):

        localctx = AsmParser.Goto_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_goto_argument)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.addr_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.byte_expr()
                pass


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
        self.enterRule(localctx, 54, self.RULE_argument)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 332
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
        self.enterRule(localctx, 56, self.RULE_byte_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.byte_specifier()
            self.state = 336
            self.match(AsmParser.OPEN_PAREN)
            self.state = 337
            self.addr_expr()
            self.state = 338
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
        self.enterRule(localctx, 58, self.RULE_addr_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.first_term()
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 341
                self.add_term()
                self.state = 346
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
        self.enterRule(localctx, 60, self.RULE_first_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24 or _la==25:
                self.state = 347
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 350
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
        self.enterRule(localctx, 62, self.RULE_add_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 353
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
        self.enterRule(localctx, 64, self.RULE_term)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.template_field()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
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

        def Low(self):
            return self.getToken(AsmParser.Low, 0)

        def High(self):
            return self.getToken(AsmParser.High, 0)

        def getRuleIndex(self):
            return AsmParser.RULE_byte_specifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByte_specifier" ):
                return visitor.visitByte_specifier(self)
            else:
                return visitor.visitChildren(self)




    def byte_specifier(self):

        localctx = AsmParser.Byte_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_byte_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
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
        self.enterRule(localctx, 68, self.RULE_template_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.name()
            self.state = 363
            self.match(AsmParser.DOT)
            self.state = 364
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
        self.enterRule(localctx, 70, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
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
        self.enterRule(localctx, 72, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
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
        self.enterRule(localctx, 74, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
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
        self.enterRule(localctx, 76, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
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
        self.enterRule(localctx, 78, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
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
        self.enterRule(localctx, 80, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
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

        def Goto(self):
            return self.getToken(AsmParser.Goto, 0)

        def High(self):
            return self.getToken(AsmParser.High, 0)

        def If(self):
            return self.getToken(AsmParser.If, 0)

        def Is(self):
            return self.getToken(AsmParser.Is, 0)

        def Low(self):
            return self.getToken(AsmParser.Low, 0)

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
        self.enterRule(localctx, 82, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8594128894) != 0):
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





