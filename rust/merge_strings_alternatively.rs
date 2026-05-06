use std::cmp;

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let max_len = cmp::max(word1.len(), word2.len());
        let mut res = String::new();
        for i in 0..max_len{
            res.push(word1.chars().nth(i).unwrap_or_default());
            res.push(word2.chars().nth(i).unwrap_or_default());
        }
        res = res.replace('\u{0}', "");
        return res;
    }
}