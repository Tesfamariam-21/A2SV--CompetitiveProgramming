
from collections import Counter
def solve(shoe_sizes, number_customer):
    
    # we need counter
    counter = Counter(shoe_sizes)
    total_prices = 0
    
    for _ in range(number_customers):
        shoe_size, price = map(int, input().split())
        available = counter.get(shoe_size, 0)
        if available > 0:
            total_prices += price
            counter[shoe_size] -= 1
            
    return total_prices
        
    
if __name__=="__main__":
    n_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    number_customers = int(input())
    
    answer = solve(shoe_sizes, number_customers)
    print(answer)
