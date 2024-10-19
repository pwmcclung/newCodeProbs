function replaceCommon(string, letter) {
    let strObj = {};
    let arr = string.split('');
    let stringArr = string.split('').filter((x)=> x != ' ');
    for (let x of stringArr){
      if (strObj[x]){
        strObj[x] ++;
      }else {
        strObj[x] = 1;
      }
    }
    function getMax(obj){
          return Object.keys(obj).filter(x => {
               return obj[x] == Math.max.apply(null, 
               Object.values(obj));
         });
      };
    let maxArr = getMax(strObj);
    let smallIdx = maxArr.map((x) => arr.indexOf(x));
    let mini = Math.min(...smallIdx);
    let letterToXchange = arr[mini];
    let newArr = [];
    for (let i = 0; i < arr.length;i++){
       let first = arr[i];
       if (first == letterToXchange){
         newArr.push(letter);
       }else{
         newArr.push(arr[i]);
       }
    }
    return newArr.join('');
  }