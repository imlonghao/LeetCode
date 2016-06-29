class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and ans[left] not in vowels:
                left += 1
            while left < right and ans[right] not in vowels:
                right -= 1
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)


print Solution().reverseVowels(".,")
