# Generated from ./grammar/ObjectFile.g4 by ANTLR 4.13.1
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
        4,1,17,261,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,3,0,58,8,0,1,0,4,0,61,8,0,11,0,12,0,62,1,0,1,0,1,
        1,3,1,68,8,1,1,1,1,1,5,1,72,8,1,10,1,12,1,75,9,1,1,1,4,1,78,8,1,
        11,1,12,1,79,3,1,82,8,1,1,1,5,1,85,8,1,10,1,12,1,88,9,1,1,2,1,2,
        4,2,92,8,2,11,2,12,2,93,1,3,1,3,5,3,98,8,3,10,3,12,3,101,9,3,1,4,
        1,4,3,4,105,8,4,1,4,1,4,5,4,109,8,4,10,4,12,4,112,9,4,1,4,3,4,115,
        8,4,1,4,5,4,118,8,4,10,4,12,4,121,9,4,1,5,1,5,1,5,5,5,126,8,5,10,
        5,12,5,129,9,5,1,6,1,6,1,6,5,6,134,8,6,10,6,12,6,137,9,6,1,7,1,7,
        1,7,1,7,1,7,5,7,144,8,7,10,7,12,7,147,9,7,1,8,1,8,5,8,151,8,8,10,
        8,12,8,154,9,8,1,8,5,8,157,8,8,10,8,12,8,160,9,8,1,9,1,9,1,9,1,9,
        5,9,166,8,9,10,9,12,9,169,9,9,1,10,1,10,1,10,5,10,174,8,10,10,10,
        12,10,177,9,10,1,11,1,11,1,11,5,11,182,8,11,10,11,12,11,185,9,11,
        1,12,1,12,1,12,5,12,190,8,12,10,12,12,12,193,9,12,1,13,1,13,5,13,
        197,8,13,10,13,12,13,200,9,13,1,13,5,13,203,8,13,10,13,12,13,206,
        9,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,214,8,14,10,14,12,14,217,
        9,14,1,14,5,14,220,8,14,10,14,12,14,223,9,14,1,15,5,15,226,8,15,
        10,15,12,15,229,9,15,1,16,3,16,232,8,16,1,16,1,16,1,16,3,16,237,
        8,16,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,0,0,25,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,0,1,2,0,11,11,13,13,266,0,53,1,0,0,0,2,67,1,0,0,0,4,91,1,0,0,
        0,6,95,1,0,0,0,8,102,1,0,0,0,10,122,1,0,0,0,12,130,1,0,0,0,14,138,
        1,0,0,0,16,148,1,0,0,0,18,161,1,0,0,0,20,170,1,0,0,0,22,178,1,0,
        0,0,24,186,1,0,0,0,26,194,1,0,0,0,28,207,1,0,0,0,30,227,1,0,0,0,
        32,231,1,0,0,0,34,238,1,0,0,0,36,240,1,0,0,0,38,244,1,0,0,0,40,250,
        1,0,0,0,42,252,1,0,0,0,44,254,1,0,0,0,46,256,1,0,0,0,48,258,1,0,
        0,0,50,52,5,16,0,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,
        54,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,56,58,3,10,5,0,57,56,1,0,
        0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,61,3,2,1,0,60,59,1,0,0,0,61,62,
        1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,0,0,1,
        65,1,1,0,0,0,66,68,3,12,6,0,67,66,1,0,0,0,67,68,1,0,0,0,68,81,1,
        0,0,0,69,73,3,4,2,0,70,72,3,8,4,0,71,70,1,0,0,0,72,75,1,0,0,0,73,
        71,1,0,0,0,73,74,1,0,0,0,74,82,1,0,0,0,75,73,1,0,0,0,76,78,3,8,4,
        0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,
        1,0,0,0,81,69,1,0,0,0,81,77,1,0,0,0,82,86,1,0,0,0,83,85,3,28,14,
        0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,3,1,
        0,0,0,88,86,1,0,0,0,89,92,3,6,3,0,90,92,3,18,9,0,91,89,1,0,0,0,91,
        90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,5,1,0,0,
        0,95,99,3,14,7,0,96,98,3,16,8,0,97,96,1,0,0,0,98,101,1,0,0,0,99,
        97,1,0,0,0,99,100,1,0,0,0,100,7,1,0,0,0,101,99,1,0,0,0,102,104,3,
        20,10,0,103,105,3,22,11,0,104,103,1,0,0,0,104,105,1,0,0,0,105,106,
        1,0,0,0,106,110,3,24,12,0,107,109,3,16,8,0,108,107,1,0,0,0,109,112,
        1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,114,1,0,0,0,112,110,
        1,0,0,0,113,115,3,26,13,0,114,113,1,0,0,0,114,115,1,0,0,0,115,119,
        1,0,0,0,116,118,3,18,9,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,9,1,0,0,0,121,119,1,0,0,0,122,123,5,
        1,0,0,123,127,3,42,21,0,124,126,5,16,0,0,125,124,1,0,0,0,126,129,
        1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,11,1,0,0,0,129,127,1,
        0,0,0,130,131,5,2,0,0,131,135,3,46,23,0,132,134,5,16,0,0,133,132,
        1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,13,1,
        0,0,0,137,135,1,0,0,0,138,139,5,3,0,0,139,140,3,40,20,0,140,141,
        5,14,0,0,141,145,3,30,15,0,142,144,5,16,0,0,143,142,1,0,0,0,144,
        147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,15,1,0,0,0,147,145,
        1,0,0,0,148,152,5,4,0,0,149,151,3,38,19,0,150,149,1,0,0,0,151,154,
        1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,158,1,0,0,0,154,152,
        1,0,0,0,155,157,5,16,0,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,
        1,0,0,0,158,159,1,0,0,0,159,17,1,0,0,0,160,158,1,0,0,0,161,162,5,
        5,0,0,162,163,3,42,21,0,163,167,3,40,20,0,164,166,5,16,0,0,165,164,
        1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,19,1,
        0,0,0,169,167,1,0,0,0,170,171,5,6,0,0,171,175,3,44,22,0,172,174,
        5,16,0,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,
        1,0,0,0,176,21,1,0,0,0,177,175,1,0,0,0,178,179,5,7,0,0,179,183,3,
        40,20,0,180,182,5,16,0,0,181,180,1,0,0,0,182,185,1,0,0,0,183,181,
        1,0,0,0,183,184,1,0,0,0,184,23,1,0,0,0,185,183,1,0,0,0,186,187,5,
        8,0,0,187,191,3,30,15,0,188,190,5,16,0,0,189,188,1,0,0,0,190,193,
        1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,25,1,0,0,0,193,191,1,
        0,0,0,194,198,5,9,0,0,195,197,3,32,16,0,196,195,1,0,0,0,197,200,
        1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,204,1,0,0,0,200,198,
        1,0,0,0,201,203,5,16,0,0,202,201,1,0,0,0,203,206,1,0,0,0,204,202,
        1,0,0,0,204,205,1,0,0,0,205,27,1,0,0,0,206,204,1,0,0,0,207,208,5,
        10,0,0,208,209,3,42,21,0,209,215,5,14,0,0,210,211,3,44,22,0,211,
        212,3,32,16,0,212,214,1,0,0,0,213,210,1,0,0,0,214,217,1,0,0,0,215,
        213,1,0,0,0,215,216,1,0,0,0,216,221,1,0,0,0,217,215,1,0,0,0,218,
        220,5,16,0,0,219,218,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,
        222,1,0,0,0,222,29,1,0,0,0,223,221,1,0,0,0,224,226,3,34,17,0,225,
        224,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        31,1,0,0,0,229,227,1,0,0,0,230,232,3,48,24,0,231,230,1,0,0,0,231,
        232,1,0,0,0,232,233,1,0,0,0,233,236,3,40,20,0,234,235,5,14,0,0,235,
        237,3,36,18,0,236,234,1,0,0,0,236,237,1,0,0,0,237,33,1,0,0,0,238,
        239,3,40,20,0,239,35,1,0,0,0,240,241,3,40,20,0,241,242,5,14,0,0,
        242,243,3,40,20,0,243,37,1,0,0,0,244,245,3,40,20,0,245,246,5,14,
        0,0,246,247,3,40,20,0,247,248,5,14,0,0,248,249,3,40,20,0,249,39,
        1,0,0,0,250,251,5,11,0,0,251,41,1,0,0,0,252,253,5,11,0,0,253,43,
        1,0,0,0,254,255,7,0,0,0,255,45,1,0,0,0,256,257,5,12,0,0,257,47,1,
        0,0,0,258,259,5,15,0,0,259,49,1,0,0,0,31,53,57,62,67,73,79,81,86,
        91,93,99,104,110,114,119,127,135,145,152,158,167,175,183,191,198,
        204,215,221,227,231,236
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TARG'", "'FILE'", "'ABS'", "'LOC'", 
                     "'NTRY'", "'NAME'", "'ALIG'", "'DATA'", "'REL'", "'XTRN'", 
                     "<INVALID>", "<INVALID>", "'$abs'", "':'", "'-'" ]

    symbolicNames = [ "<INVALID>", "TARG", "FILE", "ABS", "LOC", "NTRY", 
                      "NAME", "ALIG", "DATA", "REL", "XTRN", "WORD", "FP_BASE64", 
                      "ABS_SECTION", "COLON", "MINUS", "NEWLINE", "WS" ]

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
    RULE_entry_usage = 16
    RULE_byte = 17
    RULE_range = 18
    RULE_location = 19
    RULE_number = 20
    RULE_label = 21
    RULE_section = 22
    RULE_path_base64 = 23
    RULE_minus = 24

    ruleNames =  [ "object_file", "object_block", "asect_block", "abs_block", 
                   "rsect_block", "targ_record", "source_record", "abs_record", 
                   "loc_record", "ntry_record", "name_record", "alig_record", 
                   "data_record", "rel_record", "xtrn_record", "data", "entry_usage", 
                   "byte", "range", "location", "number", "label", "section", 
                   "path_base64", "minus" ]

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
    FP_BASE64=12
    ABS_SECTION=13
    COLON=14
    MINUS=15
    NEWLINE=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Object_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ObjectFileParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
            while _la==16:
                self.state = 50
                self.match(ObjectFileParser.NEWLINE)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 56
                self.targ_record()


            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.object_block()
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 108) != 0)):
                    break

            self.state = 64
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
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 66
                self.source_record()


            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5]:
                self.state = 69
                self.asect_block()
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 70
                        self.rsect_block() 
                    self.state = 75
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            elif token in [6]:
                self.state = 77 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 76
                        self.rsect_block()

                    else:
                        raise NoViableAltException(self)
                    self.state = 79 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 83
                self.xtrn_record()
                self.state = 88
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
            self.state = 91 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 91
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 89
                        self.abs_block()
                        pass
                    elif token in [5]:
                        self.state = 90
                        self.ntry_record()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 93 
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
            self.state = 95
            self.abs_record()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 96
                self.loc_record()
                self.state = 101
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
            self.state = 102
            self.name_record()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 103
                self.alig_record()


            self.state = 106
            self.data_record()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 107
                self.loc_record()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 113
                self.rel_record()


            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 116
                    self.ntry_record() 
                self.state = 121
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ObjectFileParser.TARG)
            self.state = 123
            self.label()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 124
                self.match(ObjectFileParser.NEWLINE)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def path_base64(self):
            return self.getTypedRuleContext(ObjectFileParser.Path_base64Context,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ObjectFileParser.FILE)
            self.state = 131
            self.path_base64()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 132
                self.match(ObjectFileParser.NEWLINE)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def number(self):
            return self.getTypedRuleContext(ObjectFileParser.NumberContext,0)


        def COLON(self):
            return self.getToken(ObjectFileParser.COLON, 0)

        def data(self):
            return self.getTypedRuleContext(ObjectFileParser.DataContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
            self.state = 138
            self.match(ObjectFileParser.ABS)
            self.state = 139
            self.number()
            self.state = 140
            self.match(ObjectFileParser.COLON)
            self.state = 141
            self.data()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 142
                self.match(ObjectFileParser.NEWLINE)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def location(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.LocationContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.LocationContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
            self.state = 148
            self.match(ObjectFileParser.LOC)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 149
                self.location()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 155
                self.match(ObjectFileParser.NEWLINE)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ObjectFileParser.NTRY)
            self.state = 162
            self.label()
            self.state = 163
            self.number()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 164
                self.match(ObjectFileParser.NEWLINE)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ObjectFileParser.NAME)
            self.state = 171
            self.section()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 172
                self.match(ObjectFileParser.NEWLINE)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ObjectFileParser.ALIG)
            self.state = 179
            self.number()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 180
                self.match(ObjectFileParser.NEWLINE)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
            self.state = 186
            self.match(ObjectFileParser.DATA)
            self.state = 187
            self.data()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 188
                self.match(ObjectFileParser.NEWLINE)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def entry_usage(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Entry_usageContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Entry_usageContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
            self.state = 194
            self.match(ObjectFileParser.REL)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==15:
                self.state = 195
                self.entry_usage()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 201
                self.match(ObjectFileParser.NEWLINE)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

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
            self.state = 207
            self.match(ObjectFileParser.XTRN)
            self.state = 208
            self.label()
            self.state = 209
            self.match(ObjectFileParser.COLON)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==13:
                self.state = 210
                self.section()
                self.state = 211
                self.entry_usage()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 218
                self.match(ObjectFileParser.NEWLINE)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def byte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.ByteContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.ByteContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 224
                self.byte()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def getRuleIndex(self):
            return ObjectFileParser.RULE_entry_usage

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry_usage" ):
                return visitor.visitEntry_usage(self)
            else:
                return visitor.visitChildren(self)




    def entry_usage(self):

        localctx = ObjectFileParser.Entry_usageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_entry_usage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 230
                self.minus()


            self.state = 233
            self.number()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 234
                self.match(ObjectFileParser.COLON)
                self.state = 235
                self.range_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ByteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(ObjectFileParser.NumberContext,0)


        def getRuleIndex(self):
            return ObjectFileParser.RULE_byte

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByte" ):
                return visitor.visitByte(self)
            else:
                return visitor.visitChildren(self)




    def byte(self):

        localctx = ObjectFileParser.ByteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_byte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.number()
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
            self.state = 240
            self.number()
            self.state = 241
            self.match(ObjectFileParser.COLON)
            self.state = 242
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
        self.enterRule(localctx, 38, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.number()
            self.state = 245
            self.match(ObjectFileParser.COLON)
            self.state = 246
            self.number()
            self.state = 247
            self.match(ObjectFileParser.COLON)
            self.state = 248
            self.number()
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
        self.enterRule(localctx, 40, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
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

        def getRuleIndex(self):
            return ObjectFileParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = ObjectFileParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(ObjectFileParser.WORD)
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
        self.enterRule(localctx, 44, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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


    class Path_base64Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FP_BASE64(self):
            return self.getToken(ObjectFileParser.FP_BASE64, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_path_base64

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath_base64" ):
                return visitor.visitPath_base64(self)
            else:
                return visitor.visitChildren(self)




    def path_base64(self):

        localctx = ObjectFileParser.Path_base64Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_path_base64)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ObjectFileParser.FP_BASE64)
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
        self.enterRule(localctx, 48, self.RULE_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ObjectFileParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





