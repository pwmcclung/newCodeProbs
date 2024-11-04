function missingWord(nums, str) {
    let sortNums = nums.sort((a,b)=> a-b);
    str = str.toLowerCase().replace(/ /g,'');
    let first = str[sortNums[0]];
    let second = str[sortNums[1]];
    let third = str[sortNums[2]];
    if (nums[2] > str.length){
      return 'No mission today';
    }else{
      return first+second+third;
    }
  }