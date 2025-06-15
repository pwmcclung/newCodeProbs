function thirstyIn(water, ageOfDwellerArray) {
  
  let underEighteen = ageOfDwellerArray.filter((x)=> x < 18);
  let under50 = ageOfDwellerArray.filter((x) => x > 17 && x <51);
  let over50 = ageOfDwellerArray.filter((x) => x> 50);
  let dailyNeed = underEighteen.length * 1 + under50.length * 2 + over50.length * 1.5;
  let days =  Math.floor(water / dailyNeed);
  if (days % 1 === 0){
    return days;
  }
  return -1;
  
}