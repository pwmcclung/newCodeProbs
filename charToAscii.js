function charToAscii(string){
    let strArray = string.split('');
    if (strArray.length < 1){return null;}
    let newStrArr = strArray.join('').replace(/[^a-zA-Z]/g, ' ').replaceAll(" ", "").split('');
    let newStr1 = removeDups(newStrArr);
    let asciiArr = [];
    let setArrStr = newStr1.join('');
    for (let i = 0; i < setArrStr.length;i++){
      asciiArr.push(setArrStr.charCodeAt(i));
    }
   const hashTable = newStr1.reduce((obj, key, index) => {
    obj[key] = asciiArr[index];
    return obj;
  }, {});
    if (hashTable.length == 0){
      return null;
    }
   return hashTable;
  }
  function removeDups(arr){
    return [...new Set(arr)];
  }