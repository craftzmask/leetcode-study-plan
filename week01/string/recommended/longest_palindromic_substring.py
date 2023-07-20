class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            start, end = 0, 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l, r = l - 1, r + 1
            return s[start:end+1]

        ans = ""
        for i in range(len(s)):
            # check odd length of a substr
            odd_sub = expand(i, i)
            if len(odd_sub) > len(ans):
                ans = odd_sub
            
            # check even length of substr
            even_sub = expand(i, i + 1)
            if len(even_sub) > len(ans):
                ans = even_sub

        return ans