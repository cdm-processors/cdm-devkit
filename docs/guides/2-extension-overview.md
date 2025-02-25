# VS Code extension overview

VS Code extension allows you to edit, compile and debug code for CdM processors.

## Language support

Extension provides syntax highlighting and snippets for several languages:
- CdM-16, CdM-8/e assembly language
- Microcode definition language

You can select language mode with <kbd>Ctrl</kbd> + <kbd>K</kbd>, <kbd>M</kbd>.

## Running code

In order to run a program two steps should be done:
- Compile sources *(for this, extension provides a build system)*
- Run compiled program in some environment *(emulator or external, such as Logisim)*

In particular, when user starts debug:
- Extension calls one of tasks defined in `tasks.json` to compile program, if specified
- Extension connects to debug environment according to selected configuration defined in `launch.json` and starts program execution  

Next time, or if restart button is pressed, the same steps are done.

## Debugging features

When debugging, user is able to:
- Suspend execution of program at any point
  - Breakpoint
  - `Pause` button
  - Exception *(for CdM-16)*
- Single-step program *(execute one instruction and stop)*
- Examine contents of registers
- Examine contents of RAM
- Examine state of hardware *(for Logisim)*
- Resume normal execution of program
