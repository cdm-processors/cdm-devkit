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
        4,1,12,171,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,4,0,49,8,0,11,0,12,0,50,3,
        0,53,8,0,1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,4,1,65,
        8,1,11,1,12,1,66,1,2,1,2,1,2,1,2,5,2,73,8,2,10,2,12,2,76,9,2,1,3,
        1,3,1,3,1,3,1,3,5,3,83,8,3,10,3,12,3,86,9,3,1,4,1,4,1,4,1,4,5,4,
        92,8,4,10,4,12,4,95,9,4,1,5,1,5,1,5,5,5,100,8,5,10,5,12,5,103,9,
        5,1,6,1,6,1,6,5,6,108,8,6,10,6,12,6,111,9,6,1,7,1,7,5,7,115,8,7,
        10,7,12,7,118,9,7,1,7,5,7,121,8,7,10,7,12,7,124,9,7,1,8,1,8,1,8,
        1,8,1,8,1,8,5,8,132,8,8,10,8,12,8,135,9,8,1,8,5,8,138,8,8,10,8,12,
        8,141,9,8,1,9,5,9,144,8,9,10,9,12,9,147,9,9,1,10,3,10,150,8,10,1,
        10,1,10,1,10,3,10,155,8,10,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,
        13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,0,1,1,0,7,8,172,0,37,1,0,0,0,2,64,1,0,
        0,0,4,68,1,0,0,0,6,77,1,0,0,0,8,87,1,0,0,0,10,96,1,0,0,0,12,104,
        1,0,0,0,14,112,1,0,0,0,16,125,1,0,0,0,18,145,1,0,0,0,20,149,1,0,
        0,0,22,156,1,0,0,0,24,158,1,0,0,0,26,162,1,0,0,0,28,164,1,0,0,0,
        30,166,1,0,0,0,32,168,1,0,0,0,34,36,5,11,0,0,35,34,1,0,0,0,36,39,
        1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,52,1,0,0,0,39,37,1,0,0,0,
        40,44,3,2,1,0,41,43,3,4,2,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,
        0,0,0,44,45,1,0,0,0,45,53,1,0,0,0,46,44,1,0,0,0,47,49,3,4,2,0,48,
        47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,
        0,52,40,1,0,0,0,52,48,1,0,0,0,53,57,1,0,0,0,54,56,3,16,8,0,55,54,
        1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,
        59,57,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,65,3,6,3,0,63,65,3,8,
        4,0,64,62,1,0,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,
        1,0,0,0,67,3,1,0,0,0,68,69,3,10,5,0,69,70,3,12,6,0,70,74,3,14,7,
        0,71,73,3,8,4,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,5,1,0,0,0,76,74,1,0,0,0,77,78,5,1,0,0,78,79,3,26,13,0,
        79,80,5,9,0,0,80,84,3,18,9,0,81,83,5,11,0,0,82,81,1,0,0,0,83,86,
        1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,7,1,0,0,0,86,84,1,0,0,0,87,
        88,5,2,0,0,88,89,3,28,14,0,89,93,3,26,13,0,90,92,5,11,0,0,91,90,
        1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,9,1,0,0,0,95,
        93,1,0,0,0,96,97,5,3,0,0,97,101,3,30,15,0,98,100,5,11,0,0,99,98,
        1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,11,1,
        0,0,0,103,101,1,0,0,0,104,105,5,4,0,0,105,109,3,18,9,0,106,108,5,
        11,0,0,107,106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,
        0,0,0,110,13,1,0,0,0,111,109,1,0,0,0,112,116,5,5,0,0,113,115,3,20,
        10,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,
        0,0,117,122,1,0,0,0,118,116,1,0,0,0,119,121,5,11,0,0,120,119,1,0,
        0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,15,1,0,0,
        0,124,122,1,0,0,0,125,126,5,6,0,0,126,127,3,28,14,0,127,133,5,9,
        0,0,128,129,3,30,15,0,129,130,3,20,10,0,130,132,1,0,0,0,131,128,
        1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,139,
        1,0,0,0,135,133,1,0,0,0,136,138,5,11,0,0,137,136,1,0,0,0,138,141,
        1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,17,1,0,0,0,141,139,1,
        0,0,0,142,144,3,22,11,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,
        1,0,0,0,145,146,1,0,0,0,146,19,1,0,0,0,147,145,1,0,0,0,148,150,3,
        32,16,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,154,
        3,26,13,0,152,153,5,9,0,0,153,155,3,24,12,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,21,1,0,0,0,156,157,3,26,13,0,157,23,1,0,0,0,158,
        159,3,26,13,0,159,160,5,9,0,0,160,161,3,26,13,0,161,25,1,0,0,0,162,
        163,5,7,0,0,163,27,1,0,0,0,164,165,5,7,0,0,165,29,1,0,0,0,166,167,
        7,0,0,0,167,31,1,0,0,0,168,169,5,10,0,0,169,33,1,0,0,0,19,37,44,
        50,52,57,64,66,74,84,93,101,109,116,122,133,139,145,149,154
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ABS'", "'NTRY'", "'NAME'", "'DATA'", 
                     "'REL'", "'XTRN'", "<INVALID>", "'$abs'", "':'", "'-'" ]

    symbolicNames = [ "<INVALID>", "ABS", "NTRY", "NAME", "DATA", "REL", 
                      "XTRN", "WORD", "ABS_SECTION", "COLON", "MINUS", "NEWLINE", 
                      "WS" ]

    RULE_object_file = 0
    RULE_asect_block = 1
    RULE_rsect_block = 2
    RULE_abs_record = 3
    RULE_ntry_record = 4
    RULE_name_record = 5
    RULE_data_record = 6
    RULE_rel_record = 7
    RULE_xtrn_record = 8
    RULE_data = 9
    RULE_entry_usage = 10
    RULE_byte = 11
    RULE_range = 12
    RULE_number = 13
    RULE_label = 14
    RULE_name = 15
    RULE_minus = 16

    ruleNames =  [ "object_file", "asect_block", "rsect_block", "abs_record", 
                   "ntry_record", "name_record", "data_record", "rel_record", 
                   "xtrn_record", "data", "entry_usage", "byte", "range", 
                   "number", "label", "name", "minus" ]

    EOF = Token.EOF
    ABS=1
    NTRY=2
    NAME=3
    DATA=4
    REL=5
    XTRN=6
    WORD=7
    ABS_SECTION=8
    COLON=9
    MINUS=10
    NEWLINE=11
    WS=12

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 34
                self.match(ObjectFileParser.NEWLINE)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.state = 40
                self.asect_block()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 41
                    self.rsect_block()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 47
                    self.rsect_block()
                    self.state = 50 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                pass
            else:
                raise NoViableAltException(self)

            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 54
                self.xtrn_record()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
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
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 62
                    self.abs_record()
                    pass
                elif token in [2]:
                    self.state = 63
                    self.ntry_record()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
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
            self.state = 68
            self.name_record()
            self.state = 69
            self.data_record()
            self.state = 70
            self.rel_record()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 71
                self.ntry_record()
                self.state = 76
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
        self.enterRule(localctx, 6, self.RULE_abs_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ObjectFileParser.ABS)
            self.state = 78
            self.number()
            self.state = 79
            self.match(ObjectFileParser.COLON)
            self.state = 80
            self.data()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 81
                self.match(ObjectFileParser.NEWLINE)
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
        self.enterRule(localctx, 8, self.RULE_ntry_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ObjectFileParser.NTRY)
            self.state = 88
            self.label()
            self.state = 89
            self.number()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 90
                self.match(ObjectFileParser.NEWLINE)
                self.state = 95
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
        self.enterRule(localctx, 10, self.RULE_name_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ObjectFileParser.NAME)
            self.state = 97
            self.name()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 98
                self.match(ObjectFileParser.NEWLINE)
                self.state = 103
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
        self.enterRule(localctx, 12, self.RULE_data_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ObjectFileParser.DATA)
            self.state = 105
            self.data()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 106
                self.match(ObjectFileParser.NEWLINE)
                self.state = 111
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
        self.enterRule(localctx, 14, self.RULE_rel_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ObjectFileParser.REL)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==10:
                self.state = 113
                self.entry_usage()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 119
                self.match(ObjectFileParser.NEWLINE)
                self.state = 124
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
        self.enterRule(localctx, 16, self.RULE_xtrn_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ObjectFileParser.XTRN)
            self.state = 126
            self.label()
            self.state = 127
            self.match(ObjectFileParser.COLON)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 128
                self.name()
                self.state = 129
                self.entry_usage()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 136
                self.match(ObjectFileParser.NEWLINE)
                self.state = 141
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
        self.enterRule(localctx, 18, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 142
                self.byte()
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
        self.enterRule(localctx, 20, self.RULE_entry_usage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 148
                self.minus()


            self.state = 151
            self.number()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 152
                self.match(ObjectFileParser.COLON)
                self.state = 153
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
        self.enterRule(localctx, 22, self.RULE_byte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
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
        self.enterRule(localctx, 24, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.number()
            self.state = 159
            self.match(ObjectFileParser.COLON)
            self.state = 160
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
        self.enterRule(localctx, 26, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
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
        self.enterRule(localctx, 28, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
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
        self.enterRule(localctx, 30, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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
        self.enterRule(localctx, 32, self.RULE_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ObjectFileParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





