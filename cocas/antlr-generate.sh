antlr4 -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o object_file/generated \
    object_file/grammar/ObjectFileParser.g4 object_file/grammar/ObjectFileLexer.g4
antlr4 -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o assembler/generated \
    assembler/grammar/AsmLexer.g4 assembler/grammar/AsmParser.g4 assembler/grammar/Macro.g4
