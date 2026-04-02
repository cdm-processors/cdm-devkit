# Defining macro in assembly source file

You can define macro right in your assembly source file. Every such macro definition has following structure:

```
macro <name>/<arity>
	<macro body>
mend
```

1. First line - **macro header**, consist of keyword `macro`, name of the macro and its arity.
2. Macro body - several lines of assembly code. Here you can use **macro parameters** (if arity of macro isn't 0), **nonce**, **macro variables** and **macro instructions** which will be described later.
3. Last line - **macro footer** - keyword `mend` marking the end of macro definition.

## Macro parameters

You can use macro parameters passed to macro with `$` + number of parameter (numeration of parameters starts from 1), all parameters will be just substituted into macro body:

```
# Defining macro ldv
macro ldv/2
	ldi $1, $2
	ldw $1, $1
mend

rsect main
main>
	# Using macro ldv
	ldv r0, label

	halt
end
```

This will expand into following:

```
rsect main 
main> 
	ldi r0, label
	ldw r0, r0

	halt
end 
```

## Nonce

If you need to use some unique label name in macro, you can use **nonce** (an apostrophe):

```
macro uselessMacro/1
loop':
	dec $1
	bnz loop'
mend	
```

**Nonce** will expand into some number, unique for each macro expanding, e.g.:

```
ldi r0, 5
uselessMacro r0 # In this macro expansion ' will be replaced by 1. So, label in substituted code will have name `loop1`
ldi r0, 10
uselessMacro r0 # In this macro expansion ' will be replaced by 2
```

## Macro instructions

There is some instructions you can use in macros:

- `unique`
- `mpush`
- `mpop`

### unique

If you need to select register which is different from some registers passed as **macro arguments**, you can use **unique** macro instruction, e.g.:

```
macro multBy10/1
	unique $1, temp # Stores register, different from $1 in macro variable temp

	move $1, ?temp # ?temp will be replaced by value of macro variable
	
	shl $1 

	shl ?temp
	shl ?temp
	shl ?temp

	add ?temp, $1
mend
```

### mpush and mpop

If you need to pass some pieces of text through several macros, you can use **macro stack** - LIFO memory existing at compilation time.

- `mpush` pushes specified piece of text (or several pieces) on macro stack
- `mpop` pops pieces from stack to specified **macro variables** (or several variables, one by one)

E.g.:

```
# $1 <= $2 <= $3
macro isInBound/3
  cmp $2, $1
  blo alt' # If $2 < $1, branches to alt'

  cmp $2, $3
  bhi alt' # If $2 > $3, branches to alt'

  mpush alt' # Push alt' on macro stack to let another macro place this label
mend

macro notInBound/0
  mpop where # Pop label pushed by isInBound
  mpush new?where # Push new label, which will lead to end of this if block
  br new?where
  ?where:  # Place label pushed by isInBound
mend

macro fiInBound/0
  mpop term # Pop label pushed by notInBound
  ?term: # Place this label
mend

rsect main
main>
	ldi r0, 2
	isInBound 1, r0, 3
		ldi r0, 1
	notInBound
		ldi r0, 0
	fiInBound

	halt
end
``` 

# Creating macro library (.mlb)

Instead of defining macros right in assembly files, you can store them separately, in **macro libraries** - .mlb files, and then just pass them to cocas with another sources, which use macros from library.

Defining of mlb macro is a little bit different from defining macro in assembly file:

```
*<name>/<arity>
	<macro body>

*<another name>/<arity>
	<macro body>
```

For example, here is `ldv` macro from beginning of the guide, defined as mlb macro:

```
*ldv/2
	ldi $1, $2
	ldw $1, $1
```

# Include macro directive

If you need to insert in your file content of another file, you can use `include <filename>` macro directive, it will macroprocess specified file (all macros definied in including file will be available in included file and vice versa) and insert processed text into including file. 

Firstly, cocas will try to find specified file in same directory with including file, if there is no such file, it will try to find it in specified **include paths**. You can specify this paths with `-I` option of cocas:

```bash
cocas -I ./headers -I ./another_headers -o test.img test.asm
```

It is useful, when you want to create some static library and link it with your programms. Instead of declaring every external label from this lib in every source file, you can declare all this labels in some header file and include it in every source file, which use this lib.

Also, you can create files, which contain some tplates, incldude and use them in multiple files.

> [!TIP]
> Technically, you can include some code blocks or macro definitions from another source files, but better practice will be using **separete compilation** and **macro libraries** for these purposes instead.
