class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] indeg = new int[numCourses];
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());

        // build graph and indegrees
        for (int[] p : prerequisites) {
            int a = p[0], b = p[1];
            graph.get(b).add(a); // b -> a
            indeg[a]++;
        }

        // seed queue with zero indegree
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) if (indeg[i] == 0) q.add(i);

        int taken = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            taken++; // take this course
            for (int v : graph.get(u)) {
                if (--indeg[v] == 0) q.add(v); // unlock next course
            }
        }

        return taken == numCourses; // all courses taken means no cycle
    }
}
