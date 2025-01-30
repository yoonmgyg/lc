# Add ranks onto map and add acording to index
class Solution(object):
    def findRelativeRanks(self, score):
        score_map = {score[i]: i for i in range(len(score))}

        score.sort(reverse=True)
        result = ["" for _ in range(len(score))]
        for i in range(len(score)):
            if i == 0:
                result[score_map[score[i]]] = "Gold Medal"
            elif i == 1:
                result[score_map[score[i]]] = "Silver Medal"
            elif i == 2:
                result[score_map[score[i]]] = "Bronze Medal"
            else:
                result[score_map[score[i]]] = str(i + 1)

        return result
