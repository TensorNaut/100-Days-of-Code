class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort nodes by value
        arr = sorted((nums[i], i) for i in range(n))

        values = [0] * n
        pos = [0] * n

        for i, (val, idx) in enumerate(arr):
            values[i] = val
            pos[idx] = i

        # next[i] = farthest position reachable in one edge
        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        # Binary lifting table
        LOG = (n).bit_length()

        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            # Can't even move from start
            if nxt[a] == a:
                ans.append(-1)
                continue

            cur = a
            steps = 0

            # Jump as much as possible without passing b
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    steps += 1 << k

            # One final jump
            if nxt[cur] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans
    
'''
- Time Complexity: O(n log n + q log n), 
    where n is the number of nodes and q is the number of queries. 
    The sorting step takes O(n log n), building the binary lifting table takes O(n log n), 
    and each query takes O(log n) time.

- Space Complexity: O(n log n), 
    for storing the binary lifting table and other auxiliary arrays.

Approach:
1.  Sort the nodes based on their values while keeping track of their original indices.

2.  Create an array `nxt` where `nxt[i]` represents the farthest position reachable from node `i` in one edge, 
    considering the `maxDiff` constraint.

3.  Build a binary lifting table `up` to allow jumping multiple steps in logarithmic time

4.  For each query, determine the positions of the nodes in the sorted array and use the binary lifting table to 
    find the minimum number of steps required to reach from one node to another, or return -1 if it's not possible.

5.  Return the results for all queries in a list.

6.  The solution efficiently handles multiple queries by leveraging the precomputed structures, ensuring that each 
    query can be answered in logarithmic time after the initial preprocessing.
'''