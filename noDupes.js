function uniquePush(arr, obj) {
  if (!obj.phoneNumber) {
    return false; 
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].phoneNumber === obj.phoneNumber) {
      return false; 
    }
  }
  arr.push(obj);
  return true;
}