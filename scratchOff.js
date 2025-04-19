function scratch(lottery){
  let sum = 0;
  for (let i = 0; i < lottery.length; i++ ){
    let lotSplit = lottery[i].split(' ');
    if (lotSplit[0] == lotSplit[1] && lotSplit[1] == lotSplit[2]){
      sum += Number(lotSplit[3]);
    }
  }
return sum;
}
