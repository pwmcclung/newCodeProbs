function hexWordSum( string ){
 let words = string.split(" ");
  let sum = 0;

  for (let word of words) {
    let hexWord = "";
    for (let char of word) {
      if (char === 'O') {
        hexWord += '0';
      } else if (char === 'S') {
        hexWord += '5';
      } else if (/[0-9A-F]/.test(char)) {
        hexWord += char;
      } else {
        hexWord = ""; 
        break;
      }
    }

    if (hexWord !== "") {
      try {
        let decimalValue = parseInt(hexWord, 16);
        if(!isNaN(decimalValue)){
            sum += decimalValue;
        }
        
      } catch (error) {
        
      }
    }
  }

  return sum;
}