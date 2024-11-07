function perc (mins) {
    let ttlBeats = mins * 120;
    let ttl4BeatBars = ttlBeats / 4;
    let claps = ttl4BeatBars * 2;
    let kicks = ttl4BeatBars * 4;
    let hiHats = ttl4BeatBars * 8;
    if ( mins < 1 || mins > 100 || typeof(mins) != 'number'){
      return 'invalid track time';
    }else{
      return [`${Math.round(kicks)} kicks`, `${Math.round(hiHats)} hihats`, `${Math.round(claps)} claps`];
    }
  };