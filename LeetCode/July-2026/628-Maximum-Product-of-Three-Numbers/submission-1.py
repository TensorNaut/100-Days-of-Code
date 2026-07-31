class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)

    

#Time Complexity: O(n) where n is the length of nums. This is because we are iterating through the list once.
#Space Complexity: O(1) since we are using a constant amount of extra space for the variables max1, max2, max3, min1, and min2.
'''
Approach:
1. Initialize three variables max1, max2, and max3 to negative infinity to keep track of the three largest numbers.
2. Initialize two variables min1 and min2 to positive infinity to keep track of the two smallest numbers.
3. Iterate through the list of numbers:
   - Update max1, max2, and max3 accordingly to find the three largest numbers.
   - Update min1 and min2 accordingly to find the two smallest numbers.
4. The maximum product can be either:
   - The product of the three largest numbers (max1 * max2 * max3).
   - The product of the two smallest numbers and the largest number (min1 * min2 * max1).
5. Return the maximum of these two possibilities.
'''