class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(n)}

        for src, dst in invocations:
            adj[src].append(dst)

        q = [k]
        visited = set([k])

        while q:
            suspicious = q.pop()

            for nei in adj[suspicious]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        res = []

        for method in range(n):
            if method in visited:
                continue

            for nei in adj[method]:
                if nei in visited:
                    return list(range(n))

            res.append(method)

        return res


#Time Complexity: O(N+M)
#Space Complexity: O(N+M)
'''
Approach:
1. Create an adjacency list to represent the invocations between methods.
2. Use a queue to perform a breadth-first search (BFS) starting from the method k, marking all reachable methods as visited.
3. After the BFS, iterate through all methods to check if they are not visited and if they do not invoke any visited methods.
4. If a method is not visited and does not invoke any visited methods, add it to the result list.
'''