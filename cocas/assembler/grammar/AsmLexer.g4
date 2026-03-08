lexer grammar AsmLexer;

Asect : 'asect' ;
Break : 'break' ;
Continue : 'continue' ;
Do : 'do' ;
Else : 'else' ;
End : 'end' '.'? ;
Ext : 'ext' ;
File : 'file' ;
Fi : 'fi' ;
If : 'if' ;
Is : 'is' ;
Macro : 'macro' ;
Rsect : 'rsect' ;
Stays : 'stays' ;
Then : 'then' ;
Tplate : 'tplate' ;
Until : 'until' ;
Wend : 'wend' ;
While : 'while' ;

COMMA : ',' ;
PLUS : '+' ;
MINUS : '-' ;
COLON : ':' ;
ANGLE_BRACKET : '>' ;
COLON_ANGLE : ':>' ;
QUESTION_ANGLE : '?>' ;
QUESTION : '?' ;
OPEN_PAREN : '(' ;
CLOSE_PAREN : ')' ;
LINE_MARK_MARKER: '-|';

REGISTER : 'r'DECIMAL_NUMBER ;
WORD : [a-zA-Z_][a-zA-Z_0-9]* ;
WORD_WITH_DOTS : [a-zA-Z_.][a-zA-Z_.0-9]* ;
DECIMAL_NUMBER : [0-9]+  ;
BINARY_NUMBER : '0b'[01]+ ;
HEX_NUMBER : '0x'[0-9a-fA-F]+ ;
STRING : '"' (~[\\"]+ | '\\' .)* '"' ;
CHAR : '\'' (~[\\']+ | '\\' .)* '\'' ;

NEWLINE : '\r'? '\n' ;
COMMENT : '#'~[\n]* -> skip ;
WS : (' ' | '\t') -> skip ;


BASE64 : 'fp-' [a-zA-Z0-9/+=]+;


UNEXPECTED_TOKEN: [\u0000-\uFFFE];

