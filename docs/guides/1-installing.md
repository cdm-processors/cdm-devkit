# Installing `cdm-devkit`

Development kit consists of three main parts:
- Python package
- VS Code extension
- `cdm-devkit-misc-x.x.x` archive

## Python package

> [!IMPORTANT]
> Make sure you have `cocas` and `cocoemu-server` available in your PATH.
> Otherwise, or if you want to install package to managed environment, such as venv or conda, [check this article](./9-using-python-environments.md).

### Install from repository

Package is published on [PyPI](https://pypi.org/project/cdm-devkit).

```bash
pip install cdm-devkit
```

### Install from binary wheel

- Download `.whl` package from [release](https://github.com/cdm-processors/cdm-devkit/releases/latest) page
- Install package from file

```bash
pip install cdm_devkit-x.x.x-py3-none-any.whl
```

## VS Code extension

### Install from VS Code Marketplace

`CdM Processors` extension is published on [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=cdm-processors.vscode-cdm-extension).

### Install from binary package

- Download `.vsix` package from [release](https://github.com/cdm-processors/cdm-devkit/releases/latest) page
- In VS Code open Command Palette <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>
- Type `vsix`
- Select `Install from VSIX`
- Select `vscode-cdm-extension-x.x.x.vsix`
- [Read more](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix)

## Archive with miscellaneous files

- Download `.zip` or `.tar.gz` archive from [release](https://github.com/cdm-processors/cdm-devkit/releases/latest) page
- Unpack archive to some convenient place
