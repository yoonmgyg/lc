class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        max_length = 0
        path_lengths = {0: 0}  # depth: length

        for line in lines:
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            is_file = '.' in name

            if is_file:
                max_length = max(max_length, path_lengths[depth] + len(name))
            else:
                path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1  # 1 for the '/'
        
        return max_length
