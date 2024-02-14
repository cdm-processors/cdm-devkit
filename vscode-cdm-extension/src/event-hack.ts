export type InnerScope<T> = {
    submit: (data: T) => void;
};

export type OuterScope<T> = {
    event: () => Promise<T>;
};

export type EventHack<T> = OuterScope<T> & InnerScope<T>;

export function createEventHack<T>(): EventHack<T> {
    let promiseResolve: (value: T) => void;

    let promise = new Promise<T>((resolve) => {
        promiseResolve = resolve;
    });

    return {
        submit: promiseResolve!,
        event: () => promise,
    };
};
