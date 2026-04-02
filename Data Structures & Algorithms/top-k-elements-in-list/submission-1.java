class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            if (map.get(n) == null) {
                map.put(n,0);
            }
            map.put(n, map.get(n) + 1);
        }

        HashMap<Integer, List<Integer>> freqs = new HashMap<>();
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            if (freqs.get(count) == null) {
                freqs.put(count, new ArrayList<Integer>());
            }
            freqs.get(count).add(num);
        }

        int[] ans = new int[k];
        int iter = 0;
        for (int i = nums.length; i > 0; i--) {
            if (freqs.get(i) != null) {
                for (int num : freqs.get(i)) {
                    ans[iter] = num;
                    iter++;
                }
            }
            if (iter == k) return ans;
        }
        return ans;
    }
}
