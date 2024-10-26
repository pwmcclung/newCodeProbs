function twentyOne(card1, card2, card3) {
    let score = cardCount(card1) + cardCount(card2) + cardCount(card3);
     if (score < 21){
       return 'less';
     }else if (score > 21){
       return 'more';
     }else{
       return 'twenty-one';
     }
   }
   
   function cardCount(card){
     let score = 0;
     if (card.includes('A')){
       score = 11;
     }else if ( card.includes('K')){
       score = 4;
     }else if (card.includes('Q')){
       score = 3;
     }else if (card.includes('J')){
       score = 2;
     }else{
       score = parseInt(card);
     }
     return score;
   }