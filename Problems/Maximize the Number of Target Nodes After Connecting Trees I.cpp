vector<vector<int>> buildList(const vector<vector<int>>& edges) {
    int N = edges.size()+1;
    vector<vector<int>> adj(N);
    for (auto &e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    return adj;
}
