class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallestOdd = float('inf')

        for num in nums1:
            if num%2 != 0:
                smallestOdd = min(smallestOdd, num)

        if smallestOdd == float('inf'):
            return True

        for num in nums1:
            if num%2 == 0 and num <= smallestOdd:
                return False

        return True


# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Approach:
    1. Find the smallest odd number in the array.
       If there is no odd number, the array is already uniform.

    2. Check every even number. If any even number is less than
       or equal to the smallest odd number, return False.

    3. Otherwise, return True.
'''