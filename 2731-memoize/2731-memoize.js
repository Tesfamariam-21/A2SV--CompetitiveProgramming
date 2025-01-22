/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
        const memo = new Map()

    return function(...args) {
        // key = JSON.stringify(args)
        // when using object {} it automatically changes args to string 
        //but if you used map since it supports different data types as a key value we must change it
        // to string in this case

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