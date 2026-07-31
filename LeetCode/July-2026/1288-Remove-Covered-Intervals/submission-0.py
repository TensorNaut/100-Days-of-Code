class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        count = n

        for i in range(n):
            for j in range(n):
                if i != j:
                    if (intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]):
                        count -= 1
                        break
        
        return count
    
#Time Complexity: O(n^2)
#Space Complexity: O(1)

'''
Brute Force Approach: 
    1. Check for each interval if it is covered by any other interval. 
    2. If it is covered, decrement the count of intervals. 
    3. Finally, return the count of non-covered intervals.
'''