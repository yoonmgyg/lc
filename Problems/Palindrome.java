
public class Palindrome {
    public boolean pal(String str){
        for (int i = 0; i < str.length() / 2; ++i) { // loop through first half
            if (str.charAt(i) != str.charAt(str.length() - i - 1)) { // compare i with length - i
                return false;
            }
        }
        return true;
    }
}
