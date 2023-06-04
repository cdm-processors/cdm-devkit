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
        4,1,11,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,5,0,39,8,0,10,
        0,12,0,42,9,0,1,0,4,0,45,8,0,11,0,12,0,46,3,0,49,8,0,1,0,5,0,52,
        8,0,10,0,12,0,55,9,0,1,0,1,0,1,1,1,1,4,1,61,8,1,11,1,12,1,62,1,2,
        1,2,1,2,1,2,5,2,69,8,2,10,2,12,2,72,9,2,1,3,1,3,1,3,1,3,1,3,5,3,
        79,8,3,10,3,12,3,82,9,3,1,4,1,4,1,4,1,4,5,4,88,8,4,10,4,12,4,91,
        9,4,1,5,1,5,1,5,5,5,96,8,5,10,5,12,5,99,9,5,1,6,1,6,1,6,5,6,104,
        8,6,10,6,12,6,107,9,6,1,7,1,7,5,7,111,8,7,10,7,12,7,114,9,7,1,7,
        5,7,117,8,7,10,7,12,7,120,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,128,8,
        8,10,8,12,8,131,9,8,1,8,5,8,134,8,8,10,8,12,8,137,9,8,1,9,5,9,140,
        8,9,10,9,12,9,143,9,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,
        14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,1,
        1,0,7,8,156,0,33,1,0,0,0,2,60,1,0,0,0,4,64,1,0,0,0,6,73,1,0,0,0,
        8,83,1,0,0,0,10,92,1,0,0,0,12,100,1,0,0,0,14,108,1,0,0,0,16,121,
        1,0,0,0,18,141,1,0,0,0,20,144,1,0,0,0,22,146,1,0,0,0,24,148,1,0,
        0,0,26,150,1,0,0,0,28,152,1,0,0,0,30,32,5,10,0,0,31,30,1,0,0,0,32,
        35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,48,1,0,0,0,35,33,1,0,0,
        0,36,40,3,2,1,0,37,39,3,4,2,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,
        1,0,0,0,40,41,1,0,0,0,41,49,1,0,0,0,42,40,1,0,0,0,43,45,3,4,2,0,
        44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,
        0,0,0,48,36,1,0,0,0,48,44,1,0,0,0,49,53,1,0,0,0,50,52,3,16,8,0,51,
        50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,
        0,55,53,1,0,0,0,56,57,5,0,0,1,57,1,1,0,0,0,58,61,3,6,3,0,59,61,3,
        8,4,0,60,58,1,0,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,
        63,1,0,0,0,63,3,1,0,0,0,64,65,3,10,5,0,65,66,3,12,6,0,66,70,3,14,
        7,0,67,69,3,8,4,0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,5,1,0,0,0,72,70,1,0,0,0,73,74,5,1,0,0,74,75,3,24,12,0,
        75,76,5,9,0,0,76,80,3,18,9,0,77,79,5,10,0,0,78,77,1,0,0,0,79,82,
        1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,7,1,0,0,0,82,80,1,0,0,0,83,
        84,5,2,0,0,84,85,3,26,13,0,85,89,3,24,12,0,86,88,5,10,0,0,87,86,
        1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,9,1,0,0,0,91,
        89,1,0,0,0,92,93,5,3,0,0,93,97,3,28,14,0,94,96,5,10,0,0,95,94,1,
        0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,11,1,0,0,0,99,
        97,1,0,0,0,100,101,5,4,0,0,101,105,3,18,9,0,102,104,5,10,0,0,103,
        102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,
        13,1,0,0,0,107,105,1,0,0,0,108,112,5,5,0,0,109,111,3,20,10,0,110,
        109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,
        118,1,0,0,0,114,112,1,0,0,0,115,117,5,10,0,0,116,115,1,0,0,0,117,
        120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,15,1,0,0,0,120,118,
        1,0,0,0,121,122,5,6,0,0,122,123,3,26,13,0,123,129,5,9,0,0,124,125,
        3,28,14,0,125,126,3,20,10,0,126,128,1,0,0,0,127,124,1,0,0,0,128,
        131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,135,1,0,0,0,131,
        129,1,0,0,0,132,134,5,10,0,0,133,132,1,0,0,0,134,137,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,17,1,0,0,0,137,135,1,0,0,0,138,140,
        3,22,11,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,19,1,0,0,0,143,141,1,0,0,0,144,145,3,24,12,0,145,21,
        1,0,0,0,146,147,3,24,12,0,147,23,1,0,0,0,148,149,5,7,0,0,149,25,
        1,0,0,0,150,151,5,7,0,0,151,27,1,0,0,0,152,153,7,0,0,0,153,29,1,
        0,0,0,17,33,40,46,48,53,60,62,70,80,89,97,105,112,118,129,135,141
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ABS'", "'NTRY'", "'NAME'", "'DATA'", 
                     "'REL'", "'XTRN'", "<INVALID>", "'$abs'", "':'" ]

    symbolicNames = [ "<INVALID>", "ABS", "NTRY", "NAME", "DATA", "REL", 
                      "XTRN", "WORD", "ABS_SECTION", "COLON", "NEWLINE", 
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
    RULE_number = 12
    RULE_label = 13
    RULE_name = 14

    ruleNames =  [ "object_file", "asect_block", "rsect_block", "abs_record", 
                   "ntry_record", "name_record", "data_record", "rel_record", 
                   "xtrn_record", "data", "entry_usage", "byte", "number", 
                   "label", "name" ]

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
    NEWLINE=10
    WS=11

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
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 30
                self.match(ObjectFileParser.NEWLINE)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.state = 36
                self.asect_block()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 37
                    self.rsect_block()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 43
                    self.rsect_block()
                    self.state = 46 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                pass
            else:
                raise NoViableAltException(self)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 50
                self.xtrn_record()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
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
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 58
                    self.abs_record()
                    pass
                elif token in [2]:
                    self.state = 59
                    self.ntry_record()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 62 
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
            self.state = 64
            self.name_record()
            self.state = 65
            self.data_record()
            self.state = 66
            self.rel_record()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 67
                self.ntry_record()
                self.state = 72
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
            self.state = 73
            self.match(ObjectFileParser.ABS)
            self.state = 74
            self.number()
            self.state = 75
            self.match(ObjectFileParser.COLON)
            self.state = 76
            self.data()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 77
                self.match(ObjectFileParser.NEWLINE)
                self.state = 82
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
            self.state = 83
            self.match(ObjectFileParser.NTRY)
            self.state = 84
            self.label()
            self.state = 85
            self.number()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 86
                self.match(ObjectFileParser.NEWLINE)
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
            self.state = 92
            self.match(ObjectFileParser.NAME)
            self.state = 93
            self.name()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 94
                self.match(ObjectFileParser.NEWLINE)
                self.state = 99
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
            self.state = 100
            self.match(ObjectFileParser.DATA)
            self.state = 101
            self.data()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 102
                self.match(ObjectFileParser.NEWLINE)
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
            self.state = 108
            self.match(ObjectFileParser.REL)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 109
                self.entry_usage()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 115
                self.match(ObjectFileParser.NEWLINE)
                self.state = 120
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
            self.state = 121
            self.match(ObjectFileParser.XTRN)
            self.state = 122
            self.label()
            self.state = 123
            self.match(ObjectFileParser.COLON)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 124
                self.name()
                self.state = 125
                self.entry_usage()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
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
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 138
                self.byte()
                self.state = 143
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.number()
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
            self.state = 146
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
        self.enterRule(localctx, 24, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
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
        self.enterRule(localctx, 26, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
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
        self.enterRule(localctx, 28, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
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





