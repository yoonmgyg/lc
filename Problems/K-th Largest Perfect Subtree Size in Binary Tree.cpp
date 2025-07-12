class Solution {
public:
    int dfs(TreeNode* node, vector<int>& ans) {
        if (!node) return 0;
        
        int left = dfs(node->left, ans);
        int right = dfs(node->right, ans);
        
        if (left != right) return -1;
        
        ans.push_back(left + right + 1);
        return left + right + 1;
    }
    
    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        vector<int> ans;
        dfs(root, ans);
        
        if (ans.size() < k) return -1;
        
        nth_element(ans.begin(), ans.end() - k, ans.end());
        return ans[ans.size() - k];
    }
};
