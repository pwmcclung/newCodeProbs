function palindrome(str) {
    str = str.toLowerCase();
    let consonants = 'bcdfghjklmnpqrstvwxyz'.split('');
    let vowels = 'aeiou'.split('');
    let newStr1 = str.split('');
    let cons = [];
    let vows = [];
    for (let i = 0; i < newStr1.length;i++){
      if (consonants.includes(newStr1[i])){
        cons.push(newStr1[i])
      }else if (vowels.includes(newStr1[i])){
        vows.push(newStr1[i]);
      }
    }
    cons = cons.join('');
    vows = vows.join('');
    if (pali(cons) == true && pali(vows) == true){
      return 'both';
    }else if (pali(cons) == true && pali(vows)== false){
      return 'consonant';
    }else if (pali(vows) == true && pali(cons) == false){
      return 'vowel';
    }else{
      return 'neither';
    }
  }
  
  function pali(str){
    let newStr = str.split('').reverse().join('');
    if (newStr == str){
      return true;
    }else{
      return false;
    }
  }
  