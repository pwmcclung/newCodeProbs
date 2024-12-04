function winnerOfTrick( cards, players ){
    let lenCards = cards.length;
    let lenPlayers = players.length;
    if (lenPlayers > lenCards){
      players = players.slice(0,lenCards);
    }
    let scoresDict = {'AH':14, 'AC':14, 'AD':14, 'AS':14, 'KH':13, 'KC':13, 'KD':13, 'KS':13, 
                     'QH':12, 'QC':12, 'QD':12, 'QS':12,'JH':11, 'JC':11, 'JD':11, 'JS':11,'TH':10, 'TC':10, 'TD':10, 'TS':10,
                     '9H':9, '9C':9, '9D':9, '9S':9,'8H':8, '8C':8, '8D':8, '8S':8,'7H':7, '7C':7, '7D':7, '7S':7,
                     '6H':6, '6C':6, '6D':6, '6S':6,'5H':5, '5C':5, '5D':5, '5S':5,'4H':4, '4C':4, '4D':4, '4S':4,
                     '3H':3, '3C':3, '3D':3, '3S':3,'2H':2, '2C':2, '2D':2, '2S':2}
    let scoresArr = cards.map((x)=>scoresDict[x]);
    let maxScores = Math.max(...scoresArr);
    const matchingIndexes = scoresArr.reduce((acc, value, index) => {
    if (value === maxScores) {
      acc.push(index);
    }
    return acc;
  }, []);
    let names = [];
    if (matchingIndexes.length < 2){
      return `${players[matchingIndexes]} wins`;
    }else{
      let names = [];
      while (matchingIndexes.length > 0){
        let first = matchingIndexes.shift();
        names.push(players[first]);
      }
      return `Tie! (${names})`;
    }
  }