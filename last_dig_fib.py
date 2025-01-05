def get_last_digit(index):
     if index <= 0:
        return 0  
     a, b = 0, 1
     for _ in range(index):
         a, b = b, (a + b) % 10
     return a