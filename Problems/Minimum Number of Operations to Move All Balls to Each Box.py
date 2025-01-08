# Loop through box using greedy algorithm to determine ones before index to choose which box
class Solution:
  def minOperations(self, boxes: str) -> List[int]:
      n = len(boxes)
      boxes = [int(i) for i in boxes]
      pre = [[0,0] for i in range(n)]
      post= [[0,0] for i in range(n)]
      
      for i in range(1, n):
          pre[i][0] = boxes[i-1] + pre[i-1][0]
          pre[i][1] = boxes[i-1] + pre[i-1][0] + pre[i-1][1]
      
      for i in range(n-2, -1, -1):
          post[i][0] = boxes[i+1] + post[i+1][0]
          post[i][1] = boxes[i+1] + post[i+1][0] + post[i+1][1]
      
      for i in range(n):
          boxes[i] = pre[i][1]+post[i][1]
      
      return boxes
