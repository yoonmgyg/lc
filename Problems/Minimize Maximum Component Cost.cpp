class Solution {
public:
  int find(int i, vector<int> &ds) {
      return ds[i] < 0 ? i : ds[i] = find(ds[i], ds);
  }
  int minCost(int n, vector<vector<int>>& edges, int k) {
      sort(begin(edges), end(edges), [](const auto &a, const auto& b){
          return a[2] < b[2];
      });
      vector<int> ds(n, -1);
      int cost = 0;
      for (const auto &e : edges) {
          if (n == k)
              break;
          auto i = find(e[0], ds), j = find(e[1], ds);
          if (i != j) {
              --n;
              ds[i] += ds[j];
              ds[j] = i;
              cost = e[2];
          }
      }
      return cost;
  }
};
