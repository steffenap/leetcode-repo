from math import floor
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ctr = 0
        res = []
        curr = head
        while curr:
            ctr += 1
            curr = curr.next
        length = floor(ctr/2)
        curr = head
        for i in range(length):
            curr = curr.next
        return curr