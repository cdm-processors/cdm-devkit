parser grammar ObjectFileParser;

options { tokenVocab = ObjectFileLexer; }

object_file:
    NEWLINE?
    targ_record?
    object_block+
    EOF
;

object_block:
    source_record?
    ( asect_block
      rsect_block*
    | rsect_block+
    )
    xtrn_record*
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
    rel_record?
    ntry_record*
;

targ_record: TARG label NEWLINE;
source_record: FILE SPACES_FILE filepath NEWLINE;
abs_record: ABS abs_address COLON_ABS data? NEWLINE_BYTES+;
loc_record: LOC location* NEWLINE;
ntry_record: NTRY label number NEWLINE;
name_record: NAME section NEWLINE;
alig_record: ALIG number NEWLINE;
data_record: DATA data? NEWLINE_BYTES+;
rel_record: REL entry_usage* NEWLINE;
xtrn_record: XTRN label COLON (section entry_usage)* NEWLINE;

data: BYTES;
filepath: FILEPATH;
entry_usage: minus? number (COLON range)?;
range: number COLON number;
location: number COLON number COLON number;

abs_address: WORD_ABS;
number: WORD;
label: WORD;
section: WORD | ABS_SECTION;
minus: MINUS;
