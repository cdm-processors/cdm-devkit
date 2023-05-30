
interface ResolvablePromise<T> extends Promise<T>{
    resolve: (value: T) => void
}

export function createResolvable<T>(): ResolvablePromise<T>{
    let resolve!: (v: T)=>void;
    const promise: ResolvablePromise<T> = new Promise<T>((res, rej) =>{
        resolve = res;
    }) as ResolvablePromise<T>;
    promise.resolve = resolve;
    return promise;
}