class Solution:
    def isFascinating(self, num):
        two_times_num = 2 * num
        three_times_num = 3 * num

        nums_concatenation = str(num) + str(two_times_num) + str(three_times_num)
        digit_to_freq_map = defaultdict(int)
        for d in nums_concatenation:
            digit_to_freq_map[d] += 1
            if (digit_to_freq_map[d] > 1):
                return False

        return len(set(range(1, 9 + 1)).difference(set([int(d) for d in list(nums_concatenation)]))) == 0
