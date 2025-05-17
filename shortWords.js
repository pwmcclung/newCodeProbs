function shortForm(str) {
  let vowels = 'aeiouAEIOU';
  let strSplit = str.split('');
  let first = strSplit[0];
  let last = strSplit[strSplit.length-1];
  let middle = strSplit.slice(1,strSplit.length-1).filter((x) => !vowels.includes(x)).join('');
  return first.concat(middle).concat(last);
}
