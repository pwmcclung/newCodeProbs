function roomMates( rooms, floor ){
    let floorCalcBack = (floor * 6 ) - 1;
   let floorCalcFront = floorCalcBack - 5;
   const result = rooms.filter((room) => rooms.indexOf(room) >= floorCalcFront && rooms.indexOf(room) <= floorCalcBack );
   return result.filter((x) => x.length > 0);
   }