function area(d,l){
    if (d <= l){return 'Not a rectangle'};
    let area = l * Math.sqrt(d**2 - l**2);
    return Number(area.toFixed(2));
  }