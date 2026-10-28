class Solution(object):
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo>1:
            lo, hi = lo - len(A), lo
            A = [range(lo,hi)] +zip(*A[::-1])
        return  A
        """
        :type n: int
        :rtype: List[List[int]]
        """
        