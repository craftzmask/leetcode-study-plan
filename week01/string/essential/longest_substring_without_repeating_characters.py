class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        l, longest = 0, 0
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            unique_chars.add(s[r])
            longest = max(longest, len(unique_chars))
        return longest