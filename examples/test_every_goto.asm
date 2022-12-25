asect 0x00
ass01>
a1: ext
assC1: ext
ldi r1, ass02
ass02:
goto true, ass01
goto true, ass02
goto true, assC1
goto true, a1
goto true, assC2
halt


rsect abobus
ass01: ext
assC1: ext
a2:
a1>
goto true, ass01
goto true, assC1
goto true, a1
goto true, a2
goto true, ass02
goto true, assC2
halt


asect 0x12
ass01: ext
a1: ext
assC1>
goto true, ass01
goto true, assC1
goto true, assC2
goto true, a1
goto true, ass02
assC2:
end
