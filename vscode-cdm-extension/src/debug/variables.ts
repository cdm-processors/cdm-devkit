import { Variable } from "@vscode/debugadapter";

interface Representation {
    get variable(): Variable;
}

class Binary implements Representation {
    private _variable: Variable;
    prefix: string = "BIN";
    radix: number = 2;

    constructor(
        protected register: Register,
    ) {
        this._variable = new Variable(this.prefix, "");
    }

    get variable(): Variable {
        this._variable.value = this.register.value.toString(this.radix).padStart(this.register.size, "0");
        return this._variable;
    }
}

class Decimal implements Representation {
    private _variable: Variable;
    prefix: string = "DEC";
    radix: number = 10;

    constructor(
        protected register: Register,
    ) {
        this._variable = new Variable(this.prefix, "");
    }

    get variable(): Variable {
        this._variable.value = this.register.value.toString(this.radix);
        return this._variable;
    }
}

class Hex implements Representation {
    private _variable: Variable;
    prefix: string = "HEX";
    radix: number = 16;

    constructor(
        protected register: Register,
    ) {
        this._variable = new Variable(this.prefix, "");
    }

    get variable(): Variable {
        this._variable.value = this.register.value.toString(this.radix).padStart(this.register.size >> 2, "0");
        return this._variable;
    }
}

export interface VariableProvider {
    matches(variablesReference: number): boolean;

    sliceVariables(from: number, quantity?: number): Variable[];
}

export interface RegisterController extends VariableProvider {
    initialize(variablesReference: number, names: string[], sizes: number[]): number;

    set(values: number[]): void;

    find(variablesReference: number): VariableProvider | undefined;

    programCounter(): number;
}

class Register implements VariableProvider {
    private _value: number = 0;
    private _variable!: Variable;
    private _repr: Representation[] = [];

    constructor(
        readonly name: string,
        public size: number,
    ) {}

    get value(): number {
        return this._value;
    }

    set value(newValue: number) {
        this._value = newValue;
        this._variable.value = this._value.toString();
    }

    get variable(): Variable {
        return this._variable;
    }

    index(current: number): number {
        current += 1;
        this._variable = new Variable(this.name, this._value.toString());
        this._variable.variablesReference = current;
        this._repr.push(new Binary(this), new Decimal(this), new Hex(this));
        return current;
    }

    matches(variablesReference: number): boolean {
        return this._variable.variablesReference === variablesReference;
    }

    sliceVariables(from: number, quantity?: number | undefined): Variable[] {
        quantity ??= this._repr.length;
        return this._repr.slice(from, from + quantity).map((v) => v.variable);
    }
}

export class Cdm16VariableProvider implements RegisterController {
    private registers: Register[] = [];
    private pc_index!: number;

    initialize(variablesReference: number, names: string[], sizes: number[]): number {
        for (let index = 0; index < names.length; index += 1) {
            const register = new Register(names[index], sizes[index]);
            variablesReference = register.index(variablesReference);
            this.registers.push(register);

            if (names[index].toLowerCase() === "pc") {
                this.pc_index = index;
            }
        }

        return variablesReference;
    }

    set(values: number[]) {
        values.forEach((value, index) => this.registers[index].value = value);
    }

    find(variablesReference: number): VariableProvider | undefined {
        if (this.matches(variablesReference)) {
            return this;
        }

        for (const register of this.registers) {
            if (register.matches(variablesReference)) {
                return register;
            }
        }
    }

    matches(variablesReference: number): boolean {
        return 1 === variablesReference;
    }

    sliceVariables(from: number, quantity?: number | undefined): Variable[] {
        quantity ??= this.registers.length;
        return this.registers.slice(from, from + quantity).map((v) => v.variable);
    }

    programCounter(): number {
        return this.registers[this.pc_index].value;
    }
}
