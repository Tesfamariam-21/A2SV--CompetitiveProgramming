async function sleep(millis: number): Promise<void> {
    await new Promise((res, rej)=>{
        setTimeout(res, millis)
    })
    
}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */