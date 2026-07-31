# Time Complexity: O(n)
# Space Complexity: O(n)
'''
The algorithm iterates through the input array `nums` once, which takes O(n) time. 
The space complexity is also O(n) because we are creating three separate lists 
(`smaller`, `equal`, and `greater`) to store the elements based on their relation 
to the pivot. In the worst case, all elements could be in one of these lists, 
leading to O(n) space usage.'''

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        smaller = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return smaller + equal + greater
    

