function correctness(bobsDecisions, expertDecisions) {
    let score = 0;
   for (let i = 0; i < bobsDecisions.length;i++){
     if (bobsDecisions[i] == expertDecisions[i]){
       score += 1;
     }else if (((bobsDecisions[i] == 'M' || bobsDecisions[i] == 'F')&& expertDecisions[i] == '?')|| 
       ((bobsDecisions[i] == '?')&&(expertDecisions[i] == 'M' || expertDecisions[i] == 'F'))){
       score += 0.5;
     }else{
       score += 0;
     }
   }
   return score;
 }