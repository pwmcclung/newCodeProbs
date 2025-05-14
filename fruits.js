function cutFruits(fruits){
    let newArr = [];
    for (let i = 0; i <fruits.length; i++){
      if (fruitsName.includes(fruits[i])){
        let len = fruits[i].length;
        if(len % 2 !=0){
          let first = fruits[i].slice(0, Math.ceil(len /2));
          let second = fruits[i].slice(Math.ceil(len/2),);
          newArr.push(first);
          newArr.push(second);
        }else if (len % 2 == 0){
          let third = fruits[i].slice(0, len/2);
          let fourth = fruits[i].slice(len/2,);
          newArr.push(third);
          newArr.push(fourth);
        }
      }else{
        newArr.push(fruits[i])
  }
    }
    return newArr;
  }