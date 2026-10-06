class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,0

        max_profit=float('-inf')

        while j<len(prices):
            max_profit=max(max_profit, prices[j]-prices[i])

            if prices[j]>=prices[i]:
                j+=1

            else:
                i+=1

        return max_profit