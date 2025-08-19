function isSubsetOf(s1, s2){
  let arr1 = Array.from(s1);
  let arr2 = Array.from(s2);
  return arr1.every(item => {
    return arr2.includes(item);
  });
}

function isSupersetOf(s1, s2){
  let arr1 = Array.from(s1);
  let arr2 = Array.from(s2);
  return arr2.every(item => {
    return arr1.includes(item);
  });
}