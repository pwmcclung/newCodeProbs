function ringBank(rings, monitors, giantrings, chaosEmeralds, sonicHit, sonicShield){
   let ringCount = 0;
   if (sonicHit == true && sonicShield == false){
     return 0;
   }else{
     if (chaosEmeralds >=7){
       ringCount = rings * 1 + monitors * 10 + giantrings * 50;
     }else{
       ringCount = rings * 1 + monitors * 10;
     }
   }
  return ringCount;
  }