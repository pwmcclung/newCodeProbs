function createSSP(password){
 let passwordSplit = password.split('');
 let newPass = [];
  for (let i = 0; i < passwordSplit.length; i++){
    if (passwordSplit[i] == 'a' || passwordSplit[i] == 'A'){
      newPass.push('@');
    }else if (passwordSplit[i] == 's' || passwordSplit[i] == 'S'){
      newPass.push('$');
    }else if (passwordSplit[i] == 'o' || passwordSplit[i] == 'O'){
      newPass.push('0');
    }else if (passwordSplit[i] == 'h' || passwordSplit[i] == 'H'){
      newPass.push('5');
    }else if (passwordSplit[i] == 'x' || passwordSplit[i] == 'X'){
      newPass.push('*');
    }else{
      newPass.push(passwordSplit[i]);
    }
  }
  return newPass.join('');
}