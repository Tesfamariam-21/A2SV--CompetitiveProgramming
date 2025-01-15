/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let initial_val = init

    const increment = ()=> ++initial_val
    const decrement = ()=> --initial_val
    const reset = ()=> {
        initial_val = init
        return initial_val
    }

    return {
        increment: increment,
        decrement: decrement,
        reset: reset
    }  
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */