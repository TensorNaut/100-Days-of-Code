import heapq
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        count = 0
        amt = 0

        while costs and amt + costs[0] <= coins:
            amt += heapq.heappop(costs)
            count += 1

        return count
    

# Time Complexity: O(n log n) where n is the number of ice cream bars (costs).
# Space Complexity: O(n) for the heap used to store the costs of ice cream bars

'''
The code defines a class `Solution` with a method `maxIceCream` that takes a list of costs for ice cream bars 
and an integer representing the amount of coins available. It uses a min-heap to efficiently retrieve the cheapest 
ice cream bars first. The method counts how many ice cream bars can be purchased without exceeding the available coins. 
The time complexity is O(n log n) due to the heap operations, and the space complexity is O(n) for storing the costs in 
the heap.
'''