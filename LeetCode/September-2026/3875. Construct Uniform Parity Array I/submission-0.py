class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

#Time Complexity: O(n)
#Space Complexity: O(1)
'''
It is always possible to make the array all odd with at least 1 odd number 
since even - odd = odd, if there are no odds the array is already all even 
so it is always possible, the answer is just return true
'''