function skiJump(mountain){
  let jump = ((mountain.length * (mountain.length * 1.5)  * 9) / 10).toFixed(2);
  if (jump < 10){
    return `${jump} metres: He's crap!`;
  }else if (jump < 26){
    return `${jump} metres: He's ok!`;
  }else if (jump < 51){
    return `${jump} metres: He's flying!`;
  }else{
    return `${jump} metres: Gold!!`;
  }
  }