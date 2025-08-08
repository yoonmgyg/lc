class Solution {
    public boolean isAnagram(String s, String t) {
        // check lengths are equal
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> charS = new HashMap<>();
        HashMap<Character, Integer> charT = new HashMap<>();

        // add both chars to map
        for (int i = 0; i < s.length(); ++i) {
            charS.put(s.charAt(i), charS.getOrDefault(s.charAt(i), 0) + 1);
            charT.put(t.charAt(i), charT.getOrDefault(t.charAt(i), 0) + 1);
        }

        // compare if maps are the same
        return charS.equals(charT);
    }
}
