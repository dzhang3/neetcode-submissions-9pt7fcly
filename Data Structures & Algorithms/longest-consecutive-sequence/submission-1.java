class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int n : nums) {
            numSet.add(n);
        }

        int longest = 0;
        for (Integer n : numSet) {
            if (!numSet.contains(n-1)) {
                int length = 1;
                for (;numSet.contains(n + length); length++);
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
