function asteriscIt(n) {
 if (typeof n == 'object'){
   n = n.join('');
 }else if (typeof n == 'number'){
   n = String(n);
 }
  let nString = n.split('');
  let arr = [];
  for (let i = 0; i < nString.length;i++){
    if (Number(nString[i]) % 2 ==0 && Number(nString[i+1]) % 2 == 0){
      arr.push(nString[i]);
      arr.push('*');
    }else{
      arr.push(nString[i]);
    }
  }
  return arr.join('');
};