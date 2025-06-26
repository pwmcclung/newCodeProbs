function fistBeard(arr) {
  return  arr.flat().map((x) => String.fromCharCode(x)).join('');
}