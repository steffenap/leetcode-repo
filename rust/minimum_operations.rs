impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let n_boxes = boxes.len();
        let b: Vec<i32> = boxes.bytes().map(|c| (c - b'0') as i32).collect();
        let mut res = vec![0; n_boxes];

        res = Self::pass(n_boxes, &b, res, false);
        res = Self::pass(n_boxes, &b, res, true);
        
        return res;
    }

    pub fn pass(x: usize, b: &[i32], res: Vec<i32>, rev: bool) -> Vec<i32> {
        let mut res = res;
        let (mut ball, mut cost) = (0,0);
        if rev{
            for i in (0..x).rev() {
                res[i] += cost;
                ball += b[i];
                cost += ball; 
            }
        }
        else {
            for i in 0..x {
                res[i] += cost;
                ball += b[i];
                cost += ball; 
            }
        }
        return res;
    }
}