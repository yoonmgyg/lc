class Solution:
    def string_score(s):
        score = 0  # initialize the score to zero
        for i in range(1, len(s)):  # iterate from the second character to the end
            score += abs(ord(s[i]) - ord(s[i - 1]))  # add the absolute difference of ASCII values between adjacent characters
        return score
