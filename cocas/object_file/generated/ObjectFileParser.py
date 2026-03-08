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
        4,1,28,248,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,3,0,58,8,0,1,0,3,0,61,8,0,1,0,4,0,64,8,0,11,0,12,0,
        65,1,0,1,0,1,1,3,1,71,8,1,1,1,1,1,5,1,75,8,1,10,1,12,1,78,9,1,1,
        1,4,1,81,8,1,11,1,12,1,82,3,1,85,8,1,1,1,5,1,88,8,1,10,1,12,1,91,
        9,1,1,2,1,2,4,2,95,8,2,11,2,12,2,96,1,3,1,3,5,3,101,8,3,10,3,12,
        3,104,9,3,1,4,1,4,3,4,108,8,4,1,4,1,4,5,4,112,8,4,10,4,12,4,115,
        9,4,1,4,3,4,118,8,4,1,4,5,4,121,8,4,10,4,12,4,124,9,4,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,139,8,7,1,7,4,7,142,
        8,7,11,7,12,7,143,1,8,1,8,5,8,148,8,8,10,8,12,8,151,9,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,12,1,12,3,12,171,8,12,1,12,4,12,174,8,12,11,12,12,12,175,1,13,
        1,13,5,13,180,8,13,10,13,12,13,183,9,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,5,14,194,8,14,10,14,12,14,197,9,14,1,14,1,14,
        1,15,1,15,3,15,203,8,15,1,16,1,16,1,16,3,16,208,8,16,1,17,1,17,1,
        18,1,18,1,19,3,19,215,8,19,1,19,1,19,1,19,1,19,3,19,221,8,19,3,19,
        223,8,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,
        1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,
        0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,0,2,1,0,14,15,1,0,14,16,247,0,57,1,0,0,0,2,
        70,1,0,0,0,4,94,1,0,0,0,6,98,1,0,0,0,8,105,1,0,0,0,10,125,1,0,0,
        0,12,129,1,0,0,0,14,134,1,0,0,0,16,145,1,0,0,0,18,154,1,0,0,0,20,
        160,1,0,0,0,22,164,1,0,0,0,24,168,1,0,0,0,26,177,1,0,0,0,28,186,
        1,0,0,0,30,202,1,0,0,0,32,207,1,0,0,0,34,209,1,0,0,0,36,211,1,0,
        0,0,38,214,1,0,0,0,40,224,1,0,0,0,42,228,1,0,0,0,44,231,1,0,0,0,
        46,237,1,0,0,0,48,239,1,0,0,0,50,241,1,0,0,0,52,243,1,0,0,0,54,245,
        1,0,0,0,56,58,5,20,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,
        59,61,3,10,5,0,60,59,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,64,3,
        2,1,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,
        67,1,0,0,0,67,68,5,0,0,1,68,1,1,0,0,0,69,71,3,12,6,0,70,69,1,0,0,
        0,70,71,1,0,0,0,71,84,1,0,0,0,72,76,3,4,2,0,73,75,3,8,4,0,74,73,
        1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,85,1,0,0,0,
        78,76,1,0,0,0,79,81,3,8,4,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,
        0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,72,1,0,0,0,84,80,1,0,0,0,85,
        89,1,0,0,0,86,88,3,28,14,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,
        0,0,89,90,1,0,0,0,90,3,1,0,0,0,91,89,1,0,0,0,92,95,3,6,3,0,93,95,
        3,18,9,0,94,92,1,0,0,0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,0,
        96,97,1,0,0,0,97,5,1,0,0,0,98,102,3,14,7,0,99,101,3,16,8,0,100,99,
        1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,7,1,
        0,0,0,104,102,1,0,0,0,105,107,3,20,10,0,106,108,3,22,11,0,107,106,
        1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,113,3,24,12,0,110,112,
        3,16,8,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,
        1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,116,118,3,26,13,0,117,116,
        1,0,0,0,117,118,1,0,0,0,118,122,1,0,0,0,119,121,3,18,9,0,120,119,
        1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,9,1,
        0,0,0,124,122,1,0,0,0,125,126,5,1,0,0,126,127,3,50,25,0,127,128,
        5,20,0,0,128,11,1,0,0,0,129,130,5,2,0,0,130,131,5,27,0,0,131,132,
        3,36,18,0,132,133,5,20,0,0,133,13,1,0,0,0,134,135,5,3,0,0,135,136,
        3,46,23,0,136,138,5,26,0,0,137,139,3,34,17,0,138,137,1,0,0,0,138,
        139,1,0,0,0,139,141,1,0,0,0,140,142,5,22,0,0,141,140,1,0,0,0,142,
        143,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,15,1,0,0,0,145,149,
        5,4,0,0,146,148,3,44,22,0,147,146,1,0,0,0,148,151,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,149,1,0,0,0,152,153,
        5,20,0,0,153,17,1,0,0,0,154,155,5,5,0,0,155,156,3,50,25,0,156,157,
        3,30,15,0,157,158,3,48,24,0,158,159,5,20,0,0,159,19,1,0,0,0,160,
        161,5,6,0,0,161,162,3,52,26,0,162,163,5,20,0,0,163,21,1,0,0,0,164,
        165,5,7,0,0,165,166,3,48,24,0,166,167,5,20,0,0,167,23,1,0,0,0,168,
        170,5,8,0,0,169,171,3,34,17,0,170,169,1,0,0,0,170,171,1,0,0,0,171,
        173,1,0,0,0,172,174,5,22,0,0,173,172,1,0,0,0,174,175,1,0,0,0,175,
        173,1,0,0,0,175,176,1,0,0,0,176,25,1,0,0,0,177,181,5,9,0,0,178,180,
        3,38,19,0,179,178,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,
        1,0,0,0,182,184,1,0,0,0,183,181,1,0,0,0,184,185,5,20,0,0,185,27,
        1,0,0,0,186,187,5,10,0,0,187,188,3,50,25,0,188,189,3,30,15,0,189,
        195,5,17,0,0,190,191,3,52,26,0,191,192,3,38,19,0,192,194,1,0,0,0,
        193,190,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,
        196,198,1,0,0,0,197,195,1,0,0,0,198,199,5,20,0,0,199,29,1,0,0,0,
        200,201,5,19,0,0,201,203,3,32,16,0,202,200,1,0,0,0,202,203,1,0,0,
        0,203,31,1,0,0,0,204,208,5,11,0,0,205,208,5,12,0,0,206,208,5,13,
        0,0,207,204,1,0,0,0,207,205,1,0,0,0,207,206,1,0,0,0,208,33,1,0,0,
        0,209,210,5,23,0,0,210,35,1,0,0,0,211,212,5,28,0,0,212,37,1,0,0,
        0,213,215,3,54,27,0,214,213,1,0,0,0,214,215,1,0,0,0,215,216,1,0,
        0,0,216,222,3,48,24,0,217,218,5,17,0,0,218,220,3,40,20,0,219,221,
        3,42,21,0,220,219,1,0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,217,
        1,0,0,0,222,223,1,0,0,0,223,39,1,0,0,0,224,225,3,48,24,0,225,226,
        5,17,0,0,226,227,3,48,24,0,227,41,1,0,0,0,228,229,5,19,0,0,229,230,
        3,48,24,0,230,43,1,0,0,0,231,232,3,48,24,0,232,233,5,17,0,0,233,
        234,3,48,24,0,234,235,5,17,0,0,235,236,3,48,24,0,236,45,1,0,0,0,
        237,238,5,24,0,0,238,47,1,0,0,0,239,240,5,14,0,0,240,49,1,0,0,0,
        241,242,7,0,0,0,242,51,1,0,0,0,243,244,7,1,0,0,244,53,1,0,0,0,245,
        246,5,18,0,0,246,55,1,0,0,0,27,57,60,65,70,76,82,84,89,94,96,102,
        107,113,117,122,138,143,149,170,175,181,195,202,207,214,220,222
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFileParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TARG'", "'FILE'", "'ABS'", "'LOC'", 
                     "'NTRY'", "'NAME'", "'ALIG'", "'DATA'", "'REL'", "'XTRN'", 
                     "'GLOBAL'", "'WEAK'", "'LOCAL'", "<INVALID>", "<INVALID>", 
                     "'$abs'", "<INVALID>", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>", "TARG", "FILE", "ABS", "LOC", "NTRY", 
                      "NAME", "ALIG", "DATA", "REL", "XTRN", "GLOBAL", "WEAK", 
                      "LOCAL", "WORD", "WORD_WITH_DOTS", "ABS_SECTION", 
                      "COLON", "MINUS", "PLUS", "NEWLINE", "WS", "NEWLINE_BYTES", 
                      "BYTES", "WORD_ABS", "WS_ABS", "COLON_ABS", "SPACES_FILE", 
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
    RULE_linkage_spec = 15
    RULE_linkage = 16
    RULE_data = 17
    RULE_filepath = 18
    RULE_entry_usage = 19
    RULE_range = 20
    RULE_lower_part = 21
    RULE_location = 22
    RULE_abs_address = 23
    RULE_number = 24
    RULE_label = 25
    RULE_section = 26
    RULE_minus = 27

    ruleNames =  [ "object_file", "object_block", "asect_block", "abs_block", 
                   "rsect_block", "targ_record", "source_record", "abs_record", 
                   "loc_record", "ntry_record", "name_record", "alig_record", 
                   "data_record", "rel_record", "xtrn_record", "linkage_spec", 
                   "linkage", "data", "filepath", "entry_usage", "range", 
                   "lower_part", "location", "abs_address", "number", "label", 
                   "section", "minus" ]

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
    GLOBAL=11
    WEAK=12
    LOCAL=13
    WORD=14
    WORD_WITH_DOTS=15
    ABS_SECTION=16
    COLON=17
    MINUS=18
    PLUS=19
    NEWLINE=20
    WS=21
    NEWLINE_BYTES=22
    BYTES=23
    WORD_ABS=24
    WS_ABS=25
    COLON_ABS=26
    SPACES_FILE=27
    FILEPATH=28

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
            if _la==20:
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
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 99
                self.loc_record()
                self.state = 104
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
            self.state = 105
            self.name_record()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 106
                self.alig_record()


            self.state = 109
            self.data_record()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 110
                self.loc_record()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 116
                self.rel_record()


            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    self.ntry_record() 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.state = 125
            self.match(ObjectFileParser.TARG)
            self.state = 126
            self.label()
            self.state = 127
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
            self.state = 129
            self.match(ObjectFileParser.FILE)
            self.state = 130
            self.match(ObjectFileParser.SPACES_FILE)
            self.state = 131
            self.filepath()
            self.state = 132
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
            self.state = 134
            self.match(ObjectFileParser.ABS)
            self.state = 135
            self.abs_address()
            self.state = 136
            self.match(ObjectFileParser.COLON_ABS)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 137
                self.data()


            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.match(ObjectFileParser.NEWLINE_BYTES)
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
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
            self.state = 145
            self.match(ObjectFileParser.LOC)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 146
                self.location()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
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


        def linkage_spec(self):
            return self.getTypedRuleContext(ObjectFileParser.Linkage_specContext,0)


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
            self.state = 154
            self.match(ObjectFileParser.NTRY)
            self.state = 155
            self.label()
            self.state = 156
            self.linkage_spec()
            self.state = 157
            self.number()
            self.state = 158
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
            self.state = 160
            self.match(ObjectFileParser.NAME)
            self.state = 161
            self.section()
            self.state = 162
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
            self.state = 164
            self.match(ObjectFileParser.ALIG)
            self.state = 165
            self.number()
            self.state = 166
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
            self.state = 168
            self.match(ObjectFileParser.DATA)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 169
                self.data()


            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.match(ObjectFileParser.NEWLINE_BYTES)
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
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
            self.state = 177
            self.match(ObjectFileParser.REL)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==18:
                self.state = 178
                self.entry_usage()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
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


        def linkage_spec(self):
            return self.getTypedRuleContext(ObjectFileParser.Linkage_specContext,0)


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
            self.state = 186
            self.match(ObjectFileParser.XTRN)
            self.state = 187
            self.label()
            self.state = 188
            self.linkage_spec()
            self.state = 189
            self.match(ObjectFileParser.COLON)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 190
                self.section()
                self.state = 191
                self.entry_usage()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            self.match(ObjectFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Linkage_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ObjectFileParser.PLUS, 0)

        def linkage(self):
            return self.getTypedRuleContext(ObjectFileParser.LinkageContext,0)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_linkage_spec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkage_spec" ):
                return visitor.visitLinkage_spec(self)
            else:
                return visitor.visitChildren(self)




    def linkage_spec(self):

        localctx = ObjectFileParser.Linkage_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_linkage_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 200
                self.match(ObjectFileParser.PLUS)
                self.state = 201
                self.linkage()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ObjectFileParser.RULE_linkage

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WeakContext(LinkageContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjectFileParser.LinkageContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WEAK(self):
            return self.getToken(ObjectFileParser.WEAK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeak" ):
                return visitor.visitWeak(self)
            else:
                return visitor.visitChildren(self)


    class LocalContext(LinkageContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjectFileParser.LinkageContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOCAL(self):
            return self.getToken(ObjectFileParser.LOCAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal" ):
                return visitor.visitLocal(self)
            else:
                return visitor.visitChildren(self)


    class GlobalContext(LinkageContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjectFileParser.LinkageContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GLOBAL(self):
            return self.getToken(ObjectFileParser.GLOBAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal" ):
                return visitor.visitGlobal(self)
            else:
                return visitor.visitChildren(self)



    def linkage(self):

        localctx = ObjectFileParser.LinkageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_linkage)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = ObjectFileParser.GlobalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(ObjectFileParser.GLOBAL)
                pass
            elif token in [12]:
                localctx = ObjectFileParser.WeakContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(ObjectFileParser.WEAK)
                pass
            elif token in [13]:
                localctx = ObjectFileParser.LocalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.match(ObjectFileParser.LOCAL)
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
        self.enterRule(localctx, 34, self.RULE_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
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
        self.enterRule(localctx, 36, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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
        self.enterRule(localctx, 38, self.RULE_entry_usage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 213
                self.minus()


            self.state = 216
            self.number()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 217
                self.match(ObjectFileParser.COLON)
                self.state = 218
                self.range_()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 219
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
        self.enterRule(localctx, 40, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.number()
            self.state = 225
            self.match(ObjectFileParser.COLON)
            self.state = 226
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
        self.enterRule(localctx, 42, self.RULE_lower_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(ObjectFileParser.PLUS)
            self.state = 229
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
        self.enterRule(localctx, 44, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.number()
            self.state = 232
            self.match(ObjectFileParser.COLON)
            self.state = 233
            self.number()
            self.state = 234
            self.match(ObjectFileParser.COLON)
            self.state = 235
            self.number()
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
            self.state = 237
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
            self.state = 239
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
            self.state = 241
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
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

        def WORD_WITH_DOTS(self):
            return self.getToken(ObjectFileParser.WORD_WITH_DOTS, 0)

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
            self.state = 243
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
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
            self.state = 245
            self.match(ObjectFileParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





