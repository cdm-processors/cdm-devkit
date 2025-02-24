# **`cdm-devkit`** quickstart

This guide contains brief information about using development kit.
It is highly recommended to check out [guides](./README.md) for detailed information on topics.

## Installing

- Install [Python package](https://pypi.org/project/cdm-devkit) with `pip install cdm-devkit`
- Install [CdM Processors](https://marketplace.visualstudio.com/items?itemName=cdm-processors.vscode-cdm-extension) VS Code extension
- Download `-misc` archive from [release](https://github.com/cdm-processors/cdm-devkit/releases/latest) page

Related guides:
- [Installing](./guides/1-installing.md)

## Setting up project

Run `CdM: Create a VS Code configuration` command in VS Code, follow the prompts.

Related guides:
- [Extension overview](./guides/2-extension-overview.md)
- [Setting up project](./guides/3-setting-up-project.md)
- [Debugging](./guides/4-debugging.md)

## Debugging in emulator

Select `emulator` environment when configuring your project and run debug.

Related guides:
- [Debugging](./guides/4-debugging.md)

## Debugging in Logisim

- Load `logisim-debugger` plugin in Logisim, place `Debugger` component on root circuit near the processor and push `Start` button
- In VS Code select `external` environment when configuring your project and run debug

Related guides:
- [Debugging](./guides/4-debugging.md)
- [Setting up Logisim](./guides/5-setting-up-logisim.md)
- [Debugging in Logisim](./guides/6-debugging-in-logisim.md)
