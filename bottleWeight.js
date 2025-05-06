function contentWeight(bottleWeight, scale) {
  let multiplier = parseInt(scale) + 1;
  let num = parseInt(scale);
  let baseNum = bottleWeight / multiplier;
  if (scale.includes('larger')){
    return baseNum * num;
  }else{
    return baseNum;
  }
}
