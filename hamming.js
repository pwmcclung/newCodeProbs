function hamming(n) {
  if (n <= 0) {
    return 0;
  }
  let seq = [1];
  let i2 = 0;
  let i3 = 0;
  let i5 = 0;
  while (seq.length < n) {
    let next2 = seq[i2] * 2;
    let next3 = seq[i3] * 3;
    let next5 = seq[i5] * 5;
    let nextH = Math.min(next2, next3, next5);
    seq.push(nextH);
    if (nextH === next2) {
      i2++;
    }
    if (nextH === next3) {
      i3++;
    }
    if (nextH === next5) {
      i5++;
    }
  }
  return seq[n - 1];
}