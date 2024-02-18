# Generated from object_file/grammar/ObjectFileLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,24,184,6,-1,6,-1,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,
        7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,
        11,7,11,2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,
        17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,10,4,10,108,8,10,11,10,12,10,109,1,11,1,11,1,
        11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,3,15,124,8,15,1,
        15,4,15,127,8,15,11,15,12,15,128,1,16,4,16,132,8,16,11,16,12,16,
        133,1,16,1,16,1,17,3,17,139,8,17,1,17,4,17,142,8,17,11,17,12,17,
        143,1,17,1,17,1,18,4,18,149,8,18,11,18,12,18,150,1,19,4,19,154,8,
        19,11,19,12,19,155,1,20,4,20,159,8,20,11,20,12,20,160,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,22,4,22,171,8,22,11,22,12,22,172,1,22,
        1,22,1,22,1,23,4,23,179,8,23,11,23,12,23,180,1,23,1,23,0,0,24,5,
        1,7,2,9,3,11,4,13,5,15,6,17,7,19,8,21,9,23,10,25,11,27,12,29,13,
        31,14,33,15,35,16,37,17,39,18,41,19,43,20,45,21,47,22,49,23,51,24,
        5,0,1,2,3,4,4,4,0,48,57,65,90,95,95,97,122,2,0,9,9,32,32,6,0,9,9,
        32,32,48,57,65,90,95,95,97,122,2,0,10,10,13,13,190,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,
        1,0,0,0,1,39,1,0,0,0,1,41,1,0,0,0,2,43,1,0,0,0,2,45,1,0,0,0,2,47,
        1,0,0,0,3,49,1,0,0,0,4,51,1,0,0,0,5,53,1,0,0,0,7,58,1,0,0,0,9,65,
        1,0,0,0,11,71,1,0,0,0,13,75,1,0,0,0,15,80,1,0,0,0,17,85,1,0,0,0,
        19,90,1,0,0,0,21,97,1,0,0,0,23,101,1,0,0,0,25,107,1,0,0,0,27,111,
        1,0,0,0,29,116,1,0,0,0,31,118,1,0,0,0,33,120,1,0,0,0,35,126,1,0,
        0,0,37,131,1,0,0,0,39,141,1,0,0,0,41,148,1,0,0,0,43,153,1,0,0,0,
        45,158,1,0,0,0,47,164,1,0,0,0,49,170,1,0,0,0,51,178,1,0,0,0,53,54,
        5,84,0,0,54,55,5,65,0,0,55,56,5,82,0,0,56,57,5,71,0,0,57,6,1,0,0,
        0,58,59,5,70,0,0,59,60,5,73,0,0,60,61,5,76,0,0,61,62,5,69,0,0,62,
        63,1,0,0,0,63,64,6,1,0,0,64,8,1,0,0,0,65,66,5,65,0,0,66,67,5,66,
        0,0,67,68,5,83,0,0,68,69,1,0,0,0,69,70,6,2,1,0,70,10,1,0,0,0,71,
        72,5,76,0,0,72,73,5,79,0,0,73,74,5,67,0,0,74,12,1,0,0,0,75,76,5,
        78,0,0,76,77,5,84,0,0,77,78,5,82,0,0,78,79,5,89,0,0,79,14,1,0,0,
        0,80,81,5,78,0,0,81,82,5,65,0,0,82,83,5,77,0,0,83,84,5,69,0,0,84,
        16,1,0,0,0,85,86,5,65,0,0,86,87,5,76,0,0,87,88,5,73,0,0,88,89,5,
        71,0,0,89,18,1,0,0,0,90,91,5,68,0,0,91,92,5,65,0,0,92,93,5,84,0,
        0,93,94,5,65,0,0,94,95,1,0,0,0,95,96,6,7,2,0,96,20,1,0,0,0,97,98,
        5,82,0,0,98,99,5,69,0,0,99,100,5,76,0,0,100,22,1,0,0,0,101,102,5,
        88,0,0,102,103,5,84,0,0,103,104,5,82,0,0,104,105,5,78,0,0,105,24,
        1,0,0,0,106,108,7,0,0,0,107,106,1,0,0,0,108,109,1,0,0,0,109,107,
        1,0,0,0,109,110,1,0,0,0,110,26,1,0,0,0,111,112,5,36,0,0,112,113,
        5,97,0,0,113,114,5,98,0,0,114,115,5,115,0,0,115,28,1,0,0,0,116,117,
        5,58,0,0,117,30,1,0,0,0,118,119,5,45,0,0,119,32,1,0,0,0,120,121,
        5,43,0,0,121,34,1,0,0,0,122,124,5,13,0,0,123,122,1,0,0,0,123,124,
        1,0,0,0,124,125,1,0,0,0,125,127,5,10,0,0,126,123,1,0,0,0,127,128,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,36,1,0,0,0,130,132,7,
        1,0,0,131,130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,
        0,0,0,134,135,1,0,0,0,135,136,6,16,3,0,136,38,1,0,0,0,137,139,5,
        13,0,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,142,5,
        10,0,0,141,138,1,0,0,0,142,143,1,0,0,0,143,141,1,0,0,0,143,144,1,
        0,0,0,144,145,1,0,0,0,145,146,6,17,4,0,146,40,1,0,0,0,147,149,7,
        2,0,0,148,147,1,0,0,0,149,150,1,0,0,0,150,148,1,0,0,0,150,151,1,
        0,0,0,151,42,1,0,0,0,152,154,7,0,0,0,153,152,1,0,0,0,154,155,1,0,
        0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,44,1,0,0,0,157,159,7,1,0,
        0,158,157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,
        0,161,162,1,0,0,0,162,163,6,20,3,0,163,46,1,0,0,0,164,165,5,58,0,
        0,165,166,1,0,0,0,166,167,6,21,4,0,167,168,6,21,2,0,168,48,1,0,0,
        0,169,171,5,32,0,0,170,169,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,
        0,172,173,1,0,0,0,173,174,1,0,0,0,174,175,6,22,4,0,175,176,6,22,
        5,0,176,50,1,0,0,0,177,179,8,3,0,0,178,177,1,0,0,0,179,180,1,0,0,
        0,180,178,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,6,23,4,
        0,183,52,1,0,0,0,16,0,1,2,3,4,109,123,128,133,138,143,150,155,160,
        172,180,6,5,3,0,5,2,0,5,1,0,6,0,0,4,0,0,5,4,0
    ]

class ObjectFileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IN_BYTES = 1
    IN_ABS = 2
    IN_FILE = 3
    IN_FILEPATH = 4

    TARG = 1
    FILE = 2
    ABS = 3
    LOC = 4
    NTRY = 5
    NAME = 6
    ALIG = 7
    DATA = 8
    REL = 9
    XTRN = 10
    WORD = 11
    ABS_SECTION = 12
    COLON = 13
    MINUS = 14
    PLUS = 15
    NEWLINE = 16
    WS = 17
    NEWLINE_BYTES = 18
    BYTES = 19
    WORD_ABS = 20
    WS_ABS = 21
    COLON_ABS = 22
    SPACES_FILE = 23
    FILEPATH = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "IN_BYTES", "IN_ABS", "IN_FILE", "IN_FILEPATH" ]

    literalNames = [ "<INVALID>",
            "'TARG'", "'FILE'", "'ABS'", "'LOC'", "'NTRY'", "'NAME'", "'ALIG'", 
            "'DATA'", "'REL'", "'XTRN'", "'$abs'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "TARG", "FILE", "ABS", "LOC", "NTRY", "NAME", "ALIG", "DATA", 
            "REL", "XTRN", "WORD", "ABS_SECTION", "COLON", "MINUS", "PLUS", 
            "NEWLINE", "WS", "NEWLINE_BYTES", "BYTES", "WORD_ABS", "WS_ABS", 
            "COLON_ABS", "SPACES_FILE", "FILEPATH" ]

    ruleNames = [ "TARG", "FILE", "ABS", "LOC", "NTRY", "NAME", "ALIG", 
                  "DATA", "REL", "XTRN", "WORD", "ABS_SECTION", "COLON", 
                  "MINUS", "PLUS", "NEWLINE", "WS", "NEWLINE_BYTES", "BYTES", 
                  "WORD_ABS", "WS_ABS", "COLON_ABS", "SPACES_FILE", "FILEPATH" ]

    grammarFileName = "ObjectFileLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


