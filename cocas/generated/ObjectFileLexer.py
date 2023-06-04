# Generated from ./grammar/ObjectFile.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,76,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,4,6,55,8,6,11,6,12,6,56,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,3,10,69,8,10,1,10,1,10,1,
        11,1,11,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,
        19,10,21,11,23,12,1,0,2,4,0,48,57,65,90,95,95,97,122,2,0,9,9,32,
        32,77,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,29,1,0,0,0,5,34,1,0,0,
        0,7,39,1,0,0,0,9,44,1,0,0,0,11,48,1,0,0,0,13,54,1,0,0,0,15,58,1,
        0,0,0,17,63,1,0,0,0,19,65,1,0,0,0,21,68,1,0,0,0,23,72,1,0,0,0,25,
        26,5,65,0,0,26,27,5,66,0,0,27,28,5,83,0,0,28,2,1,0,0,0,29,30,5,78,
        0,0,30,31,5,84,0,0,31,32,5,82,0,0,32,33,5,89,0,0,33,4,1,0,0,0,34,
        35,5,78,0,0,35,36,5,65,0,0,36,37,5,77,0,0,37,38,5,69,0,0,38,6,1,
        0,0,0,39,40,5,68,0,0,40,41,5,65,0,0,41,42,5,84,0,0,42,43,5,65,0,
        0,43,8,1,0,0,0,44,45,5,82,0,0,45,46,5,69,0,0,46,47,5,76,0,0,47,10,
        1,0,0,0,48,49,5,88,0,0,49,50,5,84,0,0,50,51,5,82,0,0,51,52,5,78,
        0,0,52,12,1,0,0,0,53,55,7,0,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,
        1,0,0,0,56,57,1,0,0,0,57,14,1,0,0,0,58,59,5,36,0,0,59,60,5,97,0,
        0,60,61,5,98,0,0,61,62,5,115,0,0,62,16,1,0,0,0,63,64,5,58,0,0,64,
        18,1,0,0,0,65,66,5,45,0,0,66,20,1,0,0,0,67,69,5,13,0,0,68,67,1,0,
        0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,10,0,0,71,22,1,0,0,0,72,
        73,7,1,0,0,73,74,1,0,0,0,74,75,6,11,0,0,75,24,1,0,0,0,3,0,56,68,
        1,6,0,0
    ]

class ObjectFileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ABS = 1
    NTRY = 2
    NAME = 3
    DATA = 4
    REL = 5
    XTRN = 6
    WORD = 7
    ABS_SECTION = 8
    COLON = 9
    MINUS = 10
    NEWLINE = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ABS'", "'NTRY'", "'NAME'", "'DATA'", "'REL'", "'XTRN'", "'$abs'", 
            "':'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ABS", "NTRY", "NAME", "DATA", "REL", "XTRN", "WORD", "ABS_SECTION", 
            "COLON", "MINUS", "NEWLINE", "WS" ]

    ruleNames = [ "ABS", "NTRY", "NAME", "DATA", "REL", "XTRN", "WORD", 
                  "ABS_SECTION", "COLON", "MINUS", "NEWLINE", "WS" ]

    grammarFileName = "ObjectFile.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


