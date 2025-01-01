function shoot(x){
    let peteScore = 0;
    let philScore = 0;
      for (let  i = 0; i < x.length; i++){
       let first = x[i][0]; // change first 0 to i
       let second = x[i][1];
       let pete = first.P1.split('');
       let phil = first.P2.split('');
       if (pete[0] == 'X'&& second == true){
         peteScore += 2;
       }else if (pete[0] == 'X' && second == false){
         peteScore += 1
       }
      if (pete[1] == 'X'&& second == true){
        peteScore += 2;
      }else if (pete[1] == 'X' && second == false){
         peteScore += 1
       }
        if (phil[0] == 'X'&& second == true){
         philScore += 2;
       }else if (phil[0] == 'X' && second == false){
         philScore += 1
       }
      if (phil[1] == 'X' && second == true){
        philScore += 2;
      }else if (phil[1] == 'X' && second == false){
        philScore += 1
      }
      }    
   if (philScore > peteScore){
     return 'Phil Wins!';
   }else if (peteScore > philScore){
     return 'Pete Wins!';
   }else{
     return 'Draw!';
   }  
  }
  