# Developer tools for Coco-de-Mer processors

## Installation

- Install [Python package](https://pypi.org/project/cdm-devkit) with `pip install cdm-devkit`.
- Install [CdM Processors](https://marketplace.visualstudio.com/items?itemName=cdm-processors.vscode-cdm-extension) VS Code extension
- Download `-misc` archive from [release](https://github.com/cdm-processors/cdm-devkit/releases/latest) page

For more information check out [this](./docs/guides/1-installing.md) guide.

## Development kit contents

### CLI Programs

- `cocas` - assembler and linker
- `cocodump` - disassembler
- `synthm` - secondary decoder synthesis utility
- `cocoemu-server` - CdM emulator with CDP support

### Visual Studio Code Extension

- Syntax highlighting and code snippets for CdM assembly languages
- Debug support
- Integrated build system

### `cdm-devkit-misc` archive

- Logisim processor implementations (`./`)
- Logisim libraries (`jar/`)
  - `logisim-banked-memory` - banked memory for CdM-16
  - `logisim-cdm-emulator` - emulated CdM processors
  - `logisim-debugger` - debugger for Logisim

## Documentation

For guides and technical information check out [Documentation](./docs/README.md).

It is available in `docs/` directory.

## Report a bug

If you encountered a one, we recommend to report it using GitHub Issues:

- Open a new issue using [this template](https://github.com/cdm-processors/cdm-devkit/issues/new?template=bug_report.md)
- Provide a proper name and description
- Provide the information on how to reproduce the bug

## Setting up development environment

### Python-based projects

- Install [**Poetry**](https://python-poetry.org/docs/#installation)
- Run `poetry install` at the project root

### Java-based projects

- Install **JDK**
- **Gradle** build system should be downloaded by `gradlew` script automatically on first run

### Visual Studio Code extension

- Install [**Node.js**](https://nodejs.org/en)
  - You will need a package manager, so it's recommended to get a provided **npm** binary from **Node.js** installer
  - However, if you really understand what are you doing, you can use your favorite package manager such as **pnpm**, **Yarn** or (if you are on the cutting edge of progress) even **Bun**
- Navigate to `vscode-cdm-extension`
- Run `npm install`

## Building

### Building individual projects

#### Python-based projects

- Run `poetry build`

#### Java-based projects

- Navigate to project folder;
- For UNIX-like systems:
  - Run `./gradlew jar`
- For Windows:
  - Run `.\gradlew.bat jar`

#### Visual Studio Code extension

- Navigate to `vscode-cdm-extension`
- Run `npx @vscode/vsce package`

### Building all projects at once

There is a handy `Makefile` that will build all projects and prepare artifacts for distribution: just run `make` to build all projects.

> [!TIP]
> You can set a `VERSION` variable if you want to specify the project version; note that it should be a valid [SemVer](https://semver.org/) version.
>
> Example: `make VERSION=1.2.3`

## Contributing

If you want to participate in the development of the project, we are open to your **pull requests**!

> [!IMPORTANT]
> We expect all commit messages to comply [these guidelines](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53) and use **scope identifier(s)** - the name of the subproject enclosed in square brackets. However, if the commit applies to the entire repository, **scope identifier** must be omitted.

An example message: `[cocas] Add new target`

### Scope identifiers

#### General

- `docs`
- `ci/cd`
- `examples`
- `tests`

#### Processor implementations

- `cdm*`

#### Projects

- `cocas`
- `cocoemu`
- `cocodump`
- `synthm`
- `cdp-java`
- `logisim-banked-memory`
- `logisim-cdm-emulator`
- `logisim-runner`
- `vscode-cdm-extension`

## Contact us

If you have a proposal or a suggestion, you are free to open a GitHub Issue [here](https://github.com/cdm-processors/cdm-devkit/issues/new?template=feature_request.md).

For other questions, use these contacts:
- Email: [n.repin@g.nsu.ru](mailto:n.repin@g.nsu.ru)
- Telegram: [@cdm_updates](https://t.me/cdm_updates)
  - *(channel with updates, linked chat for support)*
