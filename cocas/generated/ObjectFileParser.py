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
        4,1,12,148,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,4,0,39,8,0,11,
        0,12,0,40,3,0,43,8,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,1,1,1,5,1,
        53,8,1,10,1,12,1,56,9,1,1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,
        9,2,1,3,1,3,1,3,1,3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,4,1,4,1,4,
        1,4,5,4,81,8,4,10,4,12,4,84,9,4,1,5,1,5,1,5,5,5,89,8,5,10,5,12,5,
        92,9,5,1,6,1,6,1,6,5,6,97,8,6,10,6,12,6,100,9,6,1,7,1,7,5,7,104,
        8,7,10,7,12,7,107,9,7,1,7,5,7,110,8,7,10,7,12,7,113,9,7,1,8,1,8,
        1,8,1,8,1,8,1,8,5,8,121,8,8,10,8,12,8,124,9,8,1,8,5,8,127,8,8,10,
        8,12,8,130,9,8,1,9,5,9,133,8,9,10,9,12,9,136,9,9,1,10,1,10,1,11,
        1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,0,1,1,0,7,8,148,0,42,1,0,0,0,2,54,1,0,0,0,4,
        57,1,0,0,0,6,66,1,0,0,0,8,76,1,0,0,0,10,85,1,0,0,0,12,93,1,0,0,0,
        14,101,1,0,0,0,16,114,1,0,0,0,18,134,1,0,0,0,20,137,1,0,0,0,22,139,
        1,0,0,0,24,141,1,0,0,0,26,143,1,0,0,0,28,145,1,0,0,0,30,34,3,2,1,
        0,31,33,3,4,2,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,
        1,0,0,0,35,43,1,0,0,0,36,34,1,0,0,0,37,39,3,4,2,0,38,37,1,0,0,0,
        39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,30,1,
        0,0,0,42,38,1,0,0,0,43,47,1,0,0,0,44,46,3,16,8,0,45,44,1,0,0,0,46,
        49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,0,49,47,1,0,0,
        0,50,53,3,6,3,0,51,53,3,8,4,0,52,50,1,0,0,0,52,51,1,0,0,0,53,56,
        1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,3,1,0,0,0,56,54,1,0,0,0,57,
        58,3,10,5,0,58,59,3,12,6,0,59,63,3,14,7,0,60,62,3,8,4,0,61,60,1,
        0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,5,1,0,0,0,65,
        63,1,0,0,0,66,67,5,1,0,0,67,68,3,22,11,0,68,69,5,10,0,0,69,73,3,
        18,9,0,70,72,5,11,0,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,
        73,74,1,0,0,0,74,7,1,0,0,0,75,73,1,0,0,0,76,77,5,2,0,0,77,78,3,26,
        13,0,78,82,3,22,11,0,79,81,5,11,0,0,80,79,1,0,0,0,81,84,1,0,0,0,
        82,80,1,0,0,0,82,83,1,0,0,0,83,9,1,0,0,0,84,82,1,0,0,0,85,86,5,3,
        0,0,86,90,3,28,14,0,87,89,5,11,0,0,88,87,1,0,0,0,89,92,1,0,0,0,90,
        88,1,0,0,0,90,91,1,0,0,0,91,11,1,0,0,0,92,90,1,0,0,0,93,94,5,4,0,
        0,94,98,3,18,9,0,95,97,5,11,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,
        96,1,0,0,0,98,99,1,0,0,0,99,13,1,0,0,0,100,98,1,0,0,0,101,105,5,
        5,0,0,102,104,3,20,10,0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,
        1,0,0,0,105,106,1,0,0,0,106,111,1,0,0,0,107,105,1,0,0,0,108,110,
        5,11,0,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,
        1,0,0,0,112,15,1,0,0,0,113,111,1,0,0,0,114,115,5,6,0,0,115,116,3,
        26,13,0,116,122,5,10,0,0,117,118,3,28,14,0,118,119,3,20,10,0,119,
        121,1,0,0,0,120,117,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,128,1,0,0,0,124,122,1,0,0,0,125,127,5,11,0,0,126,
        125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,
        17,1,0,0,0,130,128,1,0,0,0,131,133,3,24,12,0,132,131,1,0,0,0,133,
        136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,19,1,0,0,0,136,134,
        1,0,0,0,137,138,3,22,11,0,138,21,1,0,0,0,139,140,5,9,0,0,140,23,
        1,0,0,0,141,142,5,9,0,0,142,25,1,0,0,0,143,144,5,7,0,0,144,27,1,
        0,0,0,145,146,7,0,0,0,146,29,1,0,0,0,16,34,40,42,47,52,54,63,73,
        82,90,98,105,111,122,128,134
    ]

class ObjectFileParser ( Parser ):

    grammarFileName = "ObjectFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ABS'", "'NTRY'", "'NAME'", "'DATA'", 
                     "'REL'", "'XTRN'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "ABS", "NTRY", "NAME", "DATA", "REL", 
                      "XTRN", "WORD", "ABS_SECTION", "HEX_NUMBER", "COLON", 
                      "NEWLINE", "WS" ]

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
    RULE_address = 11
    RULE_byte = 12
    RULE_label = 13
    RULE_name = 14

    ruleNames =  [ "object_file", "asect_block", "rsect_block", "abs_record", 
                   "ntry_record", "name_record", "data_record", "rel_record", 
                   "xtrn_record", "data", "entry_usage", "address", "byte", 
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
    HEX_NUMBER=9
    COLON=10
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

        def asect_block(self):
            return self.getTypedRuleContext(ObjectFileParser.Asect_blockContext,0)


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
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 30
                self.asect_block()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 31
                    self.rsect_block()
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 37
                    self.rsect_block()
                    self.state = 40 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                pass


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 44
                self.xtrn_record()
                self.state = 49
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
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 52
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 50
                    self.abs_record()
                    pass
                elif token in [2]:
                    self.state = 51
                    self.ntry_record()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56
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
            self.state = 57
            self.name_record()
            self.state = 58
            self.data_record()
            self.state = 59
            self.rel_record()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 60
                self.ntry_record()
                self.state = 65
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

        def address(self):
            return self.getTypedRuleContext(ObjectFileParser.AddressContext,0)


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
            self.state = 66
            self.match(ObjectFileParser.ABS)
            self.state = 67
            self.address()
            self.state = 68
            self.match(ObjectFileParser.COLON)
            self.state = 69
            self.data()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 70
                self.match(ObjectFileParser.NEWLINE)
                self.state = 75
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


        def address(self):
            return self.getTypedRuleContext(ObjectFileParser.AddressContext,0)


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
            self.state = 76
            self.match(ObjectFileParser.NTRY)
            self.state = 77
            self.label()
            self.state = 78
            self.address()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 79
                self.match(ObjectFileParser.NEWLINE)
                self.state = 84
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
            self.state = 85
            self.match(ObjectFileParser.NAME)
            self.state = 86
            self.name()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 87
                self.match(ObjectFileParser.NEWLINE)
                self.state = 92
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
            self.state = 93
            self.match(ObjectFileParser.DATA)
            self.state = 94
            self.data()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 95
                self.match(ObjectFileParser.NEWLINE)
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
            self.state = 101
            self.match(ObjectFileParser.REL)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 102
                self.entry_usage()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
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
            self.state = 114
            self.match(ObjectFileParser.XTRN)
            self.state = 115
            self.label()
            self.state = 116
            self.match(ObjectFileParser.COLON)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 117
                self.name()
                self.state = 118
                self.entry_usage()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 125
                self.match(ObjectFileParser.NEWLINE)
                self.state = 130
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
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 131
                self.byte()
                self.state = 136
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

        def address(self):
            return self.getTypedRuleContext(ObjectFileParser.AddressContext,0)


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
            self.state = 137
            self.address()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEX_NUMBER(self):
            return self.getToken(ObjectFileParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_address

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddress" ):
                return visitor.visitAddress(self)
            else:
                return visitor.visitChildren(self)




    def address(self):

        localctx = ObjectFileParser.AddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ObjectFileParser.HEX_NUMBER)
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

        def HEX_NUMBER(self):
            return self.getToken(ObjectFileParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return ObjectFileParser.RULE_byte

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByte" ):
                return visitor.visitByte(self)
            else:
                return visitor.visitChildren(self)




    def byte(self):

        localctx = ObjectFileParser.ByteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_byte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ObjectFileParser.HEX_NUMBER)
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
            self.state = 143
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
            self.state = 145
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





