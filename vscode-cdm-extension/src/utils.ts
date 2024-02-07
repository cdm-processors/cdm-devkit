export type Ping<T> = {
    ping: (data: T) => void;
};

export type Pong<T> = {
    pong: () => Promise<T>;
};

export type PingPong<T> = Ping<T> & Pong<T>;

export const createPingPong = <T>(): PingPong<T> => {
    let promiseResolve: (value: T) => void;

    let promise = new Promise<T>((toResolve) => {
        promiseResolve = toResolve;
    });

    return {
        ping: promiseResolve!,
        pong: () => promise,
    };
};
