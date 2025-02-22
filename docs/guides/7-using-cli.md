# Using CLI tools

Development kit provides several CLI tools:
- `cocas`: assembler and linker
- `cocodump`: disassembler
- `synthm`: decoder synthesis utility
- `cocoemu-server`: CdM emulator with CDP support

These tools support all existing CdM processors.

This guide will show some common use cases for these tools.
You can run any tool with `-h` or `--help` flag to get full description of all flags.

## cocas

`cocas` is a tool used to compile and link assembly source files. Moreover it can produce object files, export debug information and create static libraries.

### Compiling assembly sources

```bash
cocas -t cdm16 -o program.img foo.asm bar.asm
```

This command will compile `foo.asm` and `bar.asm` for CdM-16 processor, link and create `program.img` output image file.

### Compiling assembly sources with debug information

```bash
cocas -t cdm16 --debug program.dbg.json -o program.img foo.asm bar.asm
```

This command will do the same as previous one, but in addition debug information will be exported to `program.dbg.json` file.

### Compiling assembly sources to object files

```bash
cocas -t cdm16 -c foo.asm bar.asm
```

This command will assemble `foo.asm` and `bar.asm` and create `foo.obj` and `bar.obj` object files without linking.

### Creating static library from object files

```bash
cocas -t cdm16 -o baz.lib -m foo.obj bar.obj
```

This command will merge `foo.obj` and `bar.obj` into `baz.lib` static library.

### Linking with libraries

```bash
cocas -t cdm16 -o program.img start.asm baz.lib faz.obj
```

Assembly sources, object files and libraries may be passed to `cocas` to link final image.

### Omitting output file name

If `-o` or `--debug` flags are used without name, files will be created with default names.

When producing object files with debug information, name should be omitted as debug info is stored in object files themselves.

### Output image formats

Format of output image file depends on its extension:
- `.img`: Logisim image format
- **other**: binary image

### Selecting target

```bash
cocas -t cdm8 foo.asm bar.asm
```

Target processor is selected with `-t` flag. Example values: `cdm8`, `cdm8e`, `cdm16`. 

## cocodump

`cocodump` is used to recover assembly source code from compiled image.

Features:
- Label inference
- Repeated instruction folding
- [IVT](../cdm16/cdm16-overview.md#startup-and-ivt) decoding *(for CdM-16)*

> [!IMPORTANT]
> Note that after compiling a program some information is lost.
> For example, macro commands are lost and can only be recovered in expanded form.

```bash
cocodump -t cdm16 --ivt --colored out.img
```

This command will output disassembled source code of `out.img`.

Breakdown:
- `-t cdm16`: decoding in CdM-16 mode
- `--ivt`: try to decode IVT
- `--colored`: produce colored output

If you want to dump output to file, omit `--colored` flag and pipe output to some file.

## synthm

`synthm` is a tool used to compile microcode definitions for CdM processors. It generated compiled binary image as well as secondary decoder circuit for Logisim.

```bash
synthm -i cdm16_decoder.def
```

This command will compile `cdm16_decoder.def` microcode definition file and produce secondary decoder circuit and microcode binary image.

## cocoemu-server

`cocoemu-server` is an CdM emulator that acts as CDP server. Upon startup it listens to incoming connections from debug clients.

```bash
cocoemu-server --port 7005
```

This command will start emulator with server on 7005 port.
