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
        4,1,26,233,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,3,0,54,
        8,0,1,0,3,0,57,8,0,1,0,4,0,60,8,0,11,0,12,0,61,1,0,1,0,1,1,3,1,67,
        8,1,1,1,1,1,5,1,71,8,1,10,1,12,1,74,9,1,1,1,4,1,77,8,1,11,1,12,1,
        78,3,1,81,8,1,1,1,5,1,84,8,1,10,1,12,1,87,9,1,1,2,1,2,4,2,91,8,2,
        11,2,12,2,92,1,3,1,3,5,3,97,8,3,10,3,12,3,100,9,3,1,4,1,4,3,4,104,
        8,4,1,4,1,4,5,4,108,8,4,10,4,12,4,111,9,4,1,4,3,4,114,8,4,1,4,5,
        4,117,8,4,10,4,12,4,120,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,3,7,135,8,7,1,7,4,7,138,8,7,11,7,12,7,139,1,8,1,
        8,5,8,144,8,8,10,8,12,8,147,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,3,12,166,8,12,1,12,
        4,12,169,8,12,11,12,12,12,170,1,13,1,13,5,13,175,8,13,10,13,12,13,
        178,9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,188,8,14,10,
        14,12,14,191,9,14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,3,17,200,8,
        17,1,17,1,17,1,17,1,17,3,17,206,8,17,3,17,208,8,17,1,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,22,
        1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,0,0,26,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,2,1,0,11,
        12,2,0,11,11,13,13,231,0,53,1,0,0,0,2,66,1,0,0,0,4,90,1,0,0,0,6,
        94,1,0,0,0,8,101,1,0,0,0,10,121,1,0,0,0,12,125,1,0,0,0,14,130,1,
        0,0,0,16,141,1,0,0,0,18,150,1,0,0,0,20,155,1,0,0,0,22,159,1,0,0,
        0,24,163,1,0,0,0,26,172,1,0,0,0,28,181,1,0,0,0,30,194,1,0,0,0,32,
        196,1,0,0,0,34,199,1,0,0,0,36,209,1,0,0,0,38,213,1,0,0,0,40,216,
        1,0,0,0,42,222,1,0,0,0,44,224,1,0,0,0,46,226,1,0,0,0,48,228,1,0,
        0,0,50,230,1,0,0,0,52,54,5,18,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,
        56,1,0,0,0,55,57,3,10,5,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,0,
        0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,
        1,0,0,0,62,63,1,0,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,67,3,12,6,0,
        66,65,1,0,0,0,66,67,1,0,0,0,67,80,1,0,0,0,68,72,3,4,2,0,69,71,3,
        8,4,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,
        81,1,0,0,0,74,72,1,0,0,0,75,77,3,8,4,0,76,75,1,0,0,0,77,78,1,0,0,
        0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,68,1,0,0,0,80,76,
        1,0,0,0,81,85,1,0,0,0,82,84,3,28,14,0,83,82,1,0,0,0,84,87,1,0,0,
        0,85,83,1,0,0,0,85,86,1,0,0,0,86,3,1,0,0,0,87,85,1,0,0,0,88,91,3,
        6,3,0,89,91,3,18,9,0,90,88,1,0,0,0,90,89,1,0,0,0,91,92,1,0,0,0,92,
        90,1,0,0,0,92,93,1,0,0,0,93,5,1,0,0,0,94,98,3,14,7,0,95,97,3,16,
        8,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,
        7,1,0,0,0,100,98,1,0,0,0,101,103,3,20,10,0,102,104,3,22,11,0,103,
        102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,109,3,24,12,0,106,
        108,3,16,8,0,107,106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,
        110,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,112,114,3,26,13,0,113,
        112,1,0,0,0,113,114,1,0,0,0,114,118,1,0,0,0,115,117,3,18,9,0,116,
        115,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,
        9,1,0,0,0,120,118,1,0,0,0,121,122,5,1,0,0,122,123,3,46,23,0,123,
        124,5,18,0,0,124,11,1,0,0,0,125,126,5,2,0,0,126,127,5,25,0,0,127,
        128,3,32,16,0,128,129,5,18,0,0,129,13,1,0,0,0,130,131,5,3,0,0,131,
        132,3,42,21,0,132,134,5,24,0,0,133,135,3,30,15,0,134,133,1,0,0,0,
        134,135,1,0,0,0,135,137,1,0,0,0,136,138,5,20,0,0,137,136,1,0,0,0,
        138,139,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,15,1,0,0,0,141,
        145,5,4,0,0,142,144,3,40,20,0,143,142,1,0,0,0,144,147,1,0,0,0,145,
        143,1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,
        149,5,18,0,0,149,17,1,0,0,0,150,151,5,5,0,0,151,152,3,46,23,0,152,
        153,3,44,22,0,153,154,5,18,0,0,154,19,1,0,0,0,155,156,5,6,0,0,156,
        157,3,48,24,0,157,158,5,18,0,0,158,21,1,0,0,0,159,160,5,7,0,0,160,
        161,3,44,22,0,161,162,5,18,0,0,162,23,1,0,0,0,163,165,5,8,0,0,164,
        166,3,30,15,0,165,164,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,
        169,5,20,0,0,168,167,1,0,0,0,169,170,1,0,0,0,170,168,1,0,0,0,170,
        171,1,0,0,0,171,25,1,0,0,0,172,176,5,9,0,0,173,175,3,34,17,0,174,
        173,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,
        179,1,0,0,0,178,176,1,0,0,0,179,180,5,18,0,0,180,27,1,0,0,0,181,
        182,5,10,0,0,182,183,3,46,23,0,183,189,5,14,0,0,184,185,3,48,24,
        0,185,186,3,34,17,0,186,188,1,0,0,0,187,184,1,0,0,0,188,191,1,0,
        0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,189,1,0,
        0,0,192,193,5,18,0,0,193,29,1,0,0,0,194,195,5,21,0,0,195,31,1,0,
        0,0,196,197,5,26,0,0,197,33,1,0,0,0,198,200,3,50,25,0,199,198,1,
        0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,207,3,44,22,0,202,203,
        5,14,0,0,203,205,3,36,18,0,204,206,3,38,19,0,205,204,1,0,0,0,205,
        206,1,0,0,0,206,208,1,0,0,0,207,202,1,0,0,0,207,208,1,0,0,0,208,
        35,1,0,0,0,209,210,3,44,22,0,210,211,5,14,0,0,211,212,3,44,22,0,
        212,37,1,0,0,0,213,214,5,16,0,0,214,215,3,44,22,0,215,39,1,0,0,0,
        216,217,3,44,22,0,217,218,5,14,0,0,218,219,3,44,22,0,219,220,5,14,
        0,0,220,221,3,44,22,0,221,41,1,0,0,0,222,223,5,22,0,0,223,43,1,0,
        0,0,224,225,5,11,0,0,225,45,1,0,0,0,226,227,7,0,0,0,227,47,1,0,0,
        0,228,229,7,1,0,0,229,49,1,0,0,0,230,231,5,15,0,0,231,51,1,0,0,0,
        25,53,56,61,66,72,78,80,85,90,92,98,103,109,113,118,134,139,145,
        165,170,176,189,199,205,207
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFileParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TARG'", "'FILE'", "'ABS'", "'LOC'", 
                     "'NTRY'", "'NAME'", "'ALIG'", "'DATA'", "'REL'", "'XTRN'", 
                     "<INVALID>", "<INVALID>", "'$abs'", "<INVALID>", "'-'", 
                     "'+'", "'.'" ]

    symbolicNames = [ "<INVALID>", "TARG", "FILE", "ABS", "LOC", "NTRY", 
                      "NAME", "ALIG", "DATA", "REL", "XTRN", "WORD", "WORD_WITH_DOTS", 
                      "ABS_SECTION", "COLON", "MINUS", "PLUS", "DOT", "NEWLINE", 
                      "WS", "NEWLINE_BYTES", "BYTES", "WORD_ABS", "WS_ABS", 
                      "COLON_ABS", "SPACES_FILE", "FILEPATH" ]

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
    RULE_data = 15
    RULE_filepath = 16
    RULE_entry_usage = 17
    RULE_range = 18
    RULE_lower_part = 19
    RULE_location = 20
    RULE_abs_address = 21
    RULE_number = 22
    RULE_label = 23
    RULE_section = 24
    RULE_minus = 25

    ruleNames =  [ "object_file", "object_block", "asect_block", "abs_block", 
                   "rsect_block", "targ_record", "source_record", "abs_record", 
                   "loc_record", "ntry_record", "name_record", "alig_record", 
                   "data_record", "rel_record", "xtrn_record", "data", "filepath", 
                   "entry_usage", "range", "lower_part", "location", "abs_address", 
                   "number", "label", "section", "minus" ]

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
    WORD=11
    WORD_WITH_DOTS=12
    ABS_SECTION=13
    COLON=14
    MINUS=15
    PLUS=16
    DOT=17
    NEWLINE=18
    WS=19
    NEWLINE_BYTES=20
    BYTES=21
    WORD_ABS=22
    WS_ABS=23
    COLON_ABS=24
    SPACES_FILE=25
    FILEPATH=26

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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 52
                self.match(ObjectFileParser.NEWLINE)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 55
                self.targ_record()


            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.object_block()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 108) != 0)):
                    break

            self.state = 63
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
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 65
                self.source_record()


            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5]:
                self.state = 68
                self.asect_block()
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 69
                        self.rsect_block() 
                    self.state = 74
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            elif token in [6]:
                self.state = 76 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 75
                        self.rsect_block()

                    else:
                        raise NoViableAltException(self)
                    self.state = 78 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 82
                self.xtrn_record()
                self.state = 87
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
            self.state = 90 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 90
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 88
                        self.abs_block()
                        pass
                    elif token in [5]:
                        self.state = 89
                        self.ntry_record()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 92 
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
            self.state = 94
            self.abs_record()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 95
                self.loc_record()
                self.state = 100
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
            self.state = 101
            self.name_record()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 102
                self.alig_record()


            self.state = 105
            self.data_record()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 106
                self.loc_record()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 112
                self.rel_record()


            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 115
                    self.ntry_record() 
                self.state = 120
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
            self.state = 121
            self.match(ObjectFileParser.TARG)
            self.state = 122
            self.label()
            self.state = 123
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
            self.state = 125
            self.match(ObjectFileParser.FILE)
            self.state = 126
            self.match(ObjectFileParser.SPACES_FILE)
            self.state = 127
            self.filepath()
            self.state = 128
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
            self.state = 130
            self.match(ObjectFileParser.ABS)
            self.state = 131
            self.abs_address()
            self.state = 132
            self.match(ObjectFileParser.COLON_ABS)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 133
                self.data()


            self.state = 137 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 136
                self.match(ObjectFileParser.NEWLINE_BYTES)
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
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
            self.state = 141
            self.match(ObjectFileParser.LOC)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 142
                self.location()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
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
            self.state = 150
            self.match(ObjectFileParser.NTRY)
            self.state = 151
            self.label()
            self.state = 152
            self.number()
            self.state = 153
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
            self.state = 155
            self.match(ObjectFileParser.NAME)
            self.state = 156
            self.section()
            self.state = 157
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
            self.state = 159
            self.match(ObjectFileParser.ALIG)
            self.state = 160
            self.number()
            self.state = 161
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
            self.state = 163
            self.match(ObjectFileParser.DATA)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 164
                self.data()


            self.state = 168 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.match(ObjectFileParser.NEWLINE_BYTES)
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
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
            self.state = 172
            self.match(ObjectFileParser.REL)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==15:
                self.state = 173
                self.entry_usage()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
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
            self.state = 181
            self.match(ObjectFileParser.XTRN)
            self.state = 182
            self.label()
            self.state = 183
            self.match(ObjectFileParser.COLON)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==13:
                self.state = 184
                self.section()
                self.state = 185
                self.entry_usage()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
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
        self.enterRule(localctx, 30, self.RULE_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 32, self.RULE_filepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
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
        self.enterRule(localctx, 34, self.RULE_entry_usage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 198
                self.minus()


            self.state = 201
            self.number()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 202
                self.match(ObjectFileParser.COLON)
                self.state = 203
                self.range_()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 204
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
        self.enterRule(localctx, 36, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.number()
            self.state = 210
            self.match(ObjectFileParser.COLON)
            self.state = 211
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
        self.enterRule(localctx, 38, self.RULE_lower_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ObjectFileParser.PLUS)
            self.state = 214
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
        self.enterRule(localctx, 40, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.number()
            self.state = 217
            self.match(ObjectFileParser.COLON)
            self.state = 218
            self.number()
            self.state = 219
            self.match(ObjectFileParser.COLON)
            self.state = 220
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
        self.enterRule(localctx, 42, self.RULE_abs_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
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
        self.enterRule(localctx, 44, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
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
        self.enterRule(localctx, 46, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
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
        self.enterRule(localctx, 48, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not(_la==11 or _la==13):
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
        self.enterRule(localctx, 50, self.RULE_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ObjectFileParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





