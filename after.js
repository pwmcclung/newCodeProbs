function comes_after(str,l) {
  let letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  let newStr = str.split('');
  let arr = [];
  for (let i = 0; i < newStr.length; i++){
    if (newStr[i] == l.toUpperCase() || newStr[i] == l.toLowerCase()){
      arr.push(newStr[i+1]);
    }
  }
  return arr.filter((x)=> letters.includes(x)).join('')
}
