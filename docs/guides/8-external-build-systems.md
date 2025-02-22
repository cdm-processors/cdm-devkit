# Using external build systems

You can use an external build system instead of integrated one. That way you need to create another task that will run your build system and then set this task as `preLaunchTask` in your launch configuration.

First of all, you need to set up your build system to produce two files:
- Program image (`.img`)
- Debug information (`.dbg.json`)

> [!TIP]
> Check out [Using CLI](./7-using-cli.md) to learn how to call assembler from command line

> [!IMPORTANT]
> Make sure to export debug information during build process
>
> In order to do it:
> - Add `--debug` to object file creation steps
> - Add `--debug <file>` to link step

For example, you want to build your project with `make`. That way you need to create a task that calls `make`, for example:

```json
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Make",  // Name of task
      "type": "shell",      // Execute command in shell
      "command": "make"     // Command to execute
    }
  ]
}
```

Then set this task as `preLaunchTask` in your launch configuration. 
Check that paths of artifacts point to files, produced by build system. 

> [!IMPORTANT]
> Make sure to fill in exact name of task as specified in `label` field.

```json
{
  "configurations": [
    {
      ...
      "artifacts": {
        "image": "<path to output image>",
        "debug": "<path to debug information file>"
      },
      "preLaunchTask": "Run Make"
      ...
    }
  ]
}
```

Now extension will use external build system to compile project.
