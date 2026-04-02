class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int lowest = prices[0];

        for (int p : prices) {
            lowest = Math.min(lowest, p);
            res = Math.max(res, p - lowest);
        }
        return res;
    }
}
