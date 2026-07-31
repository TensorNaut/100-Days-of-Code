from collections import deque

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]: 
        component = [0] * n
        comp = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1
            component[i] = comp

        ans = []

        for u, v in queries:
            ans.append(component[u] == component[v])

        return ans

'''
- Time Complexity: O(n + q),
        where n is the number of nodes and q is the number of queries.
        The first loop runs in O(n) to create the component array, 
        and the second loop runs in O(q) to answer the queries.
- Space Complexity: O(n), 
        where n is the number of nodes. 
        The component array takes O(n) space to store the component information for each node.

-Algorithm Explanation:
1.  We initialize a component array of size n to keep track of the connected components in the graph. 
    Each index in the component array corresponds to a node, and the value at that index represents 
    the component number that the node belongs to.

2.  We iterate through the nums array starting from the second element (index 1). 
    For each element, we check if the difference between the current element and the previous element 
    is greater than maxDiff. If it is, we increment the component counter (comp) to indicate that we 
    have found a new connected component. We then assign the current component number to the corresponding 
    index in the component array.

3.  After constructing the component array, we initialize an empty list ans to store the results of the queries.

4.  We iterate through each query in the queries list. For each query, we extract the two nodes u and v. 
    We check if the component numbers of u and v are the same by comparing component[u] and component[v]. 
    If they are the same, it means there is a path between u and v, so we append True to the ans list; 
    otherwise, we append False.

5.  Finally, we return the ans list containing the results of all the queries.
'''