grammar Macro;

mlb : NEWLINE* mlb_macro* EOF ;
mlb_macro : mlb_header macro_body ;
mlb_header : WS? ASTERISK WS? NAME WS? SLASH WS? DIGIT WS? NEWLINE ;

program : (macro | line)* EOF ;
macro : macro_header macro_body MACRO_FOOTER ;
macro_header : WS? Macro WS? NAME WS? SLASH WS? DIGIT WS? NEWLINE ;

macro_body : ((WS? NEWLINE) | line)*? ;
line: labels (instruction first_param)? (COMMA param)* NEWLINE;
labels : label* WS? ;
first_param : WS param | ;

label :       (macro_piece | macro_variable+ l_sep | l_sep)* macro_variable* LABEL_END ;
param :       (macro_piece | macro_variable+ p_sep | p_sep)* macro_variable* ;
instruction : (macro_piece | macro_variable+ OTHER | OTHER)+ macro_variable* | macro_variable+ ;
l_sep : OTHER | WS | COMMA ;
p_sep : OTHER | WS ;

macro_piece : macro_text | macro_param | macro_nonce ;
macro_variable : QUESTION_MARK macro_piece+ ;
macro_text : Macro | NAME | DIGIT | STRING | CHAR ;
macro_param : DOLLAR_SIGN DIGIT ;
macro_nonce : APOSTROPHE ;

Macro : 'macro' ;
MACRO_FOOTER : [\t ]* 'mend' [\t ]* '\r'? '\n' ;

WS : [\t ]+ ;
NEWLINE : '\r'? '\n' ;
COMMENT : '#'~[\n]* -> skip ;

ASTERISK : '*' ;
COMMA : ',' ;
LABEL_END : [:>] ;
QUESTION_MARK : '?' ;
STRING: '"' (~[\\"\n]+ | '\\' .)* '"' ;
CHAR : '\'' (~[\\'\n]+ | '\\' .)* '\'' ;

NAME : [_a-zA-Z][_a-zA-Z0-9.]* ;
DIGIT : [0-9] ;
SLASH : '/' ;

APOSTROPHE : '\'' ;
DOLLAR_SIGN : '$' ;

OTHER : [-+()]+ ;
