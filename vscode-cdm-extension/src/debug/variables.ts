import { Scope, Variable } from "@vscode/debugadapter";
import { Mutex } from "async-mutex";

export interface WithVariable {
    get variable(): Variable;
}

export interface Provider {
    get ref(): number;

    slice(start?: number, count?: number): Variable[];
}

export interface Sized {
    get size(): number;
}

export class ReferenceController {
    private mutex = new Mutex();
    private issued = new Map<number, Provider>();
    private value = 1;

    public async resetCounter(): Promise<void> {
        await this.mutex.runExclusive(() => {
            this.issued.clear();
            this.value = 1;
        });
    }

    public async issueReference(factory: (ref: number) => Provider): Promise<Provider> {
        let ref!: number;
        await this.mutex.runExclusive(() => {
            ref = this.value;
            this.value += 1;
        });

        const provider = factory(ref);
        this.issued.set(ref, provider);

        return provider;
    }

    public retrieve(ref: number): Provider | undefined {
        return this.issued.get(ref);
    }
}

export class ParamVariable<T> implements WithVariable {
    protected readonly _variable: Variable;

    public constructor(
        public value: T,
        private name: string,
        public update?: () => T,
        public show?: (val: T) => string,
    ) {
        this._variable = new Variable(this.name, this.display());
    }

    protected display(): string {
        return this.show ? this.show(this.value) : "ACHTUNG: show callback isn't set";
    }

    public get variable(): Variable {
        this.value = this.update!();
        this._variable.value = this.display();

        return this._variable;
    }
}

export class ProviderParamVariable<T> extends ParamVariable<T> implements Provider {
    private readonly children: ParamVariable<any>[] = [];

    public constructor(
        public readonly ref: number,
        value: T,
        name: string,
        update?: () => T,
        show?: (val: T) => string,
    ) {
        super(value, name, update, show);
        this._variable.variablesReference = ref;
    }

    public addChildren(...paramVariable: ParamVariable<any>[]) {
        this.children.push(...paramVariable);
    }

    public slice(start?: number, count?: number): Variable[] {
        return this.children.slice(start, count ? (start! + count) : count).map((val) => val.variable);
    }
}

class Binary extends ParamVariable<number> {
    public constructor(source: ParamVariable<number>, size: number) {
        super(0, "BIN", () => source.value, (val) => val.toString(2).padStart(size, "0"));
    }
}

class Unsigned extends ParamVariable<number> {
    public constructor(source: ParamVariable<number>) {
        super(0, "UNS", () => source.value, (val) => val.toString(10));
    }
}

class Signed extends ParamVariable<number> {
    private readonly border: number;
    private readonly sub: number;

    public constructor(source: ParamVariable<number>, size: number) {
        super(0, "SIG", () => source.value);

        this.border = 2 ** (size - 1);
        this.sub = this.border * 2;
        this.show = (val) => {
            if (val >= this.border) {
                return (this.sub - val).toString(10);
            } else {
                return val.toString();
            }
        };
    }
}

class Hexadecimal extends ParamVariable<number> {
    public constructor(source: ParamVariable<number>, size: number) {
        super(0, "HEX", () => source.value, (val) => val.toString(16).toUpperCase().padStart(size / 4, "0"));
    }
}

class Register extends ProviderParamVariable<number> {
    public constructor(
        size: number,
        ref: number,
        value: number,
        name: string,
    ) {
        super(ref, value, name);
        const hex = new Hexadecimal(this, size);
        this.addChildren(
            new Binary(this, size),
            new Unsigned(this),
            new Signed(this, size),
            hex,
        );

        this.show = () => hex.variable.value;
    }

    public override get variable(): Variable {
        this._variable.value = this.display();

        return this._variable;
    }
}

export class RegisterProvider implements Provider {
    public readonly scope: Scope;
    private readonly registers = new Map<string, Register>();

    public constructor(
        controller: ReferenceController,
        public readonly ref: number,
        names: string[],
        sizes: number[],
    ) {
        this.scope = new Scope("REGISTERS", ref, false);
        for (let index = 0; index < names.length; index += 1) {
            controller.issueReference((ref) => {
                return new Register(sizes[index], ref, 0, names[index]);
            }).then((provider) => {
                const register = provider as Register;
                this.registers.set(register.variable.name.toLowerCase(), provider as Register);
            });
        }
    }

    public slice(start?: number, count?: number): Variable[] {
        return Array.from(this.registers.values()).slice(start, count ? (start! + count) : count).map((val) => val.variable);
    }

    public programCounter(): number {
        return this.registers.get("pc")!.value;
    }

    public processorState(): number {
        return this.registers.get("ps")!.value;
    }

    public update(values: number[]): void {
        let counter = 0;
        for (const register of this.registers.values()) {
            register.value = values[counter];
            counter += 1;
        }
    }
}
