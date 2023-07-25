lexer grammar AsmLexer;

Asect : 'asect' ;
Break : 'break' ;
Continue : 'continue' ;
Do : 'do' ;
Else : 'else' ;
End : 'end' ;
Ext : 'ext' ;
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

DOT : '.' ;
COMMA : ',' ;
PLUS : '+' ;
MINUS : '-' ;
COLON : ':' ;
ASTERISK : '*' ;
ANGLE_BRACKET : '>' ;
OPEN_PAREN : '(' ;
CLOSE_PAREN : ')' ;
LINE_MARK_MARKER: '-|';

REGISTER : 'r'DECIMAL_NUMBER ;
WORD : [a-zA-Z_][a-zA-Z_0-9]* ;
DECIMAL_NUMBER : [0-9]+  ;
BINARY_NUMBER : '0b'[01]+ ;
HEX_NUMBER : '0x'[0-9a-fA-F]+ ;
STRING : '"'~["\\\n]*(('\\'.)~["\\\n]*)*'"' ;
CHAR : '\'' ('\\'. | ~[\\'\n]) '\'' ;

NEWLINE : '\r'? '\n' ;
COMMENT : '#'~[\n]* -> skip ;
WS : (' ' | '\t') -> skip ;


BASE64 : 'fp-' [a-zA-Z0-9/+=]+;


UNEXPECTED_TOKEN: [\u0000-\uFFFE];

