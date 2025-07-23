function eqSumPowdig(hMax, exp) {
 let count = 0;
  let start = 2;
  let arr = [];
  while (start < hMax+1){
    let numStr = String(start);
    let digStr = numStr.split('');
    let digPow = digStr.map(Number).map((x) => x**exp).reduce((a,b)=> a+b,0);
    if (digPow == start){
      arr.push(digPow)
    }
    start++;
  }
  return arr;
}