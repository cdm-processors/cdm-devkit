# Developer tools for Coco-de-Mer processors

## Installation

1. **Download** [latest version](https://github.com/cdm-processors/cdm-devkit/releases/latest)

2. **Install Python package** from `.whl` file
    - Run `pip install cdm-devkit-x.x.x.whl`

    <br>

    > Package will be published to PyPI soon 

3. **Install VS Code extension** from `.vsix` file
    
    > Remove all other extensions that add support for CdM processors

    - Open Command Palette `Ctrl+Shift+P`
    - Type `vsix`
    - Select `Install from VSIX`
    - Select `vscode-cdm-extension-x.x.x.vsix`
    - [Read more](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix)
    
    <br>

    > Extension will be published to VS Code Marketplace soon 

## Development kit contents

After installation you get several components:

- **CLI Programs**
    
    - `cocas` - universal assembler for CdM processors
    - *(coming soon)*

- **VS Code Extension**

    - Assembler language support for all CdM processors (syntax highlighting and code snippets)
    - Debug support *(coming soon)*

- **cdm-devkit-misc** archive

    - Processor implementations (`./`)
    - Logisim libraries (`jar/`)
        
        - `logisim-banked-memory` - banked memory for `cdm16`
        - `logisim-cdm-emulator` - emulated CdM processors
    - Code and scheme examples (`examples/`)

## Getting started

Check out our [Getting Stated](/docs/getting-started.md) guide.

## Documentation

We are wokring on documentation, it will be available soon.

However, some docs are available in `docs/` directory.

## Report a bug

You can report a bug with GitHub Issues.

- Open new issue [here](https://github.com/cdm-processors/cdm-devkit/issues)

- Provide a proper name and description of a problem

- Provide information on how to repoduce a bug

## Setting up development environment

- **Python-based projects** use `Poetry` as build system

    - [Install](https://python-poetry.org/docs/#installation) `Poetry`

    - Run `poetry install` to download dependencies

    > `cocas` uses `ANTLR` to parse assembly language
    >
    >    - `antlr4-python3-runtime` is needed to run `cocas` and is installed with other dependenices
    >
    >   - However, if you want to fiddle with grammar files and generate new parser you would need to install `antlr4-tools`, this package is installed with development dependencies ([Read more](https://www.antlr.org))

- **Java-based projects** use `Gradle` as build system

    - Install `JDK`

    - `gradlew` script should download `Gradle` automatically on first run

- **VS Code Extension** uses [official tools](https://code.visualstudio.com/api)

## Building

### Building indivilual projects

- **Python-based projects:**

    - Run `poetry build`

- **Java-based projects:**
    
    - Navigate to project folder

    - Run `./gradlew jar` (on Unix)
    - Run `.\gradlew.bat jar` (on Windows)

- **VS Code extension:**

    - Navigate to `vscode-cdm-extension/`

    - Run `vsce package`

### Building all projects at once

There is a `Makefile` that will build all projects and prepare files for distribution

- Run `make` to build all projects

<br>

Set `VERSION` variable if you want to specify project version
- Example: `make VERSION=1.2.3`
- `VERSION` should be valid SemVer version

<br>

> You can get `make` on Windows from GnuWin32 project.
> - For Windows 10 and above: 
>   - Run `winget install GnuWin32.Make`
>   - Maybe you would need to add `bin/` directory of make to your `PATH`
> - Using `Chocolatey`:
>   - Run `choco install make` 
> - You can read about other installation methods [here](https://gnuwin32.sourceforge.net/packages/make.htm)

## Contibuting

- All contributions should be done via **pull requests**.

- Commit messages should be written accoring to [these guidelines](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53)

- Commit messages should start with a **scope indetifier** - project name surrouneded by square brackets. That will help to determine which project commit belongs to.

**Example:** `[cocas] Add new feature`

> Commits related to whlole repository shouldn't use scope indetifier

**Possible scope indetifiers are:**

- **General:**
    
    - `docs`
    - `ci`/`cd`
    - `examples`
    - `tests`

- **Processor implemetations:**

    - `cdm*`

- **Projects:**

    - `cocas`
    - `cocemu`
    - `logisim-banked-memory`
    - `logisim-cdm-emulator`
    - `vscode-cdm-extension`

## Contact us

- If you have a proposal or a suggestion you are free to open a GitHub Issue [here](https://github.com/cdm-processors/cdm-devkit/issues).

- For other questions contact *some way of communicating here*