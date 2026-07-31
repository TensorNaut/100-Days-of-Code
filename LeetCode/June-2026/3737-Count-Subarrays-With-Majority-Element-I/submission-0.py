class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == target:
                    count += 1
                length = j-i+1
                if count > length // 2:
                    res += 1

        return res
    
#Time Complexity: O(n^2)
#Space Complexity: O(1)
'''
Brute Force Approach:
1. Initialize a variable `res` to store the count of majority subarrays.
2. Iterate through the array using two nested loops to consider all possible subarrays.
3. For each subarray, count the occurrences of the target element and calculate the length of the subarray.
4. Check if the count of the target element is greater than half the length of the subarray. 
   If it is, increment the `res` counter.
'''