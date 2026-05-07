impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let (first, second) = Self::find_largest(&candies);
        let mut ans = vec![false; candies.len()];
        for (idx, &elem) in candies.iter().enumerate() {
            if idx == first.1 {
                if elem + extra_candies >= second.0 {
                    ans[idx] = true;
                }
            }
            else {
                if elem + extra_candies >= first.0 {
                    ans[idx] = true;
                }
            }
        }
        return ans;
    }
    pub fn find_largest(candies: &Vec<i32>) -> ((i32, usize), (i32, usize)) {
        let mut first = (i32::MIN, 0);
        let mut second = (i32::MIN, 0);

        for (idx, &elem) in candies.iter().enumerate(){
            if elem > first.0 {
                second = first;
                first = (elem, idx);
            }
            else if elem > second.0 {
                second = (elem, idx);
            }
        }
        return (first, second);
    }
}