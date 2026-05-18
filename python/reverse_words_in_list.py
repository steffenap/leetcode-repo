import re
class Solution:
    def reverseWords(self, s: str) -> str:
        p = '[a-zA-Z0-9]+'
        l = re.findall(p, s)
        ans = []
        for item in l[-1::-1]:
            ans.append(item)
        return ' '.join(ans)