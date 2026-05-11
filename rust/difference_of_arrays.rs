use std::collections::HashSet;
impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let mut num1 = HashSet::<i32>::new();
        let mut num2 = HashSet::<i32>::new();
        let mut ans: Vec<Vec<i32>> = Vec::new();
        for elem in nums1 {
            num1.insert(elem);
        }
        for elem in nums2 {
            num2.insert(elem);
        }
        let diff1: Vec<i32> = num1.difference(&num2).cloned().collect();
        let diff2: Vec<i32> = num2.difference(&num1).cloned().collect();
        ans.push(diff1);
        ans.push(diff2);
        return ans
    }
}