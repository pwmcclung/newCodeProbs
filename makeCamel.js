function zebulansNightmare(functionName) {
  let functionNameArr = functionName.split('_');
  let newArr = [functionNameArr[0]];
  for (let i = 1; i < functionNameArr.length;i++){
    let firstLetter = functionNameArr[i].slice(0,1).toUpperCase();
    let lastPart = functionNameArr[i].slice(1,).toLowerCase();
    let word = firstLetter+lastPart;
    newArr.push(word);
  }
  return newArr.join('');
}
