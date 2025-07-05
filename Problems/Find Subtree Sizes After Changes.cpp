class Solution {
public:
    vector<pair<int, int>> change;
    vector<int> adj[100000]; 
    
    void dfs(int node, int original, vector<int>& parent, string& s) { 
        if (s[original] == s[node]){
            change.push_back({original, node}); //node is the new parent of orginal
            return;
        }
    
        if (node == 0) return;
    
        dfs(parent[node], original, parent, s);
    }
    
    void countChildren(int i, vector<int>& ans) { 
        for (auto child : adj[i]) {
            countChildren(child, ans);
            ans[i] += ans[child];
        }
    }
    
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<int> res(n, 1);
    
        for (int i = 1; i < n; i++) {
            dfs(parent[i], i, parent, s);
        }
    
        for (auto itr : change) parent[itr.first] = itr.second;
    
        for (int i = 1; i < n; i++){
            adj[parent[i]].push_back(i);
        }
        
        countChildren(0, res);
        
        return res;
    }
};
