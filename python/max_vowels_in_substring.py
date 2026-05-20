class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        p = {'a','e','i','o','u','A','E','I','O','U'}
        ptr_s = 0
        ptr_e = k
        ctr = 0
        for c in s[:ptr_e]:
            ctr += c in p
        mx = ctr
        while ptr_e < len(s):
            ctr -= s[ptr_s] in p
            ctr += s[ptr_e] in p
            ptr_s += 1
            ptr_e += 1
            mx = max(ctr, mx)
        return mx
