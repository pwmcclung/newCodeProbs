function validateNumber(str){
    let nums = '0123456789';
    let arr = str.split('').filter( (x) => nums.includes(x)).join('');
     let len = arr.length;
     if (len == 11){
       let first = arr.slice(0,2);
       if (first == '07'){
         return 'In with a chance';
       }else{
         return 'Plenty more fish in the sea';
       }
     }else if (len == 12){
       let first = arr.slice(0,3);
       if (first == '447'){
         return 'In with a chance';
       }else{
         return 'Plenty more fish in the sea';
       }
     }
      return 'Plenty more fish in the sea';
    }