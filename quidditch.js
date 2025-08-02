function gameWinners(gryffindor, slytherin) {
  let gryfScore = gryffindor[0];
  let slyScore = slytherin[0];
  if (gryffindor[1] == 'yes'){gryfScore += 150};
  if (slytherin[1] == 'yes'){slyScore+=150};
  if (gryfScore > slyScore){
    return 'Gryffindor wins!';
  }else if (slyScore > gryfScore){
    return 'Slytherin wins!';
  }else{
    return "It's a draw!";
  }
};