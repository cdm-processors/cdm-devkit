# 'CdM Processors' extension for Visual Studio Code

A debug adapter and language definitions for CdM family assembly languages.

Marketplace Identifier: `cdm-processors.vscode-cdm-extension`.

## Getting a copy

### Stable release

Install [the extension](https://marketplace.visualstudio.com/items?itemName=cdm-processors.vscode-cdm-extension) from Visual Studio Code Marketplace.

### As fresh as possible

Clone the repository, [prepare the environment](https://github.com/cdm-processors/cdm-devkit/blob/master/README.md#visual-studio-code-extension) and [build](https://github.com/cdm-processors/cdm-devkit/blob/master/README.md#visual-studio-code-extension-1).

## Features

### Syntax highlighting and language snippets

#### Usage

Should work out of the box, however, if you want to set preferences for files manually, you can use the *Change Language Mode* command (<kbd>Ctrl</kbd> + <kbd>K</kbd> + <kbd>M</kbd> on Windows and Linux and <kbd>Command</kbd> + <kbd>K</kbd> + <kbd>M</kbd> on macOS).

### Debug Adapter for CdM Logisim Debugger

#### Prerequisites

- [**Logisim**](http://www.cburch.com/logisim/) digital circuit simulator;
- A circuit with the [**CdM Logisim Debugger**](THERE-SHOULD-BE-LINK-TO-DEBUGGER-CIRCUIT).

#### Setup

1. Create a `.vscode/launch.json` at the project root;
2. Click the *Add configuration* button and pick the one, that suits your needs;

> [!IMPORTANT]
> There is a known issue that CdM debug configurations are not displayed because Visual Studio Code does not activate the extension.
>
> Opening a `.asm`-file will send an activation event to Visual Studio Code, after which the configurations should appear in the list.

3. Add all project files to the `sources` configuration attribute so that they will be passed to `cocas` before the start of a debug session.

#### Usage

1. Open the debug circuit and start the debug server.
2. Press <kbd>F5</kbd> to start a debug session.

#### Functionality

Currently the debug adapter supports the next features:

- Displaying register values
- Breakpoints
- Memory map using the Hex Editor extension
- Watches (coming soon)
