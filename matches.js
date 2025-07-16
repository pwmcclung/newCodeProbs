let countCombinations = function(string, key){
  if (string == '' || key == ''){return 0}
  let reg = new RegExp(key, "gi");
  let matches = string.match(reg);
  if (matches){
    return matches.length;
  }
  return 0;
}