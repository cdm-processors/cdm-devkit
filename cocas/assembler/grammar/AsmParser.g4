parser grammar AsmParser;

options { tokenVocab=AsmLexer; }

@header {
from base64 import b64decode
}

@members {
    self.current_file = ''
    self.current_line = 0
    self.current_offset = 0
}

program_nomacros : NEWLINE* top_line* section* End ;

program : NEWLINE* line_mark+ top_line* section* End ;

section
    :  asect_header section_body # absoluteSection
    |  rsect_header section_body # relocatableSection
    | tplate_header section_body # templateSection
    ;

asect_header  :  Asect number NEWLINE+ ;
rsect_header  :  Rsect name   NEWLINE+ ;
tplate_header : Tplate name   NEWLINE+ ;

section_body : code_block ;
code_block
    :
    ( break_statement
    | continue_statement
    | line
    | conditional
    | while_loop
    | until_loop
    | line_mark
    )*
    ;

line_mark locals [
source_file = '',
source_line = 0
] : LINE_MARK_MARKER  line_number filepath WORD? NEWLINE+
    {self.current_line = int($line_number.text)}
    {self.current_file =  b64decode($filepath.text[3:]).decode()}
    {$source_file = self.current_file}
    {$source_line = self.current_line}
    {self.current_offset = $line_number.start.line - self.current_line + 1}
    ;

line_number: DECIMAL_NUMBER;
filepath: BASE64;

break_statement : Break NEWLINE+ ;
continue_statement : Continue NEWLINE+ ;

top_line: line;

ext_type
    : Ext   # globalExtType
    | File  # fileExtType
    | Weak  # weakExtType
    ;

label_suffix
    : COLON         # localLabelSuffix
    | ANGLE_BRACKET # globalLabelSuffix
    | COLON_ANGLE   # fileLabelSuffix
    | TILDE_ANGLE   # weakLabelSuffix
    ;

line
    : labels_declaration ext_type? NEWLINE+                    # standaloneLabels
    | labels_declaration? instruction arguments? NEWLINE+ # instructionLine
    ;

labels_declaration: labels label_suffix ;
labels: label (COMMA label)*;
arguments : argument (COMMA argument)* ;

conditional : If NEWLINE+ conditions code_block else_clause? Fi NEWLINE+ ;
conditions : connective_condition* condition NEWLINE+ (Then NEWLINE+)? ;
connective_condition : condition COMMA conjunction NEWLINE+ ;
condition : code_block Is branch_mnemonic ;
else_clause : Else NEWLINE+ code_block ;

branch_mnemonic : WORD ;
conjunction : WORD ;

while_loop : While NEWLINE+ while_condition Stays branch_mnemonic NEWLINE+ code_block Wend NEWLINE+ ;
while_condition : code_block ;

until_loop : Do NEWLINE+ code_block Until branch_mnemonic NEWLINE+ ;

argument
    : character
    | string
    | register
    | addr_expr
    | byte_expr
    ;

byte_expr : byte_specifier OPEN_PAREN addr_expr CLOSE_PAREN ;
addr_expr : first_term add_term* ;
first_term : (PLUS | MINUS)? term ;
add_term : (PLUS | MINUS) term ;
term : number | label ;
byte_specifier : name;

label : name ;
instruction : WORD ;
string : STRING ;
register : REGISTER ;
character : CHAR ;
number
    : DECIMAL_NUMBER
    | HEX_NUMBER
    | BINARY_NUMBER
    ;

name
    : Asect
    | Break
    | Continue
    | Do
    | Else
    | End
    | Ext
    | File
    | Weak
    | Fi
    | If
    | Is
    | Macro
    | Rsect
    | Stays
    | Then
    | Tplate
    | Until
    | Wend
    | While
    | WORD
    | WORD_WITH_DOTS
    ;
