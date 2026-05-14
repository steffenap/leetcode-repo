import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return bool(re.search(".*".join([x for x in s]),t))
