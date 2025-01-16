/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
//   return nums.reduce(fn, init)

    let res = init
    // for (const i of nums){
    //     res = fn(res, i)
    // }

    nums.forEach((i)=> res = fn(res, i))

    return res
};