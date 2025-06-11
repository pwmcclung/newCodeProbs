function cupVolume(d1, d2, height){
  let pie = Math.PI;
  let rad1 = d1 / 2;
  let rad2 = d2 / 2;
  let volume = (1/3)*pie * height * (rad1**2 + rad2**2 + rad1*rad2);
  return volume
}