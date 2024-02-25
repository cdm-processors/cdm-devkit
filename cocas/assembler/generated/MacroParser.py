# Generated from assembler/grammar/Macro.g4 by ANTLR 4.13.1
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
        4,1,17,238,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,
        1,0,1,1,1,1,1,1,1,2,3,2,59,8,2,1,2,1,2,3,2,63,8,2,1,2,1,2,3,2,67,
        8,2,1,2,1,2,3,2,71,8,2,1,2,1,2,3,2,75,8,2,1,2,1,2,1,3,1,3,5,3,81,
        8,3,10,3,12,3,84,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,3,5,93,8,5,1,5,
        1,5,3,5,97,8,5,1,5,1,5,3,5,101,8,5,1,5,1,5,3,5,105,8,5,1,5,1,5,3,
        5,109,8,5,1,5,1,5,1,6,5,6,114,8,6,10,6,12,6,117,9,6,1,7,1,7,1,7,
        1,7,3,7,123,8,7,1,7,1,7,5,7,127,8,7,10,7,12,7,130,9,7,1,7,1,7,1,
        8,5,8,135,8,8,10,8,12,8,138,9,8,1,8,3,8,141,8,8,1,9,1,9,1,9,3,9,
        146,8,9,1,10,1,10,4,10,150,8,10,11,10,12,10,151,1,10,1,10,1,10,5,
        10,157,8,10,10,10,12,10,160,9,10,1,10,5,10,163,8,10,10,10,12,10,
        166,9,10,1,10,1,10,1,11,1,11,4,11,172,8,11,11,11,12,11,173,1,11,
        1,11,1,11,5,11,179,8,11,10,11,12,11,182,9,11,1,11,5,11,185,8,11,
        10,11,12,11,188,9,11,1,12,1,12,4,12,192,8,12,11,12,12,12,193,1,12,
        1,12,1,12,4,12,199,8,12,11,12,12,12,200,1,12,5,12,204,8,12,10,12,
        12,12,207,9,12,1,12,4,12,210,8,12,11,12,12,12,211,3,12,214,8,12,
        1,13,1,13,1,14,1,14,1,15,1,15,1,15,3,15,223,8,15,1,16,1,16,4,16,
        227,8,16,11,16,12,16,228,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,
        1,115,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        0,3,3,0,3,3,7,7,17,17,2,0,3,3,17,17,2,0,1,1,10,13,257,0,43,1,0,0,
        0,2,54,1,0,0,0,4,58,1,0,0,0,6,82,1,0,0,0,8,87,1,0,0,0,10,92,1,0,
        0,0,12,115,1,0,0,0,14,118,1,0,0,0,16,136,1,0,0,0,18,145,1,0,0,0,
        20,158,1,0,0,0,22,180,1,0,0,0,24,213,1,0,0,0,26,215,1,0,0,0,28,217,
        1,0,0,0,30,222,1,0,0,0,32,224,1,0,0,0,34,230,1,0,0,0,36,232,1,0,
        0,0,38,235,1,0,0,0,40,42,5,4,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,
        41,1,0,0,0,43,44,1,0,0,0,44,49,1,0,0,0,45,43,1,0,0,0,46,48,3,2,1,
        0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,
        1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,55,3,4,2,0,55,
        56,3,12,6,0,56,3,1,0,0,0,57,59,5,3,0,0,58,57,1,0,0,0,58,59,1,0,0,
        0,59,60,1,0,0,0,60,62,5,6,0,0,61,63,5,3,0,0,62,61,1,0,0,0,62,63,
        1,0,0,0,63,64,1,0,0,0,64,66,5,12,0,0,65,67,5,3,0,0,66,65,1,0,0,0,
        66,67,1,0,0,0,67,68,1,0,0,0,68,70,5,14,0,0,69,71,5,3,0,0,70,69,1,
        0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,74,5,13,0,0,73,75,5,3,0,0,74,
        73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,4,0,0,77,5,1,0,0,
        0,78,81,3,8,4,0,79,81,3,14,7,0,80,78,1,0,0,0,80,79,1,0,0,0,81,84,
        1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,
        85,86,5,0,0,1,86,7,1,0,0,0,87,88,3,10,5,0,88,89,3,12,6,0,89,90,5,
        2,0,0,90,9,1,0,0,0,91,93,5,3,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,
        94,1,0,0,0,94,96,5,1,0,0,95,97,5,3,0,0,96,95,1,0,0,0,96,97,1,0,0,
        0,97,98,1,0,0,0,98,100,5,12,0,0,99,101,5,3,0,0,100,99,1,0,0,0,100,
        101,1,0,0,0,101,102,1,0,0,0,102,104,5,14,0,0,103,105,5,3,0,0,104,
        103,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,108,5,13,0,0,107,
        109,5,3,0,0,108,107,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,
        111,5,4,0,0,111,11,1,0,0,0,112,114,3,14,7,0,113,112,1,0,0,0,114,
        117,1,0,0,0,115,116,1,0,0,0,115,113,1,0,0,0,116,13,1,0,0,0,117,115,
        1,0,0,0,118,122,3,16,8,0,119,120,3,24,12,0,120,121,3,18,9,0,121,
        123,1,0,0,0,122,119,1,0,0,0,122,123,1,0,0,0,123,128,1,0,0,0,124,
        125,5,7,0,0,125,127,3,22,11,0,126,124,1,0,0,0,127,130,1,0,0,0,128,
        126,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,
        132,5,4,0,0,132,15,1,0,0,0,133,135,3,20,10,0,134,133,1,0,0,0,135,
        138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,140,1,0,0,0,138,
        136,1,0,0,0,139,141,5,3,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,
        17,1,0,0,0,142,143,5,3,0,0,143,146,3,22,11,0,144,146,1,0,0,0,145,
        142,1,0,0,0,145,144,1,0,0,0,146,19,1,0,0,0,147,157,3,30,15,0,148,
        150,3,32,16,0,149,148,1,0,0,0,150,151,1,0,0,0,151,149,1,0,0,0,151,
        152,1,0,0,0,152,153,1,0,0,0,153,154,3,26,13,0,154,157,1,0,0,0,155,
        157,3,26,13,0,156,147,1,0,0,0,156,149,1,0,0,0,156,155,1,0,0,0,157,
        160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,164,1,0,0,0,160,
        158,1,0,0,0,161,163,3,32,16,0,162,161,1,0,0,0,163,166,1,0,0,0,164,
        162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,
        168,5,8,0,0,168,21,1,0,0,0,169,179,3,30,15,0,170,172,3,32,16,0,171,
        170,1,0,0,0,172,173,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,
        175,1,0,0,0,175,176,3,28,14,0,176,179,1,0,0,0,177,179,3,28,14,0,
        178,169,1,0,0,0,178,171,1,0,0,0,178,177,1,0,0,0,179,182,1,0,0,0,
        180,178,1,0,0,0,180,181,1,0,0,0,181,186,1,0,0,0,182,180,1,0,0,0,
        183,185,3,32,16,0,184,183,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,
        0,186,187,1,0,0,0,187,23,1,0,0,0,188,186,1,0,0,0,189,199,3,30,15,
        0,190,192,3,32,16,0,191,190,1,0,0,0,192,193,1,0,0,0,193,191,1,0,
        0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,196,5,17,0,0,196,199,1,0,
        0,0,197,199,5,17,0,0,198,189,1,0,0,0,198,191,1,0,0,0,198,197,1,0,
        0,0,199,200,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,205,1,0,
        0,0,202,204,3,32,16,0,203,202,1,0,0,0,204,207,1,0,0,0,205,203,1,
        0,0,0,205,206,1,0,0,0,206,214,1,0,0,0,207,205,1,0,0,0,208,210,3,
        32,16,0,209,208,1,0,0,0,210,211,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,214,1,0,0,0,213,198,1,0,0,0,213,209,1,0,0,0,214,25,1,
        0,0,0,215,216,7,0,0,0,216,27,1,0,0,0,217,218,7,1,0,0,218,29,1,0,
        0,0,219,223,3,34,17,0,220,223,3,36,18,0,221,223,3,38,19,0,222,219,
        1,0,0,0,222,220,1,0,0,0,222,221,1,0,0,0,223,31,1,0,0,0,224,226,5,
        9,0,0,225,227,3,30,15,0,226,225,1,0,0,0,227,228,1,0,0,0,228,226,
        1,0,0,0,228,229,1,0,0,0,229,33,1,0,0,0,230,231,7,2,0,0,231,35,1,
        0,0,0,232,233,5,16,0,0,233,234,5,13,0,0,234,37,1,0,0,0,235,236,5,
        15,0,0,236,39,1,0,0,0,36,43,49,58,62,66,70,74,80,82,92,96,100,104,
        108,115,122,128,136,140,145,151,156,158,164,173,178,180,186,193,
        198,200,205,211,213,222,228
    ]

class MacroParser ( Parser ):

    grammarFileName = "Macro.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'macro'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "','", "<INVALID>", "'?'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'/'", "'''", 
                     "'$'" ]

    symbolicNames = [ "<INVALID>", "Macro", "MACRO_FOOTER", "WS", "NEWLINE", 
                      "COMMENT", "ASTERISK", "COMMA", "LABEL_END", "QUESTION_MARK", 
                      "STRING", "CHAR", "NAME", "DIGIT", "SLASH", "APOSTROPHE", 
                      "DOLLAR_SIGN", "OTHER" ]

    RULE_mlb = 0
    RULE_mlb_macro = 1
    RULE_mlb_header = 2
    RULE_program = 3
    RULE_macro = 4
    RULE_macro_header = 5
    RULE_macro_body = 6
    RULE_line = 7
    RULE_labels = 8
    RULE_first_param = 9
    RULE_label = 10
    RULE_param = 11
    RULE_instruction = 12
    RULE_l_sep = 13
    RULE_p_sep = 14
    RULE_macro_piece = 15
    RULE_macro_variable = 16
    RULE_macro_text = 17
    RULE_macro_param = 18
    RULE_macro_nonce = 19

    ruleNames =  [ "mlb", "mlb_macro", "mlb_header", "program", "macro", 
                   "macro_header", "macro_body", "line", "labels", "first_param", 
                   "label", "param", "instruction", "l_sep", "p_sep", "macro_piece", 
                   "macro_variable", "macro_text", "macro_param", "macro_nonce" ]

    EOF = Token.EOF
    Macro=1
    MACRO_FOOTER=2
    WS=3
    NEWLINE=4
    COMMENT=5
    ASTERISK=6
    COMMA=7
    LABEL_END=8
    QUESTION_MARK=9
    STRING=10
    CHAR=11
    NAME=12
    DIGIT=13
    SLASH=14
    APOSTROPHE=15
    DOLLAR_SIGN=16
    OTHER=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MlbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MacroParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.NEWLINE)
            else:
                return self.getToken(MacroParser.NEWLINE, i)

        def mlb_macro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Mlb_macroContext)
            else:
                return self.getTypedRuleContext(MacroParser.Mlb_macroContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_mlb

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMlb" ):
                return visitor.visitMlb(self)
            else:
                return visitor.visitChildren(self)




    def mlb(self):

        localctx = MacroParser.MlbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_mlb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 40
                self.match(MacroParser.NEWLINE)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==6:
                self.state = 46
                self.mlb_macro()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(MacroParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mlb_macroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mlb_header(self):
            return self.getTypedRuleContext(MacroParser.Mlb_headerContext,0)


        def macro_body(self):
            return self.getTypedRuleContext(MacroParser.Macro_bodyContext,0)


        def getRuleIndex(self):
            return MacroParser.RULE_mlb_macro

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMlb_macro" ):
                return visitor.visitMlb_macro(self)
            else:
                return visitor.visitChildren(self)




    def mlb_macro(self):

        localctx = MacroParser.Mlb_macroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mlb_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.mlb_header()
            self.state = 55
            self.macro_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mlb_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASTERISK(self):
            return self.getToken(MacroParser.ASTERISK, 0)

        def NAME(self):
            return self.getToken(MacroParser.NAME, 0)

        def SLASH(self):
            return self.getToken(MacroParser.SLASH, 0)

        def DIGIT(self):
            return self.getToken(MacroParser.DIGIT, 0)

        def NEWLINE(self):
            return self.getToken(MacroParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.WS)
            else:
                return self.getToken(MacroParser.WS, i)

        def getRuleIndex(self):
            return MacroParser.RULE_mlb_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMlb_header" ):
                return visitor.visitMlb_header(self)
            else:
                return visitor.visitChildren(self)




    def mlb_header(self):

        localctx = MacroParser.Mlb_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mlb_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 57
                self.match(MacroParser.WS)


            self.state = 60
            self.match(MacroParser.ASTERISK)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 61
                self.match(MacroParser.WS)


            self.state = 64
            self.match(MacroParser.NAME)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 65
                self.match(MacroParser.WS)


            self.state = 68
            self.match(MacroParser.SLASH)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 69
                self.match(MacroParser.WS)


            self.state = 72
            self.match(MacroParser.DIGIT)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 73
                self.match(MacroParser.WS)


            self.state = 76
            self.match(MacroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MacroParser.EOF, 0)

        def macro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.MacroContext)
            else:
                return self.getTypedRuleContext(MacroParser.MacroContext,i)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.LineContext)
            else:
                return self.getTypedRuleContext(MacroParser.LineContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MacroParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 245658) != 0):
                self.state = 80
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 78
                    self.macro()
                    pass

                elif la_ == 2:
                    self.state = 79
                    self.line()
                    pass


                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(MacroParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def macro_header(self):
            return self.getTypedRuleContext(MacroParser.Macro_headerContext,0)


        def macro_body(self):
            return self.getTypedRuleContext(MacroParser.Macro_bodyContext,0)


        def MACRO_FOOTER(self):
            return self.getToken(MacroParser.MACRO_FOOTER, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_macro

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro" ):
                return visitor.visitMacro(self)
            else:
                return visitor.visitChildren(self)




    def macro(self):

        localctx = MacroParser.MacroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.macro_header()
            self.state = 88
            self.macro_body()
            self.state = 89
            self.match(MacroParser.MACRO_FOOTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Macro(self):
            return self.getToken(MacroParser.Macro, 0)

        def NAME(self):
            return self.getToken(MacroParser.NAME, 0)

        def SLASH(self):
            return self.getToken(MacroParser.SLASH, 0)

        def DIGIT(self):
            return self.getToken(MacroParser.DIGIT, 0)

        def NEWLINE(self):
            return self.getToken(MacroParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.WS)
            else:
                return self.getToken(MacroParser.WS, i)

        def getRuleIndex(self):
            return MacroParser.RULE_macro_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_header" ):
                return visitor.visitMacro_header(self)
            else:
                return visitor.visitChildren(self)




    def macro_header(self):

        localctx = MacroParser.Macro_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_macro_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 91
                self.match(MacroParser.WS)


            self.state = 94
            self.match(MacroParser.Macro)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 95
                self.match(MacroParser.WS)


            self.state = 98
            self.match(MacroParser.NAME)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 99
                self.match(MacroParser.WS)


            self.state = 102
            self.match(MacroParser.SLASH)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 103
                self.match(MacroParser.WS)


            self.state = 106
            self.match(MacroParser.DIGIT)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 107
                self.match(MacroParser.WS)


            self.state = 110
            self.match(MacroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.LineContext)
            else:
                return self.getTypedRuleContext(MacroParser.LineContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_macro_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_body" ):
                return visitor.visitMacro_body(self)
            else:
                return visitor.visitChildren(self)




    def macro_body(self):

        localctx = MacroParser.Macro_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_macro_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 112
                    self.line() 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labels(self):
            return self.getTypedRuleContext(MacroParser.LabelsContext,0)


        def NEWLINE(self):
            return self.getToken(MacroParser.NEWLINE, 0)

        def instruction(self):
            return self.getTypedRuleContext(MacroParser.InstructionContext,0)


        def first_param(self):
            return self.getTypedRuleContext(MacroParser.First_paramContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.COMMA)
            else:
                return self.getToken(MacroParser.COMMA, i)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.ParamContext)
            else:
                return self.getTypedRuleContext(MacroParser.ParamContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = MacroParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.labels()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245250) != 0):
                self.state = 119
                self.instruction()
                self.state = 120
                self.first_param()


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 124
                self.match(MacroParser.COMMA)
                self.state = 125
                self.param()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(MacroParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.LabelContext)
            else:
                return self.getTypedRuleContext(MacroParser.LabelContext,i)


        def WS(self):
            return self.getToken(MacroParser.WS, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_labels

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabels" ):
                return visitor.visitLabels(self)
            else:
                return visitor.visitChildren(self)




    def labels(self):

        localctx = MacroParser.LabelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_labels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 133
                    self.label() 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 139
                self.match(MacroParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class First_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(MacroParser.WS, 0)

        def param(self):
            return self.getTypedRuleContext(MacroParser.ParamContext,0)


        def getRuleIndex(self):
            return MacroParser.RULE_first_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFirst_param" ):
                return visitor.visitFirst_param(self)
            else:
                return visitor.visitChildren(self)




    def first_param(self):

        localctx = MacroParser.First_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_first_param)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(MacroParser.WS)
                self.state = 143
                self.param()
                pass
            elif token in [4, 7]:
                self.enterOuterAlt(localctx, 2)

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


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL_END(self):
            return self.getToken(MacroParser.LABEL_END, 0)

        def macro_piece(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Macro_pieceContext)
            else:
                return self.getTypedRuleContext(MacroParser.Macro_pieceContext,i)


        def l_sep(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.L_sepContext)
            else:
                return self.getTypedRuleContext(MacroParser.L_sepContext,i)


        def macro_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Macro_variableContext)
            else:
                return self.getTypedRuleContext(MacroParser.Macro_variableContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = MacroParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 10, 11, 12, 13, 15, 16]:
                        self.state = 147
                        self.macro_piece()
                        pass
                    elif token in [9]:
                        self.state = 149 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 148
                            self.macro_variable()
                            self.state = 151 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==9):
                                break

                        self.state = 153
                        self.l_sep()
                        pass
                    elif token in [3, 7, 17]:
                        self.state = 155
                        self.l_sep()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 161
                self.macro_variable()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(MacroParser.LABEL_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def macro_piece(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Macro_pieceContext)
            else:
                return self.getTypedRuleContext(MacroParser.Macro_pieceContext,i)


        def p_sep(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.P_sepContext)
            else:
                return self.getTypedRuleContext(MacroParser.P_sepContext,i)


        def macro_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Macro_variableContext)
            else:
                return self.getTypedRuleContext(MacroParser.Macro_variableContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MacroParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 178
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 10, 11, 12, 13, 15, 16]:
                        self.state = 169
                        self.macro_piece()
                        pass
                    elif token in [9]:
                        self.state = 171 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 170
                            self.macro_variable()
                            self.state = 173 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==9):
                                break

                        self.state = 175
                        self.p_sep()
                        pass
                    elif token in [3, 17]:
                        self.state = 177
                        self.p_sep()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 183
                self.macro_variable()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def macro_piece(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Macro_pieceContext)
            else:
                return self.getTypedRuleContext(MacroParser.Macro_pieceContext,i)


        def OTHER(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.OTHER)
            else:
                return self.getToken(MacroParser.OTHER, i)

        def macro_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Macro_variableContext)
            else:
                return self.getTypedRuleContext(MacroParser.Macro_variableContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = MacroParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 198
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [1, 10, 11, 12, 13, 15, 16]:
                            self.state = 189
                            self.macro_piece()
                            pass
                        elif token in [9]:
                            self.state = 191 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while True:
                                self.state = 190
                                self.macro_variable()
                                self.state = 193 
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)
                                if not (_la==9):
                                    break

                            self.state = 195
                            self.match(MacroParser.OTHER)
                            pass
                        elif token in [17]:
                            self.state = 197
                            self.match(MacroParser.OTHER)
                            pass
                        else:
                            raise NoViableAltException(self)


                    else:
                        raise NoViableAltException(self)
                    self.state = 200 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 202
                    self.macro_variable()
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 208
                    self.macro_variable()
                    self.state = 211 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class L_sepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OTHER(self):
            return self.getToken(MacroParser.OTHER, 0)

        def WS(self):
            return self.getToken(MacroParser.WS, 0)

        def COMMA(self):
            return self.getToken(MacroParser.COMMA, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_l_sep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_sep" ):
                return visitor.visitL_sep(self)
            else:
                return visitor.visitChildren(self)




    def l_sep(self):

        localctx = MacroParser.L_sepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_l_sep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 131208) != 0)):
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


    class P_sepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OTHER(self):
            return self.getToken(MacroParser.OTHER, 0)

        def WS(self):
            return self.getToken(MacroParser.WS, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_p_sep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_sep" ):
                return visitor.visitP_sep(self)
            else:
                return visitor.visitChildren(self)




    def p_sep(self):

        localctx = MacroParser.P_sepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_p_sep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==3 or _la==17):
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


    class Macro_pieceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def macro_text(self):
            return self.getTypedRuleContext(MacroParser.Macro_textContext,0)


        def macro_param(self):
            return self.getTypedRuleContext(MacroParser.Macro_paramContext,0)


        def macro_nonce(self):
            return self.getTypedRuleContext(MacroParser.Macro_nonceContext,0)


        def getRuleIndex(self):
            return MacroParser.RULE_macro_piece

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_piece" ):
                return visitor.visitMacro_piece(self)
            else:
                return visitor.visitChildren(self)




    def macro_piece(self):

        localctx = MacroParser.Macro_pieceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_macro_piece)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.macro_text()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.macro_param()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.macro_nonce()
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


    class Macro_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION_MARK(self):
            return self.getToken(MacroParser.QUESTION_MARK, 0)

        def macro_piece(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.Macro_pieceContext)
            else:
                return self.getTypedRuleContext(MacroParser.Macro_pieceContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_macro_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_variable" ):
                return visitor.visitMacro_variable(self)
            else:
                return visitor.visitChildren(self)




    def macro_variable(self):

        localctx = MacroParser.Macro_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_macro_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MacroParser.QUESTION_MARK)
            self.state = 226 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 225
                self.macro_piece()
                self.state = 228 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 113666) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Macro(self):
            return self.getToken(MacroParser.Macro, 0)

        def NAME(self):
            return self.getToken(MacroParser.NAME, 0)

        def DIGIT(self):
            return self.getToken(MacroParser.DIGIT, 0)

        def STRING(self):
            return self.getToken(MacroParser.STRING, 0)

        def CHAR(self):
            return self.getToken(MacroParser.CHAR, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_macro_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_text" ):
                return visitor.visitMacro_text(self)
            else:
                return visitor.visitChildren(self)




    def macro_text(self):

        localctx = MacroParser.Macro_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_macro_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15362) != 0)):
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


    class Macro_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_SIGN(self):
            return self.getToken(MacroParser.DOLLAR_SIGN, 0)

        def DIGIT(self):
            return self.getToken(MacroParser.DIGIT, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_macro_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_param" ):
                return visitor.visitMacro_param(self)
            else:
                return visitor.visitChildren(self)




    def macro_param(self):

        localctx = MacroParser.Macro_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_macro_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MacroParser.DOLLAR_SIGN)
            self.state = 233
            self.match(MacroParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_nonceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APOSTROPHE(self):
            return self.getToken(MacroParser.APOSTROPHE, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_macro_nonce

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_nonce" ):
                return visitor.visitMacro_nonce(self)
            else:
                return visitor.visitChildren(self)




    def macro_nonce(self):

        localctx = MacroParser.Macro_nonceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_macro_nonce)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(MacroParser.APOSTROPHE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





