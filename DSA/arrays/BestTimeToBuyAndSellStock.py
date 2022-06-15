'''
Idea here is to loop through the list and check if the next val is less than the curr.
if it is then you set a new sell price, if it's greater then you check to see if 
the difference gives you a better profit.


'''
import sys

def maxProfit(self, prices: List[int]) -> int:
    min_price = sys.maxsize
    profit = 0
    
    for i in range(0, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif (prices[i] - min_price > profit):
            profit = prices[i] - min_price
            
    return profit