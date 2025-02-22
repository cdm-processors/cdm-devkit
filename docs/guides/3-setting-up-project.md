# Setting up a project

## Creating new configuration 

- Open a folder with VS Code
- Type <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> to open `Command Palette`
- Type `CdM` and select `CdM: Create a VS Code configuration` to configure your project
- You will be prompted some questions about project configuration
- Upon completion it will generate necessary configuration files in `.vscode` folder

## Configuration files

As mentioned before, configuration consists of two files:
- `tasks.json` defines tasks that are run to **build** your project and produce an image
- `launch.json` defines launch configurations that determine how your program will be run and debugged

## Build configuration

Build tasks are defined in `tasks.json`. These tasks should compile project and produce two artifacts:
- Image file with `.img` extension *(compiled program image)*
- Debug information file with `.dbg.json` extension *(debug information, e.g. line locations for compiled image)*

### Integrated build system

Extension provides a task that compiles a bunch of assembly sources.

Example of `tasks.json` using integrated build task:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Compile CdM-16",
      "type": "cocas",
      "target": "cdm16",
      "sources": [
        "main.asm",
        "lib/sadd.asm"
      ],
      "artifacts": {
        "image": "${workspaceFolder}${/}build${/}out.img",
        "debug": "${workspaceFolder}${/}build${/}out.dbg.json"
      }
    }
  ]
}
```

Breakdown:
- `label`: arbitrary name for task
- `type`: type of task, always `cocas`
- `target`: target processor architecture (`cdm16`, `cdm8`, `cdm8e`)
- `sources`: list of assembly files to compile
- `artifacts`: paths for produced artifacts
  - `image`: path for image file (`.img`)
  - `debug`: path for debug information file (`.dbg.json`)

> [!TIP]
> Typically, you should check that all necessary assembly files are listed in `sources` and appropriate `target` is selected.

### External build system

If you project requires more sophisticated build procedures, for example preprocessing or uses C compiler, you might need to use an external build system.

For more information on this topic check:
- [Assembler command line interface](./7-using-cli.md)
- [Writing build task for an external build system](./8-external-build-systems.md)

## Launch configuration

Launch configuration defines how your compiled program will be executed.

There are two environment types:
- `emulator`: program will be run in integrated emulator (**extension** is responsible for starting emulator)
- `external`: program will be run in external environment, such as Logisim (**user** is responsible for staring debug server, e.g. `logisim-debugger`)

Example of `launch.json`:

```json
{
  "configurations": [
    {
      "name": "Debug CdM-16 with Harvard architecture",
      "type": "cdm",
      "request": "launch",
      "address": "ws://localhost:7001",
      "target": "cdm16",
      "architecture": "harvard",
      "environment": "emulator",
      "artifacts": {
        "image": "${workspaceFolder}${/}build${/}out.img",
        "debug": "${workspaceFolder}${/}build${/}out.dbg.json"
      },
      "preLaunchTask": "Compile CdM-16"
    }
  ]
}
```

Breakdown:
- `name`: name of debug configuration
- `type`: type of debugger, always `cdm`
- `request`: type of debug request for VS Code, always `launch`
- `address`: address of debug server to connect to
  - For `emulator` environment, emulator will be started on port specified in this address
- `target`: target processor architecture (`cdm16`, `cdm8`, `cdm8e`)
- `architecture`: memory architecture 
  - `harvard`: separate program and data memory
  - `vonNeumann`: shared program and data memory
- `environment`: debug environment (`emulator`, `external`)
- `artifacts`: paths for artifacts, produced by build step
  - `image`: path for image file (`.img`)
  - `debug`: path for debug information file (`.dbg.json`)
- `preLaunchTask`: task that will be run before starting session (specify exact name of build task). If this field is absent, no build task will be run
