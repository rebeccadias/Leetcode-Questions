class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # heapify everything
        for i in range(len(matrix)):
            heapq.heapify(matrix[i])

        heapq.heapify(matrix)

        while k > 0:
            res = matrix[0][0]
            heapq.heappop(matrix[0])

            if not len(matrix[0]):
                heapq.heappop(matrix)
            
            if len(matrix):
                # restore heap properties.
                # heappop() + heappush() is O(logN + logN)
                # not using heapq.heapify() because it is O(N)
                head = matrix[0]
                heapq.heappop(matrix)
                heapq.heappush(matrix, head)

            k -= 1

        return res
