function shifter(s){
    if (s==''){
      return '';
    }
    let shifter = 'HINOSXZMW'.split('');
    let sArr = s.split(' ');
    sArr = [...new Set(sArr)];
    let count = 0;
    let newArr = [];
   for (let  i = 0; i < sArr.length;i++){
     let word = sArr[i].split('');
     if (word.every((x)=>shifter.includes(x))){
         count++;
         }
   }
    return count;
  }