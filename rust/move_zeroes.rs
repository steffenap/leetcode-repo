impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let original: usize = nums.len();
        nums.retain(|&x| x != 0);
        let removed: usize = nums.len();
        let diff: usize = original - removed;
        for i in 0..diff{
            nums.push(0);
        } 
    }
}