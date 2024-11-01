function giveChange(amount) {
    let ones = 0;
    let fives = 0;
    let tens = 0;
    let twenties = 0;
    let fifties = 0;
    let hundos = 0;
    
    let newAmt = amount;
    
    while (newAmt >0){
      
      if (newAmt > 99){
        while (newAmt > 99){
          hundos += 1;
          newAmt -= 100;
        }
      }else if (newAmt < 100 && newAmt > 49){
        while (newAmt < 100 && newAmt > 49){
          fifties += 1;
          newAmt -= 50;
        }
      }else if (newAmt < 50 && newAmt > 19){
        while (newAmt < 50 && newAmt > 19){
          twenties += 1;
          newAmt -= 20;
        }
      }else if( newAmt < 20 && newAmt > 9){
        while (newAmt < 20 && newAmt > 9){
          tens += 1;
          newAmt -= 10;
        }
      }else if (newAmt > 4 && newAmt < 10){
        while (newAmt > 4 && newAmt < 10){
          fives += 1;
          newAmt -= 5;
        }
          }else if (newAmt >0 && newAmt < 10){
          while (newAmt >0 && newAmt < 10){
            ones+=1;
          newAmt -= 1;
        }
      }
    }
    
    
    return [ones,fives, tens, twenties, fifties, hundos];
  }