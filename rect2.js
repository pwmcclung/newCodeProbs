function getRectangleString(width, height) {
  if (width && height  <= 1){
    return '*\r\n';
  }
  if (width == 1 && height ==2){
    return '*\r\n'+'*\r\n';
  }
  let first = '*'.repeat(width)+'\r\n';
  let last = '*'.repeat(width) + '\r\n';
  let mids = '*' + ' '.repeat(width - 2) + '*' + '\r\n';
  return first + mids.repeat(height-2)+last;
}
