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
        4,1,17,218,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,3,0,52,8,0,1,0,
        3,0,55,8,0,1,0,4,0,58,8,0,11,0,12,0,59,1,0,1,0,1,1,3,1,65,8,1,1,
        1,1,1,5,1,69,8,1,10,1,12,1,72,9,1,1,1,4,1,75,8,1,11,1,12,1,76,3,
        1,79,8,1,1,1,5,1,82,8,1,10,1,12,1,85,9,1,1,2,1,2,4,2,89,8,2,11,2,
        12,2,90,1,3,1,3,5,3,95,8,3,10,3,12,3,98,9,3,1,4,1,4,3,4,102,8,4,
        1,4,1,4,5,4,106,8,4,10,4,12,4,109,9,4,1,4,3,4,112,8,4,1,4,5,4,115,
        8,4,10,4,12,4,118,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,5,8,136,8,8,10,8,12,8,139,9,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,13,1,13,5,13,162,8,13,10,13,12,13,165,9,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,5,14,175,8,14,10,14,12,14,178,9,14,
        1,14,1,14,1,15,5,15,183,8,15,10,15,12,15,186,9,15,1,16,3,16,189,
        8,16,1,16,1,16,1,16,3,16,194,8,16,1,17,1,17,1,18,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,
        1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,0,1,2,0,11,11,13,13,213,0,51,1,
        0,0,0,2,64,1,0,0,0,4,88,1,0,0,0,6,92,1,0,0,0,8,99,1,0,0,0,10,119,
        1,0,0,0,12,123,1,0,0,0,14,127,1,0,0,0,16,133,1,0,0,0,18,142,1,0,
        0,0,20,147,1,0,0,0,22,151,1,0,0,0,24,155,1,0,0,0,26,159,1,0,0,0,
        28,168,1,0,0,0,30,184,1,0,0,0,32,188,1,0,0,0,34,195,1,0,0,0,36,197,
        1,0,0,0,38,201,1,0,0,0,40,207,1,0,0,0,42,209,1,0,0,0,44,211,1,0,
        0,0,46,213,1,0,0,0,48,215,1,0,0,0,50,52,5,16,0,0,51,50,1,0,0,0,51,
        52,1,0,0,0,52,54,1,0,0,0,53,55,3,10,5,0,54,53,1,0,0,0,54,55,1,0,
        0,0,55,57,1,0,0,0,56,58,3,2,1,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,
        1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,0,0,1,62,1,1,0,0,0,63,
        65,3,12,6,0,64,63,1,0,0,0,64,65,1,0,0,0,65,78,1,0,0,0,66,70,3,4,
        2,0,67,69,3,8,4,0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,79,1,0,0,0,72,70,1,0,0,0,73,75,3,8,4,0,74,73,1,0,0,0,
        75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,66,1,
        0,0,0,78,74,1,0,0,0,79,83,1,0,0,0,80,82,3,28,14,0,81,80,1,0,0,0,
        82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,3,1,0,0,0,85,83,1,0,
        0,0,86,89,3,6,3,0,87,89,3,18,9,0,88,86,1,0,0,0,88,87,1,0,0,0,89,
        90,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,5,1,0,0,0,92,96,3,14,7,
        0,93,95,3,16,8,0,94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,
        1,0,0,0,97,7,1,0,0,0,98,96,1,0,0,0,99,101,3,20,10,0,100,102,3,22,
        11,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,107,3,24,
        12,0,104,106,3,16,8,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,
        0,0,0,107,108,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,110,112,3,
        26,13,0,111,110,1,0,0,0,111,112,1,0,0,0,112,116,1,0,0,0,113,115,
        3,18,9,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,
        1,0,0,0,117,9,1,0,0,0,118,116,1,0,0,0,119,120,5,1,0,0,120,121,3,
        42,21,0,121,122,5,16,0,0,122,11,1,0,0,0,123,124,5,2,0,0,124,125,
        3,46,23,0,125,126,5,16,0,0,126,13,1,0,0,0,127,128,5,3,0,0,128,129,
        3,40,20,0,129,130,5,14,0,0,130,131,3,30,15,0,131,132,5,16,0,0,132,
        15,1,0,0,0,133,137,5,4,0,0,134,136,3,38,19,0,135,134,1,0,0,0,136,
        139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,
        137,1,0,0,0,140,141,5,16,0,0,141,17,1,0,0,0,142,143,5,5,0,0,143,
        144,3,42,21,0,144,145,3,40,20,0,145,146,5,16,0,0,146,19,1,0,0,0,
        147,148,5,6,0,0,148,149,3,44,22,0,149,150,5,16,0,0,150,21,1,0,0,
        0,151,152,5,7,0,0,152,153,3,40,20,0,153,154,5,16,0,0,154,23,1,0,
        0,0,155,156,5,8,0,0,156,157,3,30,15,0,157,158,5,16,0,0,158,25,1,
        0,0,0,159,163,5,9,0,0,160,162,3,32,16,0,161,160,1,0,0,0,162,165,
        1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,163,
        1,0,0,0,166,167,5,16,0,0,167,27,1,0,0,0,168,169,5,10,0,0,169,170,
        3,42,21,0,170,176,5,14,0,0,171,172,3,44,22,0,172,173,3,32,16,0,173,
        175,1,0,0,0,174,171,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,
        177,1,0,0,0,177,179,1,0,0,0,178,176,1,0,0,0,179,180,5,16,0,0,180,
        29,1,0,0,0,181,183,3,34,17,0,182,181,1,0,0,0,183,186,1,0,0,0,184,
        182,1,0,0,0,184,185,1,0,0,0,185,31,1,0,0,0,186,184,1,0,0,0,187,189,
        3,48,24,0,188,187,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,193,
        3,40,20,0,191,192,5,14,0,0,192,194,3,36,18,0,193,191,1,0,0,0,193,
        194,1,0,0,0,194,33,1,0,0,0,195,196,3,40,20,0,196,35,1,0,0,0,197,
        198,3,40,20,0,198,199,5,14,0,0,199,200,3,40,20,0,200,37,1,0,0,0,
        201,202,3,40,20,0,202,203,5,14,0,0,203,204,3,40,20,0,204,205,5,14,
        0,0,205,206,3,40,20,0,206,39,1,0,0,0,207,208,5,11,0,0,208,41,1,0,
        0,0,209,210,5,11,0,0,210,43,1,0,0,0,211,212,7,0,0,0,212,45,1,0,0,
        0,213,214,5,12,0,0,214,47,1,0,0,0,215,216,5,15,0,0,216,49,1,0,0,
        0,21,51,54,59,64,70,76,78,83,88,90,96,101,107,111,116,137,163,176,
        184,188,193
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
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 50
                self.match(ObjectFileParser.NEWLINE)


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 53
                self.targ_record()


            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.object_block()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 108) != 0)):
                    break

            self.state = 61
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
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 63
                self.source_record()


            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5]:
                self.state = 66
                self.asect_block()
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 67
                        self.rsect_block() 
                    self.state = 72
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            elif token in [6]:
                self.state = 74 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 73
                        self.rsect_block()

                    else:
                        raise NoViableAltException(self)
                    self.state = 76 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 80
                self.xtrn_record()
                self.state = 85
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
            self.state = 88 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 88
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 86
                        self.abs_block()
                        pass
                    elif token in [5]:
                        self.state = 87
                        self.ntry_record()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 90 
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
            self.state = 92
            self.abs_record()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 93
                self.loc_record()
                self.state = 98
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
            self.state = 99
            self.name_record()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 100
                self.alig_record()


            self.state = 103
            self.data_record()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 104
                self.loc_record()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 110
                self.rel_record()


            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 113
                    self.ntry_record() 
                self.state = 118
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
            self.state = 119
            self.match(ObjectFileParser.TARG)
            self.state = 120
            self.label()
            self.state = 121
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

        def path_base64(self):
            return self.getTypedRuleContext(ObjectFileParser.Path_base64Context,0)


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
            self.state = 123
            self.match(ObjectFileParser.FILE)
            self.state = 124
            self.path_base64()
            self.state = 125
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

        def number(self):
            return self.getTypedRuleContext(ObjectFileParser.NumberContext,0)


        def COLON(self):
            return self.getToken(ObjectFileParser.COLON, 0)

        def data(self):
            return self.getTypedRuleContext(ObjectFileParser.DataContext,0)


        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ObjectFileParser.ABS)
            self.state = 128
            self.number()
            self.state = 129
            self.match(ObjectFileParser.COLON)
            self.state = 130
            self.data()
            self.state = 131
            self.match(ObjectFileParser.NEWLINE)
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
            self.state = 133
            self.match(ObjectFileParser.LOC)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 134
                self.location()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
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
            self.state = 142
            self.match(ObjectFileParser.NTRY)
            self.state = 143
            self.label()
            self.state = 144
            self.number()
            self.state = 145
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
            self.state = 147
            self.match(ObjectFileParser.NAME)
            self.state = 148
            self.section()
            self.state = 149
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
            self.state = 151
            self.match(ObjectFileParser.ALIG)
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


    class Data_recordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(ObjectFileParser.DATA, 0)

        def data(self):
            return self.getTypedRuleContext(ObjectFileParser.DataContext,0)


        def NEWLINE(self):
            return self.getToken(ObjectFileParser.NEWLINE, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ObjectFileParser.DATA)
            self.state = 156
            self.data()
            self.state = 157
            self.match(ObjectFileParser.NEWLINE)
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
            self.state = 159
            self.match(ObjectFileParser.REL)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==15:
                self.state = 160
                self.entry_usage()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
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
            self.state = 168
            self.match(ObjectFileParser.XTRN)
            self.state = 169
            self.label()
            self.state = 170
            self.match(ObjectFileParser.COLON)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==13:
                self.state = 171
                self.section()
                self.state = 172
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
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 181
                self.byte()
                self.state = 186
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
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 187
                self.minus()


            self.state = 190
            self.number()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 191
                self.match(ObjectFileParser.COLON)
                self.state = 192
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
            self.state = 195
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
            self.state = 197
            self.number()
            self.state = 198
            self.match(ObjectFileParser.COLON)
            self.state = 199
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
            self.state = 201
            self.number()
            self.state = 202
            self.match(ObjectFileParser.COLON)
            self.state = 203
            self.number()
            self.state = 204
            self.match(ObjectFileParser.COLON)
            self.state = 205
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
            self.state = 207
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
            self.state = 209
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
            self.state = 211
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
            self.state = 213
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
            self.state = 215
            self.match(ObjectFileParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





