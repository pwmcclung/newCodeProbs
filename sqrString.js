function vertMirror(strng) {
    return strng.split('\n').map(line => line.split('').reverse().join('')).join('\n');
  }
  
  function horMirror(strng) {
    return strng.split('\n').reverse().join('\n');
  }
  
  function oper(fct, s) {
    return fct(s);
  }