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
        4,0,11,72,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,6,4,6,53,8,6,11,6,12,6,54,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,9,3,9,65,8,9,1,9,1,9,1,10,1,10,1,10,1,10,0,0,11,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,2,4,0,48,
        57,65,90,95,95,97,122,2,0,9,9,32,32,73,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,27,
        1,0,0,0,5,32,1,0,0,0,7,37,1,0,0,0,9,42,1,0,0,0,11,46,1,0,0,0,13,
        52,1,0,0,0,15,56,1,0,0,0,17,61,1,0,0,0,19,64,1,0,0,0,21,68,1,0,0,
        0,23,24,5,65,0,0,24,25,5,66,0,0,25,26,5,83,0,0,26,2,1,0,0,0,27,28,
        5,78,0,0,28,29,5,84,0,0,29,30,5,82,0,0,30,31,5,89,0,0,31,4,1,0,0,
        0,32,33,5,78,0,0,33,34,5,65,0,0,34,35,5,77,0,0,35,36,5,69,0,0,36,
        6,1,0,0,0,37,38,5,68,0,0,38,39,5,65,0,0,39,40,5,84,0,0,40,41,5,65,
        0,0,41,8,1,0,0,0,42,43,5,82,0,0,43,44,5,69,0,0,44,45,5,76,0,0,45,
        10,1,0,0,0,46,47,5,88,0,0,47,48,5,84,0,0,48,49,5,82,0,0,49,50,5,
        78,0,0,50,12,1,0,0,0,51,53,7,0,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,
        52,1,0,0,0,54,55,1,0,0,0,55,14,1,0,0,0,56,57,5,36,0,0,57,58,5,97,
        0,0,58,59,5,98,0,0,59,60,5,115,0,0,60,16,1,0,0,0,61,62,5,58,0,0,
        62,18,1,0,0,0,63,65,5,13,0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,66,1,
        0,0,0,66,67,5,10,0,0,67,20,1,0,0,0,68,69,7,1,0,0,69,70,1,0,0,0,70,
        71,6,10,0,0,71,22,1,0,0,0,3,0,54,64,1,6,0,0
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
    NEWLINE = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ABS'", "'NTRY'", "'NAME'", "'DATA'", "'REL'", "'XTRN'", "'$abs'", 
            "':'" ]

    symbolicNames = [ "<INVALID>",
            "ABS", "NTRY", "NAME", "DATA", "REL", "XTRN", "WORD", "ABS_SECTION", 
            "COLON", "NEWLINE", "WS" ]

    ruleNames = [ "ABS", "NTRY", "NAME", "DATA", "REL", "XTRN", "WORD", 
                  "ABS_SECTION", "COLON", "NEWLINE", "WS" ]

    grammarFileName = "ObjectFile.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


