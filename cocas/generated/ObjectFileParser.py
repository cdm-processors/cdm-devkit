# Generated from ./grammar/ObjectFile.g4 by ANTLR 4.13.0
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
        4,1,14,197,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,3,0,46,8,0,1,0,1,0,5,0,50,8,0,10,0,12,0,53,
        9,0,1,0,4,0,56,8,0,11,0,12,0,57,3,0,60,8,0,1,0,5,0,63,8,0,10,0,12,
        0,66,9,0,1,0,1,0,1,1,1,1,4,1,72,8,1,11,1,12,1,73,1,2,1,2,3,2,78,
        8,2,1,2,1,2,1,2,5,2,83,8,2,10,2,12,2,86,9,2,1,3,1,3,1,3,5,3,91,8,
        3,10,3,12,3,94,9,3,1,4,1,4,1,4,1,4,1,4,5,4,101,8,4,10,4,12,4,104,
        9,4,1,5,1,5,1,5,1,5,5,5,110,8,5,10,5,12,5,113,9,5,1,6,1,6,1,6,5,
        6,118,8,6,10,6,12,6,121,9,6,1,7,1,7,1,7,5,7,126,8,7,10,7,12,7,129,
        9,7,1,8,1,8,1,8,5,8,134,8,8,10,8,12,8,137,9,8,1,9,1,9,5,9,141,8,
        9,10,9,12,9,144,9,9,1,9,5,9,147,8,9,10,9,12,9,150,9,9,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,158,8,10,10,10,12,10,161,9,10,1,10,5,10,
        164,8,10,10,10,12,10,167,9,10,1,11,5,11,170,8,11,10,11,12,11,173,
        9,11,1,12,3,12,176,8,12,1,12,1,12,1,12,3,12,181,8,12,1,13,1,13,1,
        14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,0,
        0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,1,1,0,
        9,10,200,0,41,1,0,0,0,2,71,1,0,0,0,4,75,1,0,0,0,6,87,1,0,0,0,8,95,
        1,0,0,0,10,105,1,0,0,0,12,114,1,0,0,0,14,122,1,0,0,0,16,130,1,0,
        0,0,18,138,1,0,0,0,20,151,1,0,0,0,22,171,1,0,0,0,24,175,1,0,0,0,
        26,182,1,0,0,0,28,184,1,0,0,0,30,188,1,0,0,0,32,190,1,0,0,0,34,192,
        1,0,0,0,36,194,1,0,0,0,38,40,5,13,0,0,39,38,1,0,0,0,40,43,1,0,0,
        0,41,39,1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,44,46,
        3,6,3,0,45,44,1,0,0,0,45,46,1,0,0,0,46,59,1,0,0,0,47,51,3,2,1,0,
        48,50,3,4,2,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,
        0,0,0,52,60,1,0,0,0,53,51,1,0,0,0,54,56,3,4,2,0,55,54,1,0,0,0,56,
        57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,47,1,0,0,
        0,59,55,1,0,0,0,60,64,1,0,0,0,61,63,3,20,10,0,62,61,1,0,0,0,63,66,
        1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,
        67,68,5,0,0,1,68,1,1,0,0,0,69,72,3,8,4,0,70,72,3,10,5,0,71,69,1,
        0,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,
        3,1,0,0,0,75,77,3,12,6,0,76,78,3,14,7,0,77,76,1,0,0,0,77,78,1,0,
        0,0,78,79,1,0,0,0,79,80,3,16,8,0,80,84,3,18,9,0,81,83,3,10,5,0,82,
        81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,5,1,0,0,
        0,86,84,1,0,0,0,87,88,5,1,0,0,88,92,3,34,17,0,89,91,5,13,0,0,90,
        89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,7,1,0,0,
        0,94,92,1,0,0,0,95,96,5,2,0,0,96,97,3,30,15,0,97,98,5,11,0,0,98,
        102,3,22,11,0,99,101,5,13,0,0,100,99,1,0,0,0,101,104,1,0,0,0,102,
        100,1,0,0,0,102,103,1,0,0,0,103,9,1,0,0,0,104,102,1,0,0,0,105,106,
        5,3,0,0,106,107,3,32,16,0,107,111,3,30,15,0,108,110,5,13,0,0,109,
        108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,
        11,1,0,0,0,113,111,1,0,0,0,114,115,5,4,0,0,115,119,3,34,17,0,116,
        118,5,13,0,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,
        120,1,0,0,0,120,13,1,0,0,0,121,119,1,0,0,0,122,123,5,5,0,0,123,127,
        3,30,15,0,124,126,5,13,0,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,15,1,0,0,0,129,127,1,0,0,0,130,131,5,
        6,0,0,131,135,3,22,11,0,132,134,5,13,0,0,133,132,1,0,0,0,134,137,
        1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,17,1,0,0,0,137,135,1,
        0,0,0,138,142,5,7,0,0,139,141,3,24,12,0,140,139,1,0,0,0,141,144,
        1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,148,1,0,0,0,144,142,
        1,0,0,0,145,147,5,13,0,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,19,1,0,0,0,150,148,1,0,0,0,151,152,5,
        8,0,0,152,153,3,32,16,0,153,159,5,11,0,0,154,155,3,34,17,0,155,156,
        3,24,12,0,156,158,1,0,0,0,157,154,1,0,0,0,158,161,1,0,0,0,159,157,
        1,0,0,0,159,160,1,0,0,0,160,165,1,0,0,0,161,159,1,0,0,0,162,164,
        5,13,0,0,163,162,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,21,1,0,0,0,167,165,1,0,0,0,168,170,3,26,13,0,169,168,
        1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,23,1,
        0,0,0,173,171,1,0,0,0,174,176,3,36,18,0,175,174,1,0,0,0,175,176,
        1,0,0,0,176,177,1,0,0,0,177,180,3,30,15,0,178,179,5,11,0,0,179,181,
        3,28,14,0,180,178,1,0,0,0,180,181,1,0,0,0,181,25,1,0,0,0,182,183,
        3,30,15,0,183,27,1,0,0,0,184,185,3,30,15,0,185,186,5,11,0,0,186,
        187,3,30,15,0,187,29,1,0,0,0,188,189,5,9,0,0,189,31,1,0,0,0,190,
        191,5,9,0,0,191,33,1,0,0,0,192,193,7,0,0,0,193,35,1,0,0,0,194,195,
        5,12,0,0,195,37,1,0,0,0,23,41,45,51,57,59,64,71,73,77,84,92,102,
        111,119,127,135,142,148,159,165,171,175,180
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TARG'", "'ABS'", "'NTRY'", "'NAME'", 
                     "'ALIG'", "'DATA'", "'REL'", "'XTRN'", "<INVALID>", 
                     "'$abs'", "':'", "'-'" ]

    symbolicNames = [ "<INVALID>", "TARG", "ABS", "NTRY", "NAME", "ALIG", 
                      "DATA", "REL", "XTRN", "WORD", "ABS_SECTION", "COLON", 
                      "MINUS", "NEWLINE", "WS" ]

    RULE_object_file = 0
    RULE_asect_block = 1
    RULE_rsect_block = 2
    RULE_targ_record = 3
    RULE_abs_record = 4
    RULE_ntry_record = 5
    RULE_name_record = 6
    RULE_alig_record = 7
    RULE_data_record = 8
    RULE_rel_record = 9
    RULE_xtrn_record = 10
    RULE_data = 11
    RULE_entry_usage = 12
    RULE_byte = 13
    RULE_range = 14
    RULE_number = 15
    RULE_label = 16
    RULE_name = 17
    RULE_minus = 18

    ruleNames =  [ "object_file", "asect_block", "rsect_block", "targ_record", 
                   "abs_record", "ntry_record", "name_record", "alig_record", 
                   "data_record", "rel_record", "xtrn_record", "data", "entry_usage", 
                   "byte", "range", "number", "label", "name", "minus" ]

    EOF = Token.EOF
    TARG=1
    ABS=2
    NTRY=3
    NAME=4
    ALIG=5
    DATA=6
    REL=7
    XTRN=8
    WORD=9
    ABS_SECTION=10
    COLON=11
    MINUS=12
    NEWLINE=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Object_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ObjectFileParser.EOF, 0)

        def asect_block(self):
            return self.getTypedRuleContext(ObjectFileParser.Asect_blockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ObjectFileParser.NEWLINE)
            else:
                return self.getToken(ObjectFileParser.NEWLINE, i)

        def targ_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Targ_recordContext,0)


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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 38
                self.match(ObjectFileParser.NEWLINE)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 44
                self.targ_record()


            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.state = 47
                self.asect_block()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 48
                    self.rsect_block()
                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [4]:
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 54
                    self.rsect_block()
                    self.state = 57 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                pass
            else:
                raise NoViableAltException(self)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 61
                self.xtrn_record()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(ObjectFileParser.EOF)
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

        def abs_record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.Abs_recordContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.Abs_recordContext,i)


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
        self.enterRule(localctx, 2, self.RULE_asect_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 69
                    self.abs_record()
                    pass
                elif token in [3]:
                    self.state = 70
                    self.ntry_record()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==3):
                    break

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


        def rel_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Rel_recordContext,0)


        def alig_record(self):
            return self.getTypedRuleContext(ObjectFileParser.Alig_recordContext,0)


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
        self.enterRule(localctx, 4, self.RULE_rsect_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.name_record()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 76
                self.alig_record()


            self.state = 79
            self.data_record()
            self.state = 80
            self.rel_record()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 81
                self.ntry_record()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def name(self):
            return self.getTypedRuleContext(ObjectFileParser.NameContext,0)


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
        self.enterRule(localctx, 6, self.RULE_targ_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ObjectFileParser.TARG)
            self.state = 88
            self.name()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 89
                self.match(ObjectFileParser.NEWLINE)
                self.state = 94
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
        self.enterRule(localctx, 8, self.RULE_abs_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ObjectFileParser.ABS)
            self.state = 96
            self.number()
            self.state = 97
            self.match(ObjectFileParser.COLON)
            self.state = 98
            self.data()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 99
                self.match(ObjectFileParser.NEWLINE)
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
        self.enterRule(localctx, 10, self.RULE_ntry_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ObjectFileParser.NTRY)
            self.state = 106
            self.label()
            self.state = 107
            self.number()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 108
                self.match(ObjectFileParser.NEWLINE)
                self.state = 113
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

        def name(self):
            return self.getTypedRuleContext(ObjectFileParser.NameContext,0)


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
        self.enterRule(localctx, 12, self.RULE_name_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ObjectFileParser.NAME)
            self.state = 115
            self.name()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 116
                self.match(ObjectFileParser.NEWLINE)
                self.state = 121
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
        self.enterRule(localctx, 14, self.RULE_alig_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ObjectFileParser.ALIG)
            self.state = 123
            self.number()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
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
        self.enterRule(localctx, 16, self.RULE_data_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ObjectFileParser.DATA)
            self.state = 131
            self.data()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
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
        self.enterRule(localctx, 18, self.RULE_rel_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ObjectFileParser.REL)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==12:
                self.state = 139
                self.entry_usage()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 145
                self.match(ObjectFileParser.NEWLINE)
                self.state = 150
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

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjectFileParser.NameContext)
            else:
                return self.getTypedRuleContext(ObjectFileParser.NameContext,i)


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
        self.enterRule(localctx, 20, self.RULE_xtrn_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ObjectFileParser.XTRN)
            self.state = 152
            self.label()
            self.state = 153
            self.match(ObjectFileParser.COLON)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 154
                self.name()
                self.state = 155
                self.entry_usage()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 162
                self.match(ObjectFileParser.NEWLINE)
                self.state = 167
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
        self.enterRule(localctx, 22, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 168
                self.byte()
                self.state = 173
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
        self.enterRule(localctx, 24, self.RULE_entry_usage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 174
                self.minus()


            self.state = 177
            self.number()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 178
                self.match(ObjectFileParser.COLON)
                self.state = 179
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
        self.enterRule(localctx, 26, self.RULE_byte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
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
        self.enterRule(localctx, 28, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.number()
            self.state = 185
            self.match(ObjectFileParser.COLON)
            self.state = 186
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
        self.enterRule(localctx, 30, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
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
        self.enterRule(localctx, 32, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(ObjectFileParser.WORD)
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

        def WORD(self):
            return self.getToken(ObjectFileParser.WORD, 0)

        def ABS_SECTION(self):
            return self.getToken(ObjectFileParser.ABS_SECTION, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = ObjectFileParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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
        self.enterRule(localctx, 36, self.RULE_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ObjectFileParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





