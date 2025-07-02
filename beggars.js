function distributionOf(golds) {
let beggarA = [];
  let beggarB = [];
  let turns = 0;
  let countLeft = 0;
  let countRight = golds.length-1;
  while (countLeft <= countRight){
    let left = golds[countLeft];
    let right = golds[countRight];
    if (turns % 2 == 0){
      if (left > right){
        beggarA.push(left);
        countLeft += 1;
      }else if (right > left){
        beggarA.push(right);
        countRight -= 1;
      }else{
        beggarA.push(left);
        countLeft += 1;
      }
    }else  if (turns % 2 != 0){
      if (left > right){
        beggarB.push(left);
        countLeft += 1;
      }else if (right > left){
        beggarB.push(right);
        countRight -= 1;
      }else{
        beggarB.push(left);
        countLeft += 1;
      }
    }
    turns += 1;
}
  let aSum = beggarA.reduce((a,b) => a + b,0);
  let bSum = beggarB.reduce((a,b) => a + b,0);
  return [aSum,bSum];
  }