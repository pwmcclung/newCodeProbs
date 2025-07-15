function makesTheSentence(characterArray, sentenceString) {
  let  arr1 =characterArray.sort().join('')
  let str = sentenceString.replace(/\s/g,"").split('').sort().join('');
  if (arr1 === str){
    return true
  }else{
    return false
  }
}