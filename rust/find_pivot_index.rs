impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let mut right_ptr: i32 = nums.iter().sum();
        let mut left_ptr = 0;
        for (i, elem) in nums.iter().enumerate() {
            right_ptr -= elem;
            if left_ptr == right_ptr {
                return i as i32;
            }
            left_ptr += elem;
        }
        return -1;
    }
}