class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_prof = 0
        max_prof = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_prof = prices[j] - prices[i]
                if curr_prof > max_prof:
                    max_prof = curr_prof
        return max_prof
