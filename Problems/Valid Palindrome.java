class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            while (left < right && !alphaNum(s.charAt(left))) { // move left and right until alphanumeric
                left++;
            }
            while (right > left && !alphaNum(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) { // convert to lowercase and cehck to be equal
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z' || c >= '0' && c <= '9'); // check char values are within digits and letters
    }
}
