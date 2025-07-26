class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0); // 0 = unvisited, 1 = visiting, 2 = visited

        for (auto& pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
        }

        function<bool(int)> dfs = [&](int course) {
            if (visited[course] == 1) return false; // cycle detected
            if (visited[course] == 2) return true;

            visited[course] = 1;
            for (int next : graph[course]) {
                if (!dfs(next)) return false;
            }
            visited[course] = 2;
            return true;
        };

        for (int i = 0; i < numCourses; ++i) {
            if (!dfs(i)) return false;
        }
        return true;
    }
};
