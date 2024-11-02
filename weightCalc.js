function liftingCalc(w){
    if (w < 20 || w % 1.25 != 0){
      return false;
    }
   if (w == 20){
     return [];
   }
     let newArr = [];
     let weightNeeded = (w - 20)/2;
     while (weightNeeded != 0){
       if (weightNeeded > 19){
         while(weightNeeded > 19){
           newArr.push(20);
           weightNeeded -= 20;
         }
       }if (weightNeeded > 14){
         while(weightNeeded > 14){
           newArr.push(15);
           weightNeeded -= 15;
         }
       }if (weightNeeded > 9){
         while(weightNeeded > 9){
           newArr.push(10);
           weightNeeded -= 10;
         }
       }if (weightNeeded > 4){
         while(weightNeeded > 4){
           newArr.push(5);
           weightNeeded -= 5;
         }
       }if (weightNeeded > 2.49){
         while(weightNeeded > 2.49){
           newArr.push(2.5);
           weightNeeded -= 2.5;
         }
       }if (weightNeeded > 1.24){
         while(weightNeeded > 1.24){
           newArr.push(1.25);
           weightNeeded -= 1.25;
         }
       }
     }
     return newArr;
   }