grammar ObjectFile;

object_file:
    NEWLINE*
    ( asect_block
      rsect_block*
    | rsect_block+
    )
    xtrn_record*
    EOF
;

asect_block:
    (abs_record | ntry_record)+
;

rsect_block:
    name_record
    data_record
    rel_record
    ntry_record*
;

abs_record: ABS number COLON data NEWLINE*;
ntry_record: NTRY label number NEWLINE*;
name_record: NAME name NEWLINE*;
data_record: DATA data NEWLINE*;
rel_record: REL entry_usage* NEWLINE*;
xtrn_record: XTRN label COLON (name entry_usage)* NEWLINE*;

data: byte*;
entry_usage: number;
byte: number;

number: WORD;
label: WORD;
name: WORD | ABS_SECTION;

ABS : 'ABS';
NTRY: 'NTRY';
NAME: 'NAME';
DATA: 'DATA';
REL : 'REL';
XTRN: 'XTRN';

WORD: [a-zA-Z_0-9]+;
ABS_SECTION: '$abs';

COLON: ':';
NEWLINE: '\r'? '\n' ;
WS : (' ' | '\t') -> skip ;
