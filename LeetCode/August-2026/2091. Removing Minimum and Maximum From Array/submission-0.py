class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)
        min_idx = max_idx = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == minn:
                min_idx = i+1
            elif nums[i] == maxx:
                max_idx = i+1

        c1 = max(min_idx, max_idx)
        c2 = n+1 - min(min_idx, max_idx)
        c3 = min((max_idx + n+1-min_idx), (min_idx + n+1-max_idx))

        return min(c1, c2, c3)


#Time Complexity: O(n)
#Space Complexity: O(1)

'''
Approach:
1. Find the minimum and maximum values in the array.
2. Find the indices of the minimum and maximum values.
3. Calculate the number of deletions required to remove both the minimum and maximum values from the array using three different strategies:
   a. Remove elements from the left side of the array until both minimum and maximum are removed.
   b. Remove elements from the right side of the array until both minimum and maximum are removed.
   c. Remove elements from both sides of the array until both minimum and maximum are removed.
4. Return the minimum number of deletions required among the three strategies.
'''