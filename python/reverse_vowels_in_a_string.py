class Solution:
    def reverseVowels(self, s: str) -> str:
        pat = {'a','e','i','o','u','A','E','I','O','U'}
        idx = []
        c = []
        strlst = list(s)
        for i, char in enumerate(strlst):
            if char in pat:
                print('hello')
                idx.append(i)
                c.append(char)
        c.reverse()
        print(c)
        for i, elem in enumerate(c):
            strlst[idx[i]] = elem
        return "".join(strlst)