lexer grammar ObjectFileLexer;

TARG: 'TARG';
FILE: 'FILE' -> pushMode(IN_FILE);
ABS : 'ABS' -> pushMode(IN_ABS);
LOC: 'LOC';
NTRY: 'NTRY';
NAME: 'NAME';
ALIG: 'ALIG';
DATA: 'DATA' -> pushMode(IN_BYTES);
REL : 'REL';
XTRN: 'XTRN';

WORD: [a-zA-Z_0-9]+;
ABS_SECTION: '$abs';

COLON: ':';
MINUS: '-';
NEWLINE: ('\r'? '\n')+ ;
WS : (' ' | '\t')+ -> skip ;


mode IN_BYTES;
NEWLINE_BYTES: ('\r'? '\n')+ -> popMode;
BYTES: [a-zA-Z_0-9 \t]+;


mode IN_ABS;
WORD_ABS: [a-zA-Z_0-9]+;
WS_ABS : (' ' | '\t')+ -> skip ;
COLON_ABS: ':' -> popMode, pushMode(IN_BYTES);

mode IN_FILE;
SPACES_FILE: ' '+ -> popMode, pushMode(IN_FILEPATH);

mode IN_FILEPATH;
FILEPATH: ~[\r\n]+ -> popMode;