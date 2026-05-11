from itertools import groupby
from math import ceil
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [list(group) for is_delim, group in itertools.groupby(flowerbed, lambda x: x == 1) if not is_delim]
        ctr = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                ctr += 1
            return ctr >= n
        if 1 not in set(flowerbed):
            ctr += ceil(len(flowerbed) / 2)
            return ctr >= n
        if bed:
            if flowerbed[0] == 0:
                if len(bed[0]) - 1 > 0:
                    ctr += ceil((len(bed[0]) - 1) / 2)
            else:
                if (len(bed[0]) - 2) > 0 and len(bed) > 1:
                    ctr += ceil((len(bed[0]) - 2) / 2)
            for b in bed[1:-1]:
                if (len(b) - 2) > 0:
                    ctr += ceil((len(b) - 2) / 2)
            if (len(bed) > 1 or ctr == 0):
                if flowerbed[-1] == 0:
                    if (len(bed[-1]) - 1) > 0:
                        ctr += ceil(((len(bed[-1]) - 1)) / 2)
                else:
                    if (len(bed[-1]) - 2) > 0:
                        ctr += ceil((len(bed[-1]) - 2) / 2)
        if ctr >= n:
            return True
        return False