from heapq import nlargest
def top3(products, amounts, prices):
    dictionary = {pro: a*p for pro,a,p in zip(products, amounts, prices)}
    larg3 = nlargest(3,dictionary, dictionary.get)
    return larg3