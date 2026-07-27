class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = float('-inf')
        idx1 = idx2 = -1

        for i, num in enumerate(nums):
            if num > max1:
                max2, idx2 = max1, idx1
                max1, idx1 = num, i
            elif num > max2:
                max2, idx2 = num, i

        print(idx1, idx2)

        return (nums[idx1]-1) * (nums[idx2]-1)


#Time Complexity: O(n) where n is the length of the input array nums. This is because we are iterating through the array once to find the two largest elements.
#Space Complexity: O(1) since we are not using any additional data structures that scale

'''
Optimization:
- Instead of sorting the entire array, we can find the two largest elements in a single pass through the array. 
- This reduces the time complexity from O(n log n) to O(n).
'''