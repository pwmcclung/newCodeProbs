function calc(expression) {
    let tokens = tokenize(expression);
    return parseExpression(tokens);
  }
  
  function tokenize(expression) {
    const tokens = [];
    let i = 0;
    while (i < expression.length) {
      if (expression[i].match(/[0-9.]+/)) { //Number
        let numStr = "";
        while (i < expression.length && expression[i].match(/[0-9.]/)) {
          numStr += expression[i];
          i++;
        }
        tokens.push(parseFloat(numStr));
      } else if (expression[i].match(/[-+*/()]/)) { //Operator or parenthesis
        tokens.push(expression[i]);
        i++;
      } else { //Whitespace
        i++;
      }
    }
    return tokens;
  }
  
  
  function parseExpression(tokens) {
    let left = parseTerm(tokens);
    while (tokens.length > 0 && (tokens[0] === '+' || tokens[0] === '-')) {
      const operator = tokens.shift();
      const right = parseTerm(tokens);
      left = operator === '+' ? left + right : left - right;
    }
    return left;
  }
  
  function parseTerm(tokens) {
    let left = parseFactor(tokens);
    while (tokens.length > 0 && (tokens[0] === '*' || tokens[0] === '/')) {
      const operator = tokens.shift();
      const right = parseFactor(tokens);
      left = operator === '*' ? left * right : left / right;
    }
    return left;
  }
  
  function parseFactor(tokens) {
    if (tokens[0] === '(') {
      tokens.shift(); //Consume '('
      const result = parseExpression(tokens);
      if (tokens.shift() !== ')') {
        throw new Error("Mismatched parentheses");
      }
      return result;
    } else if(tokens[0] === '-'){
      tokens.shift();
      return -parseFactor(tokens);
    } else {
      return tokens.shift();
    }
  }