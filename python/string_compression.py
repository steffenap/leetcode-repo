class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        curr = None
        ctr = 0
        for c in chars:
            if not curr:
                curr = c
                ctr = 1
            else:
                if curr != c:
                    res.append(curr)
                    if ctr != 1:
                        for cc in str(ctr):
                            res.append(cc)
                    curr = c
                    ctr = 1
                else:
                    ctr += 1
        res.append(curr)
        if ctr != 1:
            for cc in str(ctr):
                res.append(cc)
        print(res)
        chars.clear()
        for elem in res:
            chars.append(elem)
        return len(chars)