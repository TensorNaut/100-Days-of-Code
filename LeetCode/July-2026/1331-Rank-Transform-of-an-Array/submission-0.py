class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {value: index for index, value in enumerate(sorted(set(arr)), start = 1)}
        res = []
        for i in arr:
            res.append(rank_map.get(i))
        return res

#Time Complexity: O(n log n), where n is the length of the input array. This is due to the sorting step.
#Space Complexity: O(n), for storing the rank_map and the result array.

'''
Approach:
1.  Create a rank_map that maps each unique value in the input array to its rank (starting from 1). 
    This is done by sorting the unique values and enumerating them.

2.  Initialize an empty result array.

3.  Iterate through the original array and for each element, append its corresponding rank from 
    the rank_map to the result array.

4. Return the result array containing the ranks of the original elements.
'''