# Generated from object_file/grammar/ObjectFileParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,253,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,3,0,58,8,0,1,0,3,0,61,8,0,1,0,4,0,64,8,0,11,0,12,0,
        65,1,0,1,0,1,1,3,1,71,8,1,1,1,1,1,5,1,75,8,1,10,1,12,1,78,9,1,1,
        1,4,1,81,8,1,11,1,12,1,82,3,1,85,8,1,1,1,5,1,88,8,1,10,1,12,1,91,
        9,1,1,2,1,2,4,2,95,8,2,11,2,12,2,96,1,3,1,3,3,3,101,8,3,1,3,5,3,
        104,8,3,10,3,12,3,107,9,3,1,4,1,4,3,4,111,8,4,1,4,1,4,3,4,115,8,
        4,1,4,5,4,118,8,4,10,4,12,4,121,9,4,1,4,3,4,124,8,4,1,4,5,4,127,
        8,4,10,4,12,4,130,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,3,7,145,8,7,1,7,4,7,148,8,7,11,7,12,7,149,1,8,1,8,5,8,
        154,8,8,10,8,12,8,157,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,3,12,176,8,12,1,12,4,12,
        179,8,12,11,12,12,12,180,1,13,1,13,5,13,185,8,13,10,13,12,13,188,
        9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,198,8,14,10,14,
        12,14,201,9,14,1,14,1,14,1,15,1,15,4,15,207,8,15,11,15,12,15,208,
        1,15,1,15,1,16,1,16,1,17,1,17,1,18,3,18,218,8,18,1,18,1,18,1,18,
        1,18,3,18,224,8,18,3,18,226,8,18,1,19,1,19,1,19,1,19,1,20,1,20,1,
        20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,
        25,1,25,1,26,1,26,1,27,1,27,1,27,0,0,28,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,0,2,1,0,12,
        13,2,0,12,12,14,14,252,0,57,1,0,0,0,2,70,1,0,0,0,4,94,1,0,0,0,6,
        98,1,0,0,0,8,108,1,0,0,0,10,131,1,0,0,0,12,135,1,0,0,0,14,140,1,
        0,0,0,16,151,1,0,0,0,18,160,1,0,0,0,20,165,1,0,0,0,22,169,1,0,0,
        0,24,173,1,0,0,0,26,182,1,0,0,0,28,191,1,0,0,0,30,204,1,0,0,0,32,
        212,1,0,0,0,34,214,1,0,0,0,36,217,1,0,0,0,38,227,1,0,0,0,40,231,
        1,0,0,0,42,234,1,0,0,0,44,240,1,0,0,0,46,242,1,0,0,0,48,244,1,0,
        0,0,50,246,1,0,0,0,52,248,1,0,0,0,54,250,1,0,0,0,56,58,5,19,0,0,
        57,56,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,61,3,10,5,0,60,59,1,
        0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,
        65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,0,0,
        1,68,1,1,0,0,0,69,71,3,12,6,0,70,69,1,0,0,0,70,71,1,0,0,0,71,84,
        1,0,0,0,72,76,3,4,2,0,73,75,3,8,4,0,74,73,1,0,0,0,75,78,1,0,0,0,
        76,74,1,0,0,0,76,77,1,0,0,0,77,85,1,0,0,0,78,76,1,0,0,0,79,81,3,
        8,4,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,
        85,1,0,0,0,84,72,1,0,0,0,84,80,1,0,0,0,85,89,1,0,0,0,86,88,3,28,
        14,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,
        3,1,0,0,0,91,89,1,0,0,0,92,95,3,6,3,0,93,95,3,18,9,0,94,92,1,0,0,
        0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,5,1,
        0,0,0,98,100,3,14,7,0,99,101,3,30,15,0,100,99,1,0,0,0,100,101,1,
        0,0,0,101,105,1,0,0,0,102,104,3,16,8,0,103,102,1,0,0,0,104,107,1,
        0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,7,1,0,0,0,107,105,1,0,
        0,0,108,110,3,20,10,0,109,111,3,22,11,0,110,109,1,0,0,0,110,111,
        1,0,0,0,111,112,1,0,0,0,112,114,3,24,12,0,113,115,3,30,15,0,114,
        113,1,0,0,0,114,115,1,0,0,0,115,119,1,0,0,0,116,118,3,16,8,0,117,
        116,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,
        123,1,0,0,0,121,119,1,0,0,0,122,124,3,26,13,0,123,122,1,0,0,0,123,
        124,1,0,0,0,124,128,1,0,0,0,125,127,3,18,9,0,126,125,1,0,0,0,127,
        130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,9,1,0,0,0,130,128,
        1,0,0,0,131,132,5,1,0,0,132,133,3,50,25,0,133,134,5,19,0,0,134,11,
        1,0,0,0,135,136,5,2,0,0,136,137,5,26,0,0,137,138,3,34,17,0,138,139,
        5,19,0,0,139,13,1,0,0,0,140,141,5,3,0,0,141,142,3,46,23,0,142,144,
        5,25,0,0,143,145,3,32,16,0,144,143,1,0,0,0,144,145,1,0,0,0,145,147,
        1,0,0,0,146,148,5,21,0,0,147,146,1,0,0,0,148,149,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,15,1,0,0,0,151,155,5,4,0,0,152,154,3,
        42,21,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,
        1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,159,5,19,0,0,159,17,
        1,0,0,0,160,161,5,5,0,0,161,162,3,50,25,0,162,163,3,48,24,0,163,
        164,5,19,0,0,164,19,1,0,0,0,165,166,5,6,0,0,166,167,3,52,26,0,167,
        168,5,19,0,0,168,21,1,0,0,0,169,170,5,7,0,0,170,171,3,48,24,0,171,
        172,5,19,0,0,172,23,1,0,0,0,173,175,5,8,0,0,174,176,3,32,16,0,175,
        174,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,179,5,21,0,0,178,
        177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
        25,1,0,0,0,182,186,5,9,0,0,183,185,3,36,18,0,184,183,1,0,0,0,185,
        188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,
        186,1,0,0,0,189,190,5,19,0,0,190,27,1,0,0,0,191,192,5,10,0,0,192,
        193,3,50,25,0,193,199,5,15,0,0,194,195,3,52,26,0,195,196,3,36,18,
        0,196,198,1,0,0,0,197,194,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,
        0,199,200,1,0,0,0,200,202,1,0,0,0,201,199,1,0,0,0,202,203,5,19,0,
        0,203,29,1,0,0,0,204,206,5,11,0,0,205,207,3,44,22,0,206,205,1,0,
        0,0,207,208,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,210,1,0,
        0,0,210,211,5,19,0,0,211,31,1,0,0,0,212,213,5,22,0,0,213,33,1,0,
        0,0,214,215,5,27,0,0,215,35,1,0,0,0,216,218,3,54,27,0,217,216,1,
        0,0,0,217,218,1,0,0,0,218,219,1,0,0,0,219,225,3,48,24,0,220,221,
        5,15,0,0,221,223,3,38,19,0,222,224,3,40,20,0,223,222,1,0,0,0,223,
        224,1,0,0,0,224,226,1,0,0,0,225,220,1,0,0,0,225,226,1,0,0,0,226,
        37,1,0,0,0,227,228,3,48,24,0,228,229,5,15,0,0,229,230,3,48,24,0,
        230,39,1,0,0,0,231,232,5,17,0,0,232,233,3,48,24,0,233,41,1,0,0,0,
        234,235,3,48,24,0,235,236,5,15,0,0,236,237,3,48,24,0,237,238,5,15,
        0,0,238,239,3,48,24,0,239,43,1,0,0,0,240,241,5,12,0,0,241,45,1,0,
        0,0,242,243,5,23,0,0,243,47,1,0,0,0,244,245,5,12,0,0,245,49,1,0,
        0,0,246,247,7,0,0,0,247,51,1,0,0,0,248,249,7,1,0,0,249,53,1,0,0,
        0,250,251,5,16,0,0,251,55,1,0,0,0,28,57,60,65,70,76,82,84,89,94,
        96,100,105,110,114,119,123,128,144,149,155,175,180,186,199,208,217,
        223,225
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFileParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TARG'", "'FILE'", "'ABS'", "'LOC'", 
                     "'NTRY'", "'NAME'", "'ALIG'", "'DATA'", "'REL'", "'XTRN'", 
                     "'ATTR'", "<INVALID>", "<INVALID>", "'$abs'", "<INVALID>", 
                     "'-'", "'+'", "'.'" ]

    symbolicNames = [ "<INVALID>", "TARG", "FILE", "ABS", "LOC", "NTRY", 
                      "NAME", "ALIG", "DATA", "REL", "XTRN", "ATTR", "WORD", 
                      "WORD_WITH_DOTS", "ABS_SECTION", "COLON", "MINUS", 
                      "PLUS", "DOT", "NEWLINE", "WS", "NEWLINE_BYTES", "BYTES", 
                      "WORD_ABS", "WS_ABS", "COLON_ABS", "SPACES_FILE", 
                      "FILEPATH" ]

    RULE_object_file = 0
    RULE_object_block = 1
    RULE_asect_block = 2
    RULE_abs_block = 3
    RULE_rsect_block = 4
    RULE_targ_record = 5
    RULE_source_record = 6
    RULE_abs_record = 7
    RULE_loc_record = 8
    RULE_ntry_record = 9
    RULE_name_record = 10
    RULE_alig_record = 11
    RULE_data_record = 12
    RULE_rel_record = 13
    RULE_xtrn_record = 14
    RULE_attr_record = 15
    RULE_data = 16
    RULE_filepath = 17
    RULE_entry_usage = 18
    RULE_range = 19
    RULE_lower_part = 20
    RULE_location = 21
    RULE_section_attr = 22
    RULE_abs_address = 23
    RULE_number = 24
    RULE_label = 25
    RULE_section = 26
    RULE_minus = 27

    ruleNames =  [ "object_file", "object_block", "asect_block", "abs_block", 
                   "rsect_block", "targ_record", "source_record", "abs_record", 
                   "loc_record", "ntry_record", "name_record", "alig_record", 
                   "data_record", "rel_record", "xtrn_record", "attr_record", 
                   "data", "filepath", "entry_usage", "range", "lower_part", 
                   "location", "section_attr", "abs_address", "number", 
                   "label", "section", "minus" ]

    EOF = Token.EOF
    TARG=1
    FILE=2
    ABS=3
    LOC=4
    NTRY=5
    NAME=6
    ALIG=7
    DATA=8
    REL=9
    XTRN=10
    ATTR=11
    WORD=12
    WORD_WITH_DOTS=13
    ABS_SECTION=14
    COLON=15
    MINUS=16
    PLUS=17
    DOT=18
    NEWLINE=19
    WS=20
    NEWLINE_BYTES=21
    BYTES=22
    WORD_ABS=23
    WS_ABS=24
    COLON_ABS=25
    SPACES_FILE=26
    FILEPATH=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Object_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ObjectFileParser.EOF, 0)

        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def targ_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Targ_recordContext,0)


        def object_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Object_blockContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Object_blockContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_object_file

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_file" ):
                return visitor.visitObject_file(self)
            else:
                return visitor.visitChildren(self)




    def object_file(self):

        localctx = ObjectFileParser.Object_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_object_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 56
                self.match(ObjectFileParser.NEWLINE)


            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 59
                self.targ_record()


            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.object_block()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 108) != 0)):
                    break

            self.state = 67
            self.match(ObjectFileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asect_block(self):
            return self.getTypedRuleContext(ObjectFileParser.Asect_blockContext,0)


        def source_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Source_recordContext,0)


        def xtrn_record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Xtrn_recordContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Xtrn_recordContext,i)


        def rsect_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Rsect_blockContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Rsect_blockContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_object_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_block" ):
                return visitor.visitObject_block(self)
            else:
                return visitor.visitChildren(self)




    def object_block(self):

        localctx = ObjectFileParser.Object_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_object_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 69
                self.source_record()


            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5]:
                self.state = 72
                self.asect_block()
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 73
                        self.rsect_block() 
                    self.state = 78
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            elif token in [6]:
                self.state = 80 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 79
                        self.rsect_block()

                    else:
                        raise NoViableAltException(self)
                    self.state = 82 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 86
                self.xtrn_record()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asect_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def abs_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Abs_blockContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Abs_blockContext,i)


        def ntry_record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Ntry_recordContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Ntry_recordContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_asect_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsect_block" ):
                return visitor.visitAsect_block(self)
            else:
                return visitor.visitChildren(self)




    def asect_block(self):

        localctx = ObjectFileParser.Asect_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asect_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 94
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 92
                        self.abs_block()
                        pass
                    elif token in [5]:
                        self.state = 93
                        self.ntry_record()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 96 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abs_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def abs_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Abs_recordContext,0)


        def attr_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Attr_recordContext,0)


        def loc_record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Loc_recordContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Loc_recordContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_abs_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs_block" ):
                return visitor.visitAbs_block(self)
            else:
                return visitor.visitChildren(self)




    def abs_block(self):

        localctx = ObjectFileParser.Abs_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_abs_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.abs_record()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 99
                self.attr_record()


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 102
                self.loc_record()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rsect_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Name_recordContext,0)


        def data_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Data_recordContext,0)


        def alig_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Alig_recordContext,0)


        def attr_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Attr_recordContext,0)


        def loc_record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Loc_recordContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Loc_recordContext,i)


        def rel_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Rel_recordContext,0)


        def ntry_record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Ntry_recordContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Ntry_recordContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_rsect_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRsect_block" ):
                return visitor.visitRsect_block(self)
            else:
                return visitor.visitChildren(self)




    def rsect_block(self):

        localctx = ObjectFileParser.Rsect_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rsect_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.name_record()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 109
                self.alig_record()


            self.state = 112
            self.data_record()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 113
                self.attr_record()


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 116
                self.loc_record()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 122
                self.rel_record()


            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 125
                    self.ntry_record() 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Targ_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TARG(self):
            return self.getToken(ObjectFileParser.TARG, 0)

        def label(self):
            return self.getTypedRuleContext(ObjectFileParser.LabelContext,0)


        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_targ_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarg_record" ):
                return visitor.visitTarg_record(self)
            else:
                return visitor.visitChildren(self)




    def targ_record(self):

        localctx = ObjectFileParser.Targ_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_targ_record)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ObjectFileParser.TARG)
            self.state = 132
            self.label()
            self.state = 133
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Source_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILE(self):
            return self.getToken(ObjectFileParser.FILE, 0)

        def SPACES_FILE(self):
            return self.getToken(ObjectFileParser.SPACES_FILE, 0)

        def filepath(self):
            return self.getTypedRuleContext(ObjectFileParser.FilepathContext,0)


        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_source_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource_record" ):
                return visitor.visitSource_record(self)
            else:
                return visitor.visitChildren(self)




    def source_record(self):

        localctx = ObjectFileParser.Source_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_source_record)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ObjectFileParser.FILE)
            self.state = 136
            self.match(ObjectFileParser.SPACES_FILE)
            self.state = 137
            self.filepath()
            self.state = 138
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abs_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABS(self):
            return self.getToken(ObjectFileParser.ABS, 0)

        def abs_address(self):
            return self.getTypedRuleContext(ObjectFileParser.Abs_addressContext,0)


        def COLON_ABS(self):
            return self.getToken(ObjectFileParser.COLON_ABS, 0)

        def data(self):
            return self.getTypedRuleContext(ObjectFileParser.DataContext,0)


        def NEWLINE_BYTES(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE_BYTES)
            else:
                return self.getToken(ObjectFileParser.NEWLINE_BYTES, i)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_abs_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs_record" ):
                return visitor.visitAbs_record(self)
            else:
                return visitor.visitChildren(self)




    def abs_record(self):

        localctx = ObjectFileParser.Abs_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_abs_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ObjectFileParser.ABS)
            self.state = 141
            self.abs_address()
            self.state = 142
            self.match(ObjectFileParser.COLON_ABS)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 143
                self.data()


            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.match(ObjectFileParser.NEWLINE_BYTES)
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loc_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOC(self):
            return self.getToken(ObjectFileParser.LOC, 0)

        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def location(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.LocationContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.LocationContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_loc_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoc_record" ):
                return visitor.visitLoc_record(self)
            else:
                return visitor.visitChildren(self)




    def loc_record(self):

        localctx = ObjectFileParser.Loc_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loc_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ObjectFileParser.LOC)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 152
                self.location()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ntry_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NTRY(self):
            return self.getToken(ObjectFileParser.NTRY, 0)

        def label(self):
            return self.getTypedRuleContext(ObjectFileParser.LabelContext,0)


        def number(self):
            return self.getTypedRuleContext(ObjectFileParser.NumberContext,0)


        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_ntry_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNtry_record" ):
                return visitor.visitNtry_record(self)
            else:
                return visitor.visitChildren(self)




    def ntry_record(self):

        localctx = ObjectFileParser.Ntry_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ntry_record)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ObjectFileParser.NTRY)
            self.state = 161
            self.label()
            self.state = 162
            self.number()
            self.state = 163
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ObjectFileParser.NAME, 0)

        def section(self):
            return self.getTypedRuleContext(ObjectFileParser.SectionContext,0)


        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_name_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_record" ):
                return visitor.visitName_record(self)
            else:
                return visitor.visitChildren(self)




    def name_record(self):

        localctx = ObjectFileParser.Name_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_name_record)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ObjectFileParser.NAME)
            self.state = 166
            self.section()
            self.state = 167
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alig_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALIG(self):
            return self.getToken(ObjectFileParser.ALIG, 0)

        def number(self):
            return self.getTypedRuleContext(ObjectFileParser.NumberContext,0)


        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_alig_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlig_record" ):
                return visitor.visitAlig_record(self)
            else:
                return visitor.visitChildren(self)




    def alig_record(self):

        localctx = ObjectFileParser.Alig_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alig_record)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ObjectFileParser.ALIG)
            self.state = 170
            self.number()
            self.state = 171
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(ObjectFileParser.DATA, 0)

        def data(self):
            return self.getTypedRuleContext(ObjectFileParser.DataContext,0)


        def NEWLINE_BYTES(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE_BYTES)
            else:
                return self.getToken(ObjectFileParser.NEWLINE_BYTES, i)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_data_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_record" ):
                return visitor.visitData_record(self)
            else:
                return visitor.visitChildren(self)




    def data_record(self):

        localctx = ObjectFileParser.Data_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_data_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(ObjectFileParser.DATA)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 174
                self.data()


            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.match(ObjectFileParser.NEWLINE_BYTES)
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REL(self):
            return self.getToken(ObjectFileParser.REL, 0)

        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def entry_usage(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Entry_usageContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Entry_usageContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_rel_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_record" ):
                return visitor.visitRel_record(self)
            else:
                return visitor.visitChildren(self)




    def rel_record(self):

        localctx = ObjectFileParser.Rel_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_rel_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ObjectFileParser.REL)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==16:
                self.state = 183
                self.entry_usage()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Xtrn_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XTRN(self):
            return self.getToken(ObjectFileParser.XTRN, 0)

        def label(self):
            return self.getTypedRuleContext(ObjectFileParser.LabelContext,0)


        def COLON(self):
            return self.getToken(ObjectFileParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.SectionContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.SectionContext,i)


        def entry_usage(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Entry_usageContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Entry_usageContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_xtrn_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXtrn_record" ):
                return visitor.visitXtrn_record(self)
            else:
                return visitor.visitChildren(self)




    def xtrn_record(self):

        localctx = ObjectFileParser.Xtrn_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_xtrn_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(ObjectFileParser.XTRN)
            self.state = 192
            self.label()
            self.state = 193
            self.match(ObjectFileParser.COLON)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==14:
                self.state = 194
                self.section()
                self.state = 195
                self.entry_usage()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTR(self):
            return self.getToken(ObjectFileParser.ATTR, 0)

        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

        def section_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Section_attrContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Section_attrContext,i)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_attr_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_record" ):
                return visitor.visitAttr_record(self)
            else:
                return visitor.visitChildren(self)




    def attr_record(self):

        localctx = ObjectFileParser.Attr_recordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attr_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ObjectFileParser.ATTR)
            self.state = 206 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 205
                self.section_attr()
                self.state = 208 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

            self.state = 210
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BYTES(self):
            return self.getToken(ObjectFileParser.BYTES, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = ObjectFileParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ObjectFileParser.BYTES)
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

        def FILEPATH(self):
            return self.getToken(ObjectFileParser.FILEPATH, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_filepath

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilepath" ):
                return visitor.visitFilepath(self)
            else:
                return visitor.visitChildren(self)




    def filepath(self):

        localctx = ObjectFileParser.FilepathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ObjectFileParser.FILEPATH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entry_usageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(ObjectFileParser.NumberContext,0)


        def minus(self):
            return self.getTypedRuleContext(ObjectFileParser.MinusContext,0)


        def COLON(self):
            return self.getToken(ObjectFileParser.COLON, 0)

        def range_(self):
            return self.getTypedRuleContext(ObjectFileParser.RangeContext,0)


        def lower_part(self):
            return self.getTypedRuleContext(ObjectFileParser.Lower_partContext,0)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_entry_usage

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry_usage" ):
                return visitor.visitEntry_usage(self)
            else:
                return visitor.visitChildren(self)




    def entry_usage(self):

        localctx = ObjectFileParser.Entry_usageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_entry_usage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 216
                self.minus()


            self.state = 219
            self.number()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 220
                self.match(ObjectFileParser.COLON)
                self.state = 221
                self.range_()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 222
                    self.lower_part()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.NumberContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.NumberContext,i)


        def COLON(self):
            return self.getToken(ObjectFileParser.COLON, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = ObjectFileParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.number()
            self.state = 228
            self.match(ObjectFileParser.COLON)
            self.state = 229
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lower_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ObjectFileParser.PLUS, 0)

        def number(self):
            return self.getTypedRuleContext(ObjectFileParser.NumberContext,0)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_lower_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLower_part" ):
                return visitor.visitLower_part(self)
            else:
                return visitor.visitChildren(self)




    def lower_part(self):

        localctx = ObjectFileParser.Lower_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lower_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(ObjectFileParser.PLUS)
            self.state = 232
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.NumberContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.NumberContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.COLON)
            else:
                return self.getToken(ObjectFileParser.COLON, i)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_location

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocation" ):
                return visitor.visitLocation(self)
            else:
                return visitor.visitChildren(self)




    def location(self):

        localctx = ObjectFileParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.number()
            self.state = 235
            self.match(ObjectFileParser.COLON)
            self.state = 236
            self.number()
            self.state = 237
            self.match(ObjectFileParser.COLON)
            self.state = 238
            self.number()
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
            return self.getToken(ObjectFileParser.WORD, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_section_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection_attr" ):
                return visitor.visitSection_attr(self)
            else:
                return visitor.visitChildren(self)




    def section_attr(self):

        localctx = ObjectFileParser.Section_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_section_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(ObjectFileParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Abs_addressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD_ABS(self):
            return self.getToken(ObjectFileParser.WORD_ABS, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_abs_address

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs_address" ):
                return visitor.visitAbs_address(self)
            else:
                return visitor.visitChildren(self)




    def abs_address(self):

        localctx = ObjectFileParser.Abs_addressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_abs_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(ObjectFileParser.WORD_ABS)
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

        def WORD(self):
            return self.getToken(ObjectFileParser.WORD, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = ObjectFileParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ObjectFileParser.WORD)
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

        def WORD(self):
            return self.getToken(ObjectFileParser.WORD, 0)

        def WORD_WITH_DOTS(self):
            return self.getToken(ObjectFileParser.WORD_WITH_DOTS, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = ObjectFileParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
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


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ObjectFileParser.WORD, 0)

        def ABS_SECTION(self):
            return self.getToken(ObjectFileParser.ABS_SECTION, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_section

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = ObjectFileParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==12 or _la==14):
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


    class MinusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ObjectFileParser.MINUS, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_minus

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)




    def minus(self):

        localctx = ObjectFileParser.MinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ObjectFileParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





