class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        groups = []
        gmap = {}

        for val in sorted(nums):
            if not groups or val - groups[-1][-1] > limit:
                groups.append([])
            groups[-1].append(val)
            gmap[val] = len(groups) - 1

        itr = [iter(g) for g in groups]

        for i in range(len(nums)):
            nums[i] = next(itr[gmap[nums[i]]])

        return nums

# Time Complexity: O(n log n)
# Space Complexity: O(n)
'''
Approach:
    1. Sort the input array nums to facilitate grouping of elements based on the limit.
    2. Iterate through the sorted nums and create groups of elements such that the difference between
       the maximum and minimum elements in each group does not exceed the limit.
    3. Use a dictionary to map each element to its corresponding group index for quick access.
    4. Create iterators for each group to allow sequential access to the elements in sorted order.
    5. Iterate through the original nums array and replace each element with the next element from
       its corresponding group iterator, ensuring that the final array is lexicographically smallest.
    6. Return the modified nums array as the result.
'''