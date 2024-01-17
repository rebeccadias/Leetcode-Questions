import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]  # Start with 1, the first ugly number
        seen = {1}  # Set to keep track of ugly numbers we've seen

        for _ in range(n - 1):  # We need to find n ugly numbers
            current_ugly = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_ugly = current_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return heapq.heappop(heap)  # The n-th ugly number

# Example usage
sol = Solution()
print(sol.nthUglyNumber(10))  # Example to get the 10th ugly number



"""To optimize your code to avoid a Time Limit Exceeded (TLE) error, we need to reduce the number of unnecessary computations. 
Your current approach checks each number sequentially to determine if it's an ugly number, which is inefficient. We can improve this by directly generating ugly numbers from the existing ones. 
This way, we avoid checking non-ugly numbers altogether."""
#Getting TLE 407/596 test cases passed
# import heapq

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         """ Return the nth ugly number """
#         def isUgly(number):
#             """ Check if a number is an ugly number """
#             for factor in [2, 3, 5]:
#                 while number % factor == 0:
#                     number /= factor
#             if number ==1:
#                 return True
#             else:
#                 return False
            
#         heap = []
#         first_ugly = 1
#         heapq.heappush(heap, -first_ugly)  # Use negative numbers for max-heap 

#         while len(heap) != n:
#             first_ugly += 1
#             if isUgly(first_ugly):
#                 heapq.heappush(heap, -first_ugly)
                
#         return -heapq.heappop(heap)  # Negate again to get the positive value


