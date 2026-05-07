impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        let lhs = str1.to_owned() + &str2.to_owned();
        let rhs = str2.to_owned() + &str1.to_owned();
        if lhs != rhs {
            return "".to_string();
        }
        let idx = Self::gcd(str1.len() as i32, str2.len() as i32);
        return str1[..idx as usize].to_string();
    }

    pub fn gcd(mut x: i32, mut y: i32) -> i32 {
        while y != 0 {
            let mut temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }
}