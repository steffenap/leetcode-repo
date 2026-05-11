class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_s = set(nums1)
        nums2_s = set(nums2)
        ans = [[], []]
        ans[0] = list(nums1_s - nums2_s)
        ans[1] = list(nums2_s - nums1_s)
        return ans