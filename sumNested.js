const sumNested = arr => {
  return arr.flat(Infinity).reduce((a,b)=> a + b,0);
};