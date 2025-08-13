class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> window = new HashMap<>();
        for (char c : t.toCharArray()) { // get frequency of chars into map
            window.merge(c, 1, Integer::sum);
        }
        int left = 0;
        int right = 0;
        int counter = t.length();
        int minLength = Integer.MAX_VALUE;
        int minStart = 0;
        while (right < s.length()) { // move right pointer through string
            int rightVal = window.getOrDefault(s.charAt(right), 0);
            if (rightVal > 0) { // count missing characters and decrement frequency
                --counter;
            }
            window.put(s.charAt(right), rightVal - 1);
            ++right;

            while (counter == 0) { // when all characters are present, calculate length and move window's left pointer for smaller windows
                if (right - left < minLength) {
                    minStart = left;
                    minLength = right - left;
                }
                int leftVal = window.getOrDefault(s.charAt(left), 0);
                leftVal += 1;
                window.put(s.charAt(left), leftVal);

                if (leftVal > 0) {
                    ++counter;
                }
                ++left;

            }
        }
        if (minLength != Integer.MAX_VALUE) {
            return s.substring(minStart, minStart + minLength);
        }
        return "";
    }
}
