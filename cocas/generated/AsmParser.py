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
        4,1,42,363,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,5,0,82,8,0,10,0,12,0,85,9,0,1,0,4,0,88,8,0,11,0,12,0,89,1,0,
        5,0,93,8,0,10,0,12,0,96,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,109,8,1,1,2,1,2,1,2,4,2,114,8,2,11,2,12,2,115,1,3,1,
        3,1,3,4,3,121,8,3,11,3,12,3,122,1,4,1,4,1,4,4,4,128,8,4,11,4,12,
        4,129,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,141,8,6,10,6,12,6,
        144,9,6,1,7,1,7,1,7,1,7,3,7,150,8,7,1,7,4,7,153,8,7,11,7,12,7,154,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,4,10,169,8,10,
        11,10,12,10,170,1,11,1,11,4,11,175,8,11,11,11,12,11,176,1,12,1,12,
        3,12,181,8,12,1,12,4,12,184,8,12,11,12,12,12,185,1,12,3,12,189,8,
        12,1,12,1,12,3,12,193,8,12,1,12,4,12,196,8,12,11,12,12,12,197,3,
        12,200,8,12,1,13,1,13,1,13,1,14,1,14,1,14,5,14,208,8,14,10,14,12,
        14,211,9,14,1,15,1,15,4,15,215,8,15,11,15,12,15,216,1,15,1,15,1,
        15,3,15,222,8,15,1,15,1,15,4,15,226,8,15,11,15,12,15,227,1,16,5,
        16,231,8,16,10,16,12,16,234,9,16,1,16,1,16,4,16,238,8,16,11,16,12,
        16,239,1,16,1,16,4,16,244,8,16,11,16,12,16,245,3,16,248,8,16,1,17,
        1,17,1,17,1,17,4,17,254,8,17,11,17,12,17,255,1,18,1,18,1,18,1,18,
        1,19,1,19,4,19,264,8,19,11,19,12,19,265,1,19,1,19,1,20,1,20,1,21,
        1,21,1,22,1,22,4,22,276,8,22,11,22,12,22,277,1,22,1,22,1,22,1,22,
        4,22,284,8,22,11,22,12,22,285,1,22,1,22,1,22,4,22,291,8,22,11,22,
        12,22,292,1,23,1,23,1,24,1,24,4,24,299,8,24,11,24,12,24,300,1,24,
        1,24,1,24,1,24,4,24,307,8,24,11,24,12,24,308,1,25,1,25,1,25,1,25,
        1,25,3,25,316,8,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,5,27,325,8,
        27,10,27,12,27,328,9,27,1,28,3,28,331,8,28,1,28,1,28,1,29,1,29,1,
        29,1,30,1,30,1,30,3,30,341,8,30,1,31,1,31,1,32,1,32,1,32,1,32,1,
        33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,
        39,1,39,0,0,40,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        0,5,2,0,25,25,27,27,1,0,23,24,1,0,19,20,1,0,33,35,2,0,1,20,32,32,
        370,0,83,1,0,0,0,2,108,1,0,0,0,4,110,1,0,0,0,6,117,1,0,0,0,8,124,
        1,0,0,0,10,131,1,0,0,0,12,142,1,0,0,0,14,145,1,0,0,0,16,162,1,0,
        0,0,18,164,1,0,0,0,20,166,1,0,0,0,22,172,1,0,0,0,24,199,1,0,0,0,
        26,201,1,0,0,0,28,204,1,0,0,0,30,212,1,0,0,0,32,232,1,0,0,0,34,249,
        1,0,0,0,36,257,1,0,0,0,38,261,1,0,0,0,40,269,1,0,0,0,42,271,1,0,
        0,0,44,273,1,0,0,0,46,294,1,0,0,0,48,296,1,0,0,0,50,315,1,0,0,0,
        52,317,1,0,0,0,54,322,1,0,0,0,56,330,1,0,0,0,58,334,1,0,0,0,60,340,
        1,0,0,0,62,342,1,0,0,0,64,344,1,0,0,0,66,348,1,0,0,0,68,350,1,0,
        0,0,70,352,1,0,0,0,72,354,1,0,0,0,74,356,1,0,0,0,76,358,1,0,0,0,
        78,360,1,0,0,0,80,82,5,38,0,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,
        1,0,0,0,83,84,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,86,88,3,14,7,0,
        87,86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,94,1,
        0,0,0,91,93,3,2,1,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,
        95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,6,0,0,98,1,1,0,0,
        0,99,100,3,4,2,0,100,101,3,10,5,0,101,109,1,0,0,0,102,103,3,6,3,
        0,103,104,3,10,5,0,104,109,1,0,0,0,105,106,3,8,4,0,106,107,3,10,
        5,0,107,109,1,0,0,0,108,99,1,0,0,0,108,102,1,0,0,0,108,105,1,0,0,
        0,109,3,1,0,0,0,110,111,5,1,0,0,111,113,3,76,38,0,112,114,5,38,0,
        0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,
        0,116,5,1,0,0,0,117,118,5,12,0,0,118,120,3,78,39,0,119,121,5,38,
        0,0,120,119,1,0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,122,123,1,0,
        0,0,123,7,1,0,0,0,124,125,5,15,0,0,125,127,3,78,39,0,126,128,5,38,
        0,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,1,0,0,0,129,130,1,0,
        0,0,130,9,1,0,0,0,131,132,3,12,6,0,132,11,1,0,0,0,133,141,3,20,10,
        0,134,141,3,22,11,0,135,141,3,24,12,0,136,141,3,30,15,0,137,141,
        3,44,22,0,138,141,3,48,24,0,139,141,3,14,7,0,140,133,1,0,0,0,140,
        134,1,0,0,0,140,135,1,0,0,0,140,136,1,0,0,0,140,137,1,0,0,0,140,
        138,1,0,0,0,140,139,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,
        143,1,0,0,0,143,13,1,0,0,0,144,142,1,0,0,0,145,146,5,30,0,0,146,
        147,3,16,8,0,147,149,3,18,9,0,148,150,5,32,0,0,149,148,1,0,0,0,149,
        150,1,0,0,0,150,152,1,0,0,0,151,153,5,38,0,0,152,151,1,0,0,0,153,
        154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,
        157,6,7,-1,0,157,158,6,7,-1,0,158,159,6,7,-1,0,159,160,6,7,-1,0,
        160,161,6,7,-1,0,161,15,1,0,0,0,162,163,5,33,0,0,163,17,1,0,0,0,
        164,165,5,41,0,0,165,19,1,0,0,0,166,168,5,2,0,0,167,169,5,38,0,0,
        168,167,1,0,0,0,169,170,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,
        171,21,1,0,0,0,172,174,5,3,0,0,173,175,5,38,0,0,174,173,1,0,0,0,
        175,176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,23,1,0,0,0,178,
        180,3,26,13,0,179,181,5,7,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,
        183,1,0,0,0,182,184,5,38,0,0,183,182,1,0,0,0,184,185,1,0,0,0,185,
        183,1,0,0,0,185,186,1,0,0,0,186,200,1,0,0,0,187,189,3,26,13,0,188,
        187,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,192,3,68,34,0,191,
        193,3,28,14,0,192,191,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,
        196,5,38,0,0,195,194,1,0,0,0,196,197,1,0,0,0,197,195,1,0,0,0,197,
        198,1,0,0,0,198,200,1,0,0,0,199,178,1,0,0,0,199,188,1,0,0,0,200,
        25,1,0,0,0,201,202,3,66,33,0,202,203,7,0,0,0,203,27,1,0,0,0,204,
        209,3,50,25,0,205,206,5,22,0,0,206,208,3,50,25,0,207,205,1,0,0,0,
        208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,29,1,0,0,0,211,
        209,1,0,0,0,212,214,5,9,0,0,213,215,5,38,0,0,214,213,1,0,0,0,215,
        216,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,
        219,3,32,16,0,219,221,3,12,6,0,220,222,3,38,19,0,221,220,1,0,0,0,
        221,222,1,0,0,0,222,223,1,0,0,0,223,225,5,8,0,0,224,226,5,38,0,0,
        225,224,1,0,0,0,226,227,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,
        228,31,1,0,0,0,229,231,3,34,17,0,230,229,1,0,0,0,231,234,1,0,0,0,
        232,230,1,0,0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,1,0,0,0,
        235,237,3,36,18,0,236,238,5,38,0,0,237,236,1,0,0,0,238,239,1,0,0,
        0,239,237,1,0,0,0,239,240,1,0,0,0,240,247,1,0,0,0,241,243,5,14,0,
        0,242,244,5,38,0,0,243,242,1,0,0,0,244,245,1,0,0,0,245,243,1,0,0,
        0,245,246,1,0,0,0,246,248,1,0,0,0,247,241,1,0,0,0,247,248,1,0,0,
        0,248,33,1,0,0,0,249,250,3,36,18,0,250,251,5,22,0,0,251,253,3,42,
        21,0,252,254,5,38,0,0,253,252,1,0,0,0,254,255,1,0,0,0,255,253,1,
        0,0,0,255,256,1,0,0,0,256,35,1,0,0,0,257,258,3,12,6,0,258,259,5,
        10,0,0,259,260,3,40,20,0,260,37,1,0,0,0,261,263,5,5,0,0,262,264,
        5,38,0,0,263,262,1,0,0,0,264,265,1,0,0,0,265,263,1,0,0,0,265,266,
        1,0,0,0,266,267,1,0,0,0,267,268,3,12,6,0,268,39,1,0,0,0,269,270,
        5,32,0,0,270,41,1,0,0,0,271,272,5,32,0,0,272,43,1,0,0,0,273,275,
        5,18,0,0,274,276,5,38,0,0,275,274,1,0,0,0,276,277,1,0,0,0,277,275,
        1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,280,3,46,23,0,280,281,
        5,13,0,0,281,283,3,40,20,0,282,284,5,38,0,0,283,282,1,0,0,0,284,
        285,1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,287,1,0,0,0,287,
        288,3,12,6,0,288,290,5,17,0,0,289,291,5,38,0,0,290,289,1,0,0,0,291,
        292,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,45,1,0,0,0,294,295,
        3,12,6,0,295,47,1,0,0,0,296,298,5,4,0,0,297,299,5,38,0,0,298,297,
        1,0,0,0,299,300,1,0,0,0,300,298,1,0,0,0,300,301,1,0,0,0,301,302,
        1,0,0,0,302,303,3,12,6,0,303,304,5,16,0,0,304,306,3,40,20,0,305,
        307,5,38,0,0,306,305,1,0,0,0,307,308,1,0,0,0,308,306,1,0,0,0,308,
        309,1,0,0,0,309,49,1,0,0,0,310,316,3,74,37,0,311,316,3,70,35,0,312,
        316,3,72,36,0,313,316,3,54,27,0,314,316,3,52,26,0,315,310,1,0,0,
        0,315,311,1,0,0,0,315,312,1,0,0,0,315,313,1,0,0,0,315,314,1,0,0,
        0,316,51,1,0,0,0,317,318,3,62,31,0,318,319,5,28,0,0,319,320,3,54,
        27,0,320,321,5,29,0,0,321,53,1,0,0,0,322,326,3,56,28,0,323,325,3,
        58,29,0,324,323,1,0,0,0,325,328,1,0,0,0,326,324,1,0,0,0,326,327,
        1,0,0,0,327,55,1,0,0,0,328,326,1,0,0,0,329,331,7,1,0,0,330,329,1,
        0,0,0,330,331,1,0,0,0,331,332,1,0,0,0,332,333,3,60,30,0,333,57,1,
        0,0,0,334,335,7,1,0,0,335,336,3,60,30,0,336,59,1,0,0,0,337,341,3,
        76,38,0,338,341,3,64,32,0,339,341,3,66,33,0,340,337,1,0,0,0,340,
        338,1,0,0,0,340,339,1,0,0,0,341,61,1,0,0,0,342,343,7,2,0,0,343,63,
        1,0,0,0,344,345,3,78,39,0,345,346,5,21,0,0,346,347,3,78,39,0,347,
        65,1,0,0,0,348,349,3,78,39,0,349,67,1,0,0,0,350,351,5,32,0,0,351,
        69,1,0,0,0,352,353,5,36,0,0,353,71,1,0,0,0,354,355,5,31,0,0,355,
        73,1,0,0,0,356,357,5,37,0,0,357,75,1,0,0,0,358,359,7,3,0,0,359,77,
        1,0,0,0,360,361,7,4,0,0,361,79,1,0,0,0,38,83,89,94,108,115,122,129,
        140,142,149,154,170,176,180,185,188,192,197,199,209,216,221,227,
        232,239,245,247,255,265,277,285,292,300,308,315,326,330,340
    ]

