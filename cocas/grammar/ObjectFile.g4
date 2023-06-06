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
    (abs_block | ntry_record)+
;

abs_block:
    abs_record
    loc_record*
;

rsect_block:
    name_record
    alig_record?
    data_record
    loc_record*
    rel_record
    ntry_record*
;

targ_record: TARG label NEWLINE*;
abs_record: ABS number COLON data NEWLINE*;
loc_record: LOC path_base64 location* NEWLINE*;
ntry_record: NTRY label number NEWLINE*;
name_record: NAME section NEWLINE*;
alig_record: ALIG number NEWLINE*;
data_record: DATA data NEWLINE*;
rel_record: REL entry_usage* NEWLINE*;
xtrn_record: XTRN label COLON (section entry_usage)* NEWLINE*;

data: byte*;
entry_usage: minus? number (COLON range)?;
byte: number;
range: number COLON number;
location: number COLON number COLON number;

number: WORD;
label: WORD;
section: WORD | ABS_SECTION;
path_base64: FP_BASE64;
minus: MINUS;

TARG: 'TARG';
FILE: 'FILE';
ABS : 'ABS';
LOC: 'LOC';
NTRY: 'NTRY';
NAME: 'NAME';
ALIG: 'ALIG';
DATA: 'DATA';
REL : 'REL';
XTRN: 'XTRN';

WORD: [a-zA-Z_0-9]+;
FP_BASE64 : 'fp-' [a-zA-Z0-9/+=]+;
ABS_SECTION: '$abs';

COLON: ':';
MINUS: '-';
NEWLINE: '\r'? '\n' ;
WS : (' ' | '\t') -> skip ;
