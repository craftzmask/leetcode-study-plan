class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def pos(c):
            return ord(c) - ord('a')

        if len(p) > len(s):
            return []

        p_count = [0] * 26
        for c in p:
            p_count[pos(c)] += 1
        
        window = [0] * 26
        for i in range(len(p)):
            window[pos(s[i])] += 1
        
        ans = []
        if window == p_count:
            ans += [0]
        
        for i in range(len(p), len(s)):
            window[pos(s[i - len(p)])] -= 1
            window[pos(s[i])] += 1
            if window == p_count:
                print(i, len(p))
                ans += [i - len(p) + 1]

        return ans