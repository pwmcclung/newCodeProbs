function sexyName(name) {
  let nameUpper = name.toUpperCase().split('');
  let score = nameUpper.map((x)=>SCORES[x] || 0).reduce((a,b) => a+ b,0);
  if (score > 599){
    return 'THE ULTIMATE SEXIEST';
  }else if (score > 300){
    return 'VERY SEXY';
  }else if (score > 60){
    return 'PRETTY SEXY';
  }else{
    return 'NOT TOO SEXY';
  }
}
