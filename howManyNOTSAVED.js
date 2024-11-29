function shortestStepsToNum(num) {
    let steps = 0;
    let start = 1;
    while (start < num){
      if (num % 2 == 0 && num / 2 >= start){
        num /= 2;
        steps+=1;
      }else{
        num -= 1;
        steps += 1;
      }
    }
    return steps;
  }