class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        right_ptr = tot
        left_ptr = 0
        for i, elem in enumerate(nums):
            right_ptr -= elem
            if left_ptr == right_ptr:
                return i
            left_ptr += elem
        return -1