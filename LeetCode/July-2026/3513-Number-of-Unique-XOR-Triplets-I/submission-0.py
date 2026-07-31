class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        k = len(bin(n)[2:])

        if n == 1 or n == 2:
            k -= 1

        return 2**k


#Time Complexity: O(1)
#Space Complexity: O(1)
'''
Approach:
1.  The number of unique XOR triplets can be determined by the number of bits required to represent the length of the input list `nums`. 
    This is because each bit can either be 0 or 1, leading to a total of 2^k unique combinations, where k is the number of bits.
2.  If the length of `nums` is 1 or 2, we reduce k by 1 since we cannot form triplets with fewer than 3 elements.
3.  Finally, we return 2 raised to the power of k, which gives us the total number of unique XOR triplets possible with the given list.
'''