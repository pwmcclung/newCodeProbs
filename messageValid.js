function isAValidMessage(message){
  if (message.length == 0){
    return true;
  }
  let messSplit = message.split(/\d+/g)
  if ( messSplit[messSplit.length-1] == ''){
    return false;
  }
  let nums = message.match(/\d+/g);
  let words = message.match(/[^\d\s]+/g);
  let count = 0;
  for (let i = 0; i < words.length;i++){
    if (words[i].length == Number(nums[i])){
      count++;
    }
  }
  if (count == words.length){
    return true;
  }
  return false;
 
}