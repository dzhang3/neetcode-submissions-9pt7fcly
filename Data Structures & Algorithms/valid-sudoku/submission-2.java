class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> sqrs = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                char n = board[r][c];

                if (rows.getOrDefault(r, new HashSet<>()).contains(n)
                        || cols.getOrDefault(c, new HashSet<>()).contains(n)
                        || sqrs.getOrDefault((r / 3) * 3 + c / 3, new HashSet<>()).contains(n)) {
                    return false;
                }
                cols.computeIfAbsent(c, k -> new HashSet<>()).add(n);
                rows.computeIfAbsent(r, k -> new HashSet<>()).add(n);
                sqrs.computeIfAbsent((r / 3) * 3 + c / 3, k -> new HashSet<>()).add(n);
            }
        }
        return true;
    }
}
