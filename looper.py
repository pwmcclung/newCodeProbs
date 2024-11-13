import numpy as np
def looper(start, stop, number):
    arr = np.linspace(start, stop, number)
    return [x for x in arr]