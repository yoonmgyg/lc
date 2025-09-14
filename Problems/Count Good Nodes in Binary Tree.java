class Solution {
    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);
    }

    private int dfs(TreeNode root, int parent) {
        if (root == null) {
            return 0;
        }
        int good = root.val >= parent ? 1 : 0;
        parent = Math.max(parent, root.val);
        return dfs(root.left, parent) + dfs(root.right, parent) + good;
    }
}
