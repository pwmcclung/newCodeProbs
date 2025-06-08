var sumAndMultiply = function(sum, multiply){
  return multCheck(sumCheck(sum), multiply);
}

function sumCheck(sum){
  let num1 = 0 ;
  let num2 = sum;
  let arr = [];
  let empArr = [];
  while (num2 != 0 && num1 != sum){
    if ((num1 + num2 == sum)){
      empArr.push(num1);
      empArr.push(num2);
      num1++;
      num2--;
      arr.push(empArr)
      empArr = [];
    }
  }
  return arr;
}

function multCheck(arr, multiply){
  let multArr = [];
  for (let x of arr){
    if (x[0] * x[1] == multiply){
      multArr.push(x)
    }
  }
  if (multArr.length > 0){
    return multArr[0];
  }
  return null;
}
