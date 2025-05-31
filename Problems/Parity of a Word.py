class Solution:
  def parity(self, x):
      result = 0
      while x:
          result ^= 1 
          x &= x - 1 # Gets rid of lowest bit, looping until all bits are removed
      return result
