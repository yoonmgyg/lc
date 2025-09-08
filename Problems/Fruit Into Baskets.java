class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> state = new HashMap<>();
        int res = 0;

        int l = 0;
        int r = 0;
        while (r < fruits.length) {
            if (state.size() < 2 || state.containsKey(fruits[r])) {
                state.merge(fruits[r], 1, Integer::sum);
                ++r;
                res = Math.max(res, r-l);
            } else {
                int decremented = state.get(fruits[l]) - 1;
                if (decremented == 0) {
                    state.remove(fruits[l]);
                } else {
                    state.put(fruits[l], decremented);
                }
                ++l;
            }   
        }

        return res;
    }
}
