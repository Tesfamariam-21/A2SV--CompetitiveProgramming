function createHelloWorld() {
    
    return function(...args: any[]) {
        return "Hello World";
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */