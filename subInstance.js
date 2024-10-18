function solution(fullText, searchText){
    let fullSplit = fullText.split(searchText);
    return fullSplit.length - 1;
  }