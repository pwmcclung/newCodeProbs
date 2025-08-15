function anArgument(...args) {
if (args.length == 0){
  return "You didn't give me any arguments.";
}else if (args.length == 1){
  let word = `"${args[0]}"`
  return `You gave me 1 argument and it is ${word}.`;
}else{
  let newStr = '';
  for (let i = 0; i < args.length-1;i++){
    let word = '';
    if (i !== args.length-2){
      word = `"${args[i]}", `;
    }else{
     word = `"${args[i]}"`; 
    }
    newStr += word;
  }
  let secondPart = `"${args[args.length-1]}"`;
  return `You gave me ${args.length} arguments and they are ${newStr} and ${secondPart}.`;
}
}