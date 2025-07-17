class Solution {
public:
    int minimumOperationsToWriteY(vector<vector<int>>& grid) {
        int n = grid.size(),n1=0,n2=0;
        map<int,int> m1,m2;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (((i == j || j == n-1-i) && i <= (n-1)/2) || (j == (n-1)/2 && i > (n-1)/2)){
                    m1[grid[i][j]]++;
                    n1++;
                } else {
                    //non-Y elements
                    m2[grid[i][j]]++;
                    n2++;
                }
            }
        }
        int ans1 = n1-m1[0]+min(n2-m2[1],n2-m2[2]); // if all Y elements are 0
        int ans2 = n1-m1[1]+min(n2-m2[0],n2-m2[2]); // if all Y elements are 1
        int ans3 = n1-m1[2]+min(n2-m2[1],n2-m2[0]); // if all Y elements are 2
        int ans = min({ans1,ans2,ans3});
        return ans;
    }
};
