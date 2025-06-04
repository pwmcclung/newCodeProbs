function uglifyWord(s) {
  let letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  let flag = 1;
  let sSplit = s.split('');
  let newArr = [];
  for (let i = 0; i < sSplit.length;i++){
    if (letters.includes(sSplit[i]) && flag === 1){
      newArr.push(sSplit[i].toUpperCase());
      flag=0;
    }else if (letters.includes(sSplit[i]) && flag === 0){
      newArr.push(sSplit[i].toLowerCase());
      flag=1;
    }else{
      newArr.push(sSplit[i]);
      flag=1;
    }
  }
 return newArr.join('');
}
