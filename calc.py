def calc(expression):
    tokens = tokenize(expression)
    return parse_expression(tokens)

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '.': 
            num_str = ""
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            tokens.append(float(num_str))
        elif expression[i] in ['+', '-', '*', '/', '(', ')']:  
            tokens.append(expression[i])
            i += 1
        else:  
            i += 1
    return tokens

def parse_expression(tokens):
    left = parse_term(tokens)
    while tokens and tokens[0] in ['+', '-']:
        operator = tokens.pop(0)
        right = parse_term(tokens)
        left = left + right if operator == '+' else left - right
    return left

def parse_term(tokens):
    left = parse_factor(tokens)
    while tokens and tokens[0] in ['*', '/']:
        operator = tokens.pop(0)
        right = parse_factor(tokens)
        left = left * right if operator == '*' else left / right
    return left

def parse_factor(tokens):
    if tokens[0] == '(':
        tokens.pop(0)  
        result = parse_expression(tokens)
        if tokens.pop(0) != ')':
            raise ValueError("Mismatched parentheses")
        return result
    elif tokens[0] == '-':
        tokens.pop(0)
        return -parse_factor(tokens)
    else:
        return tokens.pop(0)