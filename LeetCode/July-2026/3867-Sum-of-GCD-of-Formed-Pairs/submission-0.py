from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = float('-inf')
        for i in range(len(nums)):
            if nums[i] > mx:
                mx = nums[i]
            prefixGcd.append(gcd(nums[i], mx))

        prefixGcd.sort()
        res = 0

        for i in range(len(prefixGcd)//2):
            res += gcd(prefixGcd[i], prefixGcd[-i-1])
            
        return res
    
#Time Complexity: O(nlogn)
#Space Complexity: O(n)
'''
Algorithm Explanation:
1.  We initialize an empty list `prefixGcd` to store the GCD values and a variable `mx` 
    to keep track of the maximum value encountered so far in the input list `nums`.

2.  We iterate through the input list `nums`. For each element, we update `mx` if the current 
    element is greater than `mx`. We then compute the GCD of the current element and `mx`, and 
    append this GCD value to the `prefixGcd` list.

3.  After processing all elements, we sort the `prefixGcd` list in ascending order.

4.  We initialize a variable `res` to accumulate the sum of GCDs of formed pairs.

5.  We iterate through the first half of the sorted `prefixGcd` list. For each index `i`, 
    we compute the GCD of the element at index `i` and the element at index `-i-1` 
    (which corresponds to the symmetric element from the end of the list). 
    We add this GCD value to `res`.

6.  Finally, we return the accumulated sum `res`, which represents the sum of GCDs of the formed pairs.
'''