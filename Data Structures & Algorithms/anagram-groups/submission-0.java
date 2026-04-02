class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map = new HashMap<>();
        
        for (String str : strs){
            int[] count = new int[26];
            for (char c : str.toCharArray()) {
                count[c - 'a'] += 1;
            }
            String c = Arrays.toString(count);
            if (map.get(c) == null) map.put(c, new ArrayList<String>());
            map.get(c).add(str);
        }
        List<List<String>> ans = new ArrayList<>(map.values());
        return ans;
    }
}
