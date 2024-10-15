function pak(s){
    if (s.trim().length == 0){
    return '';
    }
   let sArr = s.split(' ');
   let newArr = [];
    for (let i = 0; i < sArr.length; i++){
      newArr.push(sArr[i]);
      newArr.push('pak');
    }
    return newArr.slice(0, newArr.length-1).join(' ');
  }