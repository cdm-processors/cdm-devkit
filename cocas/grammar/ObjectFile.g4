grammar ObjectFile;

object_file:
    NEWLINE*
    targ_record?
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
    alig_record?
    data_record
    rel_record
    ntry_record*
;

targ_record: TARG name NEWLINE*;
abs_record: ABS number COLON data NEWLINE*;
ntry_record: NTRY label number NEWLINE*;
name_record: NAME name NEWLINE*;
alig_record: ALIG number NEWLINE*;
data_record: DATA data NEWLINE*;
rel_record: REL entry_usage* NEWLINE*;
xtrn_record: XTRN label COLON (name entry_usage)* NEWLINE*;

data: byte*;
entry_usage: minus? number (COLON range)?;
byte: number;
range: number COLON number;

number: WORD;
label: WORD;
name: WORD | ABS_SECTION;
minus: MINUS;

TARG: 'TARG';
ABS : 'ABS';
NTRY: 'NTRY';
NAME: 'NAME';
ALIG: 'ALIG';
DATA: 'DATA';
REL : 'REL';
XTRN: 'XTRN';

WORD: [a-zA-Z_0-9]+;
ABS_SECTION: '$abs';

COLON: ':';
MINUS: '-';
NEWLINE: '\r'? '\n' ;
WS : (' ' | '\t') -> skip ;
