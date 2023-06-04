grammar ObjectFile;

object_file:
    ( asect_block
      rsect_block*
    | rsect_block+
    )
    xtrn_record*
;

asect_block:
    (abs_record | ntry_record)*
;

rsect_block:
    name_record
    data_record
    rel_record
    ntry_record*
;

abs_record: ABS address COLON data NEWLINE*;
ntry_record: NTRY label address NEWLINE*;
name_record: NAME name NEWLINE*;
data_record: DATA data NEWLINE*;
rel_record: REL entry_usage* NEWLINE*;
xtrn_record: XTRN label COLON (name entry_usage)* NEWLINE*;

data: byte*;
entry_usage: address;

address: HEX_NUMBER;
byte: HEX_NUMBER;
label: WORD;
name: WORD | ABS_SECTION;

ABS : 'ABS';
NTRY: 'NTRY';
NAME: 'NAME';
DATA: 'DATA';
REL : 'REL';
XTRN: 'XTRN';

WORD: [a-zA-Z_][a-zA-Z_0-9]*;
ABS_SECTION: '$'[a-zA-Z_][a-zA-Z_0-9]*;
HEX_NUMBER: [0-9a-fA-F]+;

COLON: ':';
NEWLINE: '\r'? '\n' ;
WS : (' ' | '\t') -> skip ;
