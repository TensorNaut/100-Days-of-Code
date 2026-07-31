class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        sett = set()

        for i in range(n):
            for j in range(n):
                xor = nums[i] ^ nums[j]
                sett.add(xor)

        res = set()

        for val in sett:
            for num in nums:
                res.add(val ^ num)
        
        return len(res)


#Time Complexity: O(n^2)
#Space Complexity: O(n)

'''
Approach:
1.  We first calculate the XOR of every pair of elements in the input list `nums` and store the results in a set called `sett`. 
    This ensures that we only keep unique XOR values.
2.  Next, we iterate through each unique XOR value in `sett` and for each value, we compute the XOR with every element in `nums`. 
    The results are stored in another set called `res`, which again ensures that we only keep unique values.
3.  Finally, we return the size of the `res` set, 
    which represents the total number of unique XOR triplets that can be formed from the input list `nums`.
'''