function areEqual(s1, s2){
  let arr1 = Array.from(s1);
  let arr2 = Array.from(s2);
  if (arr1.length != arr2.length){
    return false;
  }
   let sortedArr1 = arr1.slice().sort();
  let sortedArr2 = arr2.slice().sort();

  for (let i = 0; i < sortedArr1.length; i++) {
    if (sortedArr1[i] !== sortedArr2[i]) {
      return false; 
    }
  }
  return true; 
}

function notEqual(s1, s2){
let arr1 = Array.from(s1);
  let arr2 = Array.from(s2);
 if (arr1.length !== arr2.length) {
    return true; 
  }

  let sortedArr1 = [...arr1].sort(); 
  let sortedArr2 = [...arr2].sort();

  for (let i = 0; i < sortedArr1.length; i++) {
    if (sortedArr1[i] !== sortedArr2[i]) {
      return true; 
    }
  }
  return false;
  
}