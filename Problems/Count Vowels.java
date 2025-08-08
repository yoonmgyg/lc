public static List<Integer> countVowels(String word, int[][] queries) {
    int n = word.length();
    int[] prefix = new int[n + 1];
    Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');

    // Build prefix sum array
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + (vowels.contains(word.charAt(i)) ? 1 : 0);
    }

    // Answer queries
    List<Integer> result = new ArrayList<>();
    for (int[] q : queries) {
        int l = q[0], r = q[1];
        result.add(prefix[r + 1] - prefix[l]);
    }

    return result;
}
