function twins(myArray){
    let newMyArray = myArray.slice().sort();
    let trues = [];
    while (newMyArray.length > 0){
      let first = newMyArray.shift();
      let second = newMyArray.shift();
      if (first != second || second == newMyArray[0]){
        trues.push('false');
      }else{
        trues.push('true');
      }
    }
    if (trues.includes('false')){
      return false;
    }
    return true;
  }