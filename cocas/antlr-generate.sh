antlr4 -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o generated \
    ./grammar/AsmLexer.g4 ./grammar/AsmParser.g4 ./grammar/Macro.g4 ./grammar/ObjectFileParser.g4 ./grammar/ObjectFileLexer.g4