class AsmParser ( Parser ):

    grammarFileName = "AsmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'asect'", "'break'", "'continue'", "'do'", 
                     "'else'", "'end'", "'ext'", "'fi'", "'if'", "'is'", 
                     "'macro'", "'rsect'", "'stays'", "'then'", "'tplate'", 
                     "'until'", "'wend'", "'while'", "'low'", "'high'", 
                     "'.'", "','", "'+'", "'-'", "':'", "'*'", "'>'", "'('", 
                     "')'", "'-|'" ]

    symbolicNames = [ "<INVALID>", "Asect", "Break", "Continue", "Do", "Else", 
                      "End", "Ext", "Fi", "If", "Is", "Macro", "Rsect", 
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
    RULE_argument = 25
    RULE_byte_expr = 26
    RULE_addr_expr = 27
    RULE_first_term = 28
    RULE_add_term = 29
    RULE_term = 30
    RULE_byte_specifier = 31
    RULE_template_field = 32
    RULE_label = 33
    RULE_instruction = 34
    RULE_string = 35
    RULE_register = 36
    RULE_character = 37
    RULE_number = 38
    RULE_name = 39

    ruleNames =  [ "program", "section", "asect_header", "rsect_header", 
                   "tplate_header", "section_body", "code_block", "line_mark", 
                   "line_number", "filepath", "break_statement", "continue_statement", 
                   "line", "label_declaration", "arguments", "conditional", 
                   "conditions", "connective_condition", "condition", "else_clause", 
                   "branch_mnemonic", "conjunction", "while_loop", "while_condition", 
                   "until_loop", "argument", "byte_expr", "addr_expr", "first_term", 
                   "add_term", "term", "byte_specifier", "template_field", 
                   "label", "instruction", "string", "register", "character", 
                   "number", "name" ]

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
    Low=19
    High=20
    DOT=21
    COMMA=22
    PLUS=23
    MINUS=24
    COLON=25
    ASTERISK=26
    ANGLE_BRACKET=27
    OPEN_PAREN=28
    CLOSE_PAREN=29
    LINE_MARK_MARKER=30
    REGISTER=31
    WORD=32
    DECIMAL_NUMBER=33
    BINARY_NUMBER=34
    HEX_NUMBER=35
    STRING=36
    CHAR=37
    NEWLINE=38
    COMMENT=39
    WS=40
    BASE64=41
    UNEXPECTED_TOKEN=42

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
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 80
                self.match(AsmParser.NEWLINE)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.line_mark()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==30):
                    break

            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 36866) != 0:
                self.state = 91
                self.section()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = AsmParser.AbsoluteSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.asect_header()
                self.state = 100
                self.section_body()
                pass
            elif token in [12]:
                localctx = AsmParser.RelocatableSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.rsect_header()
                self.state = 103
                self.section_body()
                pass
            elif token in [15]:
                localctx = AsmParser.TemplateSectionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.tplate_header()
                self.state = 106
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
            self.state = 110
            self.match(AsmParser.Asect)
            self.state = 111
            self.number()
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.match(AsmParser.NEWLINE)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 117
            self.match(AsmParser.Rsect)
            self.state = 118
            self.name()
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.match(AsmParser.NEWLINE)
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 124
            self.match(AsmParser.Tplate)
            self.state = 125
            self.name()
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.match(AsmParser.NEWLINE)
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 131
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
        self.enterRule(localctx, 12, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 133
                        self.break_statement()
                        pass

                    elif la_ == 2:
                        self.state = 134
                        self.continue_statement()
                        pass

                    elif la_ == 3:
                        self.state = 135
                        self.line()
                        pass

                    elif la_ == 4:
                        self.state = 136
                        self.conditional()
                        pass

                    elif la_ == 5:
                        self.state = 137
                        self.while_loop()
                        pass

                    elif la_ == 6:
                        self.state = 138
                        self.until_loop()
                        pass

                    elif la_ == 7:
                        self.state = 139
                        self.line_mark()
                        pass

             
                self.state = 144
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
            self.state = 145
            self.match(AsmParser.LINE_MARK_MARKER)
            self.state = 146
            localctx._line_number = self.line_number()
            self.state = 147
            localctx._filepath = self.filepath()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 148
                self.match(AsmParser.WORD)


            self.state = 152 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 151
                self.match(AsmParser.NEWLINE)
                self.state = 154 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 162
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
            self.state = 164
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
            self.state = 166
            self.match(AsmParser.Break)
            self.state = 168 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.match(AsmParser.NEWLINE)
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 172
            self.match(AsmParser.Continue)
            self.state = 174 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 173
                self.match(AsmParser.NEWLINE)
                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = AsmParser.StandaloneLabelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.label_declaration()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 179
                    self.match(AsmParser.Ext)


                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 182
                    self.match(AsmParser.NEWLINE)
                    self.state = 185 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
                        break

                pass

            elif la_ == 2:
                localctx = AsmParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 187
                    self.label_declaration()


                self.state = 190
                self.instruction()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 272757686270) != 0:
                    self.state = 191
                    self.arguments()


                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 194
                    self.match(AsmParser.NEWLINE)
                    self.state = 197 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
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
            self.state = 201
            self.label()
            self.state = 202
            _la = self._input.LA(1)
            if not(_la==25 or _la==27):
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
            self.state = 204
            self.argument()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 205
                self.match(AsmParser.COMMA)
                self.state = 206
                self.argument()
                self.state = 211
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
            self.state = 212
            self.match(AsmParser.If)
            self.state = 214 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 213
                self.match(AsmParser.NEWLINE)
                self.state = 216 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 218
            self.conditions()
            self.state = 219
            self.code_block()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 220
                self.else_clause()


            self.state = 223
            self.match(AsmParser.Fi)
            self.state = 225 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 224
                self.match(AsmParser.NEWLINE)
                self.state = 227 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 229
                    self.connective_condition() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 235
            self.condition()
            self.state = 237 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 236
                self.match(AsmParser.NEWLINE)
                self.state = 239 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(AsmParser.Then)
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 242
                    self.match(AsmParser.NEWLINE)
                    self.state = 245 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==38):
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
            self.state = 249
            self.condition()
            self.state = 250
            self.match(AsmParser.COMMA)
            self.state = 251
            self.conjunction()
            self.state = 253 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 252
                self.match(AsmParser.NEWLINE)
                self.state = 255 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 257
            self.code_block()
            self.state = 258
            self.match(AsmParser.Is)
            self.state = 259
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
            self.state = 261
            self.match(AsmParser.Else)
            self.state = 263 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 262
                self.match(AsmParser.NEWLINE)
                self.state = 265 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 267
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
            self.state = 269
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
            self.state = 271
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
            self.state = 273
            self.match(AsmParser.While)
            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 274
                self.match(AsmParser.NEWLINE)
                self.state = 277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 279
            self.while_condition()
            self.state = 280
            self.match(AsmParser.Stays)
            self.state = 281
            self.branch_mnemonic()
            self.state = 283 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 282
                self.match(AsmParser.NEWLINE)
                self.state = 285 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 287
            self.code_block()
            self.state = 288
            self.match(AsmParser.Wend)
            self.state = 290 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 289
                self.match(AsmParser.NEWLINE)
                self.state = 292 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
            self.state = 294
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
            self.state = 296
            self.match(AsmParser.Do)
            self.state = 298 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 297
                self.match(AsmParser.NEWLINE)
                self.state = 300 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

            self.state = 302
            self.code_block()
            self.state = 303
            self.match(AsmParser.Until)
            self.state = 304
            self.branch_mnemonic()
            self.state = 306 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 305
                self.match(AsmParser.NEWLINE)
                self.state = 308 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
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
        self.enterRule(localctx, 50, self.RULE_argument)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.character()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.register()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.addr_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
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
        self.enterRule(localctx, 52, self.RULE_byte_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.byte_specifier()
            self.state = 318
            self.match(AsmParser.OPEN_PAREN)
            self.state = 319
            self.addr_expr()
            self.state = 320
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
        self.enterRule(localctx, 54, self.RULE_addr_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.first_term()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 323
                self.add_term()
                self.state = 328
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
        self.enterRule(localctx, 56, self.RULE_first_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23 or _la==24:
                self.state = 329
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 332
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
        self.enterRule(localctx, 58, self.RULE_add_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 335
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
        self.enterRule(localctx, 60, self.RULE_term)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.template_field()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
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
        self.enterRule(localctx, 62, self.RULE_byte_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
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
        self.enterRule(localctx, 64, self.RULE_template_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.name()
            self.state = 345
            self.match(AsmParser.DOT)
            self.state = 346
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
        self.enterRule(localctx, 66, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
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
        self.enterRule(localctx, 68, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
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
        self.enterRule(localctx, 70, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
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
        self.enterRule(localctx, 72, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
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
        self.enterRule(localctx, 74, self.RULE_character)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
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
        self.enterRule(localctx, 76, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0):
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
        self.enterRule(localctx, 78, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 4297064446) != 0):
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





