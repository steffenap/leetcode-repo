use regex::Regex;
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let tokens: Vec<_> = s.chars().map(|c| c.to_string()).collect();
        let pattern = tokens.join(".*");
        let re = Regex::new(&pattern).unwrap();
        return re.is_match(&t);
    }
}