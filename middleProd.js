function findMiddle(str){
    if (str != null){
      if (typeof str != 'string'){
       return -1;
      }
      let nums = '0123456789';
       let newNums = str.split('').filter((x)=> nums.includes(x));
       if (newNums.length == 0){
         return -1;
       }
       let prod = 1;
       for (let i = 0; i < newNums.length;i++){
           prod *= newNums[i];
       }
    prod = prod.toString()
    let lenProd = prod.length;
    if (lenProd % 2 == 0){
      let sliced = prod.slice(((lenProd /2)-1), (lenProd/2)+1);
      if (sliced[0] == '0'){
        return Number(sliced[1]);
      }else{
        return Number(sliced);
      }
    }else if (lenProd % 2 != 0){
      return Number(prod.slice((lenProd /2), (lenProd/2)+1))
    } 
    }
     return -1;  
  }