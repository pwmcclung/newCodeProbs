function validPass(password) {
  
    if (password.length <= 3 || password.length >= 20) {
      return "INVALID";
    }
  
  
    if (!/^[a-zA-Z0-9]+$/.test(password)) {
      return "INVALID";
    }
  
    
    if (!/[a-zA-Z]/.test(password) || !/[0-9]/.test(password)) {
      return "INVALID";
    }
}