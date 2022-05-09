# EASY
# You are given an array prices where prices[i] is the price of a given stock on the i'th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

prices = [6,1,4,3,5,4]
def maxProfit(prices):
    l , r = 0 , 1
    maxProfit = 0
    while r < len(prices):
        if(prices[r] < prices[l]):
            l = r
            r += 1
        else:
            maxProfit = max(prices[r]-prices[l], maxProfit)
            r += 1
    return maxProfit


def maxProfit2(prices):
    left , right = 0 , 1
    maxProfit = 0
    for right in range (1 , len(prices)):
        maxProfit = max(prices[right] - prices[left], maxProfit)
        if prices[left] > prices[right]:
            left = right
            right += 1
    return maxProfit

# print(maxProfit(prices))
# print(maxProfit2(prices))

