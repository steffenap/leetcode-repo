impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
     let mut curr = 0;
     let mut mx = 0;   
     for elem in gain {
        curr += &elem;
        mx = std::cmp::max(mx, curr);
     }
     return mx;
    }
}