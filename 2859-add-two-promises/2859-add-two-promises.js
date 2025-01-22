/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // const [val1, val2] = await Promise.all([promise1, promise2])
    // return val1 + val2

    // return Promise.all([promise1, promise2]).then(values=> values[0] + values[1])
    
    // return promise1.then(val1 => promise2.then(val2=> val1 + val2))

    // return new Promise((reslove) =>{
    //     promise1.then(val1=> {
    //         promise2.then(val2 => {reslove(val1 + val2)})
    //     })
    // })
    return Promise.all([promise1, promise2]).then(values => values.reduce((acc, cur)=> acc + cur))
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */