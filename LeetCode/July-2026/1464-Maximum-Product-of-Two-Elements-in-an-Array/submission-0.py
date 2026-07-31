class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return (nums[0]-1) * (nums[1]-1)



#Time Complexity: O(nlogn) where n is the length of the input array nums. This is because we are sorting the array, which takes O(nlogn) time.
#Space Complexity: O(1) since we are not using any additional data structures that scale with the input size. The sorting is done in place.

'''
Approach:
1. Sort the input array nums in descending order.
2. The two largest elements will be at the first two indices of the sorted array.
3. Calculate the product of (nums[0] - 1) and (nums[1] - 1) and return the result.
'''