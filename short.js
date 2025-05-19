var shortenSpeech = function (str) {	
  const VOWELS = "aeiou";
  function processToken(token) {
    const originalToken = token;
    let endsWithComma = false;
    let wordToProcess = token;
    if (token.length > 0 && token.endsWith(',')) {
      endsWithComma = true;
      wordToProcess = token.substring(0, token.length - 1);
    }
    if (wordToProcess.length === 0) {
        return originalToken;
    }
    if (wordToProcess.length < 4) {
      return originalToken;
    }
    let vowelIndexInWord = -1;
    for (let i = 3; i < wordToProcess.length; i++) {
      const char = wordToProcess.charAt(i);
      if (VOWELS.includes(char.toLowerCase())) {
        vowelIndexInWord = i;
        break;
      }
    }
    if (vowelIndexInWord !== -1) {
      const shortenedCore = wordToProcess.substring(0, vowelIndexInWord);
      return shortenedCore + ".";
    } else {
      return originalToken;
    }
  }
  const parts = str.split(' ');
  const processedParts = parts.map(token => processToken(token));
  return processedParts.join(' ');
};
