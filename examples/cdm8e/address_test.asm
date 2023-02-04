asect 0x00
code_start: ext
goto true, code_start







rsect test

code_start>
# load string length into r0
ldi r0, low(string_stop - string_start)
halt

string_start:
dc "Hello, wr5yrh5orld", low(0x0a), low(0x00)
string_stop:


end