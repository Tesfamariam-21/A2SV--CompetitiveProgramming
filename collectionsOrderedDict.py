# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__=="__main__":
    _item = {}
    n = int(input())
    
    for i in range(n):
        goods = input().split()
        price = int(goods[len(goods)-1])
        goods.pop()
        goods= " ".join(goods)
        _item[goods] = _item.get(goods, 0)+ price
     
    for key, value in _item.items():
        print(key, value)
        
