# Setting up Logisim

[Logisim](https://www.cburch.com/logisim/index.html) is a program that is used to simulate logical schemes.

## Quickstart

- Open `Logisim`
- Load desired processor
  - `Project > Load Library > Logisim Library`
  - Select desired `.circ` processor scheme (you can find one in `cdm-devkit-misc` archive)
  - Now you have new category with a processor name in Logisim's left menu
  - Get processor from this category and put it on your canvas
- Build your scheme
- Load assembled program (`.img` file) to your program memory
  - Right-click on memory chip and select `Load Image`
  - Select `.img` file (one that you got from `cocas`)
- Run the simulation with `Simulate` menu

> [!IMPORTANT]
> In Harvard architecture, where you have separate memory chips for `ROM` and `RAM`, you need to load image to `ROM` chip.
    
> [!TIP]
> Useful keyboard shortcuts:
> + <kbd>Ctrl</kbd> + <kbd>K</kbd> - toggle clock
> + <kbd>Ctrl</kbd> + <kbd>R</kbd> - reset simulation
> + <kbd>Ctrl</kbd> + <kbd>E</kbd> - toggle simulation

## Scheme templates

> [!IMPORTANT]
> Processor symbols may differ, but inputs and outputs are the same.

### CdM-8/8e

**CdM-8/8e in Von Neumann configuration:**
    
![cdm8-vn](../images/cdm8_vn.png)

<br>

**CdM-8/8e in Harvard configuration:**

![cdm8-hv](../images/cdm8_hv.png)

Here `instr memory` aka instruction memory is `ROM` and `data memory` is `RAM`.

### CdM-16

**With CdM-16 you should use special memory chips:**

- In `Logisim` go to `Project > Load Library > JAR Library` 
- Select `logisim-banked-memory-*.*.*.jar` that is located in `cdm-devkit-misc` archive in `jar` folder
- Now you have new category in Logisim's left menu that is called `BankedROM&RAM`
- You should use `ROM` and `RAM` from this category

These chips emulate real banked memory configurations and allow processor to read and write 2 bytes per bus cycle.

**CdM-16 in Von Neumann configuration:**

![cdm16-vn](../images/cdm16_vn_minimal.PNG)

Memory chip is `RAM` from `logisim-banked-memory`.

Harvard configuration is built the same way as with CdM-8/8e, but with memory from `logisim-banked-memory`. In this case `word` should be connected to both `RAM` and `ROM`.
