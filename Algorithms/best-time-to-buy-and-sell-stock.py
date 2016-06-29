class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        ans = 0
        left = prices[0]
        right = 0
        for price in prices:
            if price < left:
                left = price
                right = 0
                continue
            right = max(right, price)
            ans = max(right - left, ans)
        return ans
