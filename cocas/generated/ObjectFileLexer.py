# Generated from ./grammar/ObjectFile.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,17,114,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,4,10,84,8,10,11,10,12,10,
        85,1,11,1,11,1,11,1,11,1,11,4,11,93,8,11,11,11,12,11,94,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,3,15,107,8,15,1,15,1,15,
        1,16,1,16,1,16,1,16,0,0,17,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,1,0,3,4,0,48,57,
        65,90,95,95,97,122,5,0,43,43,47,57,61,61,65,90,97,122,2,0,9,9,32,
        32,116,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,
        0,0,31,1,0,0,0,0,33,1,0,0,0,1,35,1,0,0,0,3,40,1,0,0,0,5,45,1,0,0,
        0,7,49,1,0,0,0,9,53,1,0,0,0,11,58,1,0,0,0,13,63,1,0,0,0,15,68,1,
        0,0,0,17,73,1,0,0,0,19,77,1,0,0,0,21,83,1,0,0,0,23,87,1,0,0,0,25,
        96,1,0,0,0,27,101,1,0,0,0,29,103,1,0,0,0,31,106,1,0,0,0,33,110,1,
        0,0,0,35,36,5,84,0,0,36,37,5,65,0,0,37,38,5,82,0,0,38,39,5,71,0,
        0,39,2,1,0,0,0,40,41,5,70,0,0,41,42,5,73,0,0,42,43,5,76,0,0,43,44,
        5,69,0,0,44,4,1,0,0,0,45,46,5,65,0,0,46,47,5,66,0,0,47,48,5,83,0,
        0,48,6,1,0,0,0,49,50,5,76,0,0,50,51,5,79,0,0,51,52,5,67,0,0,52,8,
        1,0,0,0,53,54,5,78,0,0,54,55,5,84,0,0,55,56,5,82,0,0,56,57,5,89,
        0,0,57,10,1,0,0,0,58,59,5,78,0,0,59,60,5,65,0,0,60,61,5,77,0,0,61,
        62,5,69,0,0,62,12,1,0,0,0,63,64,5,65,0,0,64,65,5,76,0,0,65,66,5,
        73,0,0,66,67,5,71,0,0,67,14,1,0,0,0,68,69,5,68,0,0,69,70,5,65,0,
        0,70,71,5,84,0,0,71,72,5,65,0,0,72,16,1,0,0,0,73,74,5,82,0,0,74,
        75,5,69,0,0,75,76,5,76,0,0,76,18,1,0,0,0,77,78,5,88,0,0,78,79,5,
        84,0,0,79,80,5,82,0,0,80,81,5,78,0,0,81,20,1,0,0,0,82,84,7,0,0,0,
        83,82,1,0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,22,1,
        0,0,0,87,88,5,102,0,0,88,89,5,112,0,0,89,90,5,45,0,0,90,92,1,0,0,
        0,91,93,7,1,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,
        1,0,0,0,95,24,1,0,0,0,96,97,5,36,0,0,97,98,5,97,0,0,98,99,5,98,0,
        0,99,100,5,115,0,0,100,26,1,0,0,0,101,102,5,58,0,0,102,28,1,0,0,
        0,103,104,5,45,0,0,104,30,1,0,0,0,105,107,5,13,0,0,106,105,1,0,0,
        0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,5,10,0,0,109,32,1,0,0,
        0,110,111,7,2,0,0,111,112,1,0,0,0,112,113,6,16,0,0,113,34,1,0,0,
        0,4,0,85,94,106,1,6,0,0
    ]

class ObjectFileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

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
    FP_BASE64 = 12
    ABS_SECTION = 13
    COLON = 14
    MINUS = 15
    NEWLINE = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'TARG'", "'FILE'", "'ABS'", "'LOC'", "'NTRY'", "'NAME'", "'ALIG'", 
            "'DATA'", "'REL'", "'XTRN'", "'$abs'", "':'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "TARG", "FILE", "ABS", "LOC", "NTRY", "NAME", "ALIG", "DATA", 
            "REL", "XTRN", "WORD", "FP_BASE64", "ABS_SECTION", "COLON", 
            "MINUS", "NEWLINE", "WS" ]

    ruleNames = [ "TARG", "FILE", "ABS", "LOC", "NTRY", "NAME", "ALIG", 
                  "DATA", "REL", "XTRN", "WORD", "FP_BASE64", "ABS_SECTION", 
                  "COLON", "MINUS", "NEWLINE", "WS" ]

    grammarFileName = "ObjectFile.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


