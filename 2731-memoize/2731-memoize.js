/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const memo = {}

    return function(...args) {
        // key = JSON.stringify(args)
        key = args


        if (key in memo){
            return memo[key]
        }

        // if(memo[key]) return memo[key]
        // Purpose: This checks whether the value of memo[key] is truthy. 
        //In JavaScript, values like 0, null, undefined, NaN, false, and empty strings ('') 
        //are considered falsy.

        memo[key] = fn(...args)        
        return memo[key] 
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */