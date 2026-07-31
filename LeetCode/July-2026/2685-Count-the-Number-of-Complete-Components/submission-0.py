from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree_sum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    cnt_nodes, cnt_degree = dfs(nei)
                    nodes += cnt_nodes
                    degree_sum += cnt_degree

            return nodes, degree_sum

        ans = 0

        for i in range(n):
            if not visited[i]:
                nodes, degree_sum = dfs(i)
                edge_count = degree_sum // 2

                # Complete graph should have k*(k-1)/2 edges
                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans
    

#Time Complexity: O(n + e), where n is the number of nodes and e is the number of edges. We visit each node and edge once during the DFS traversal.
#Space Complexity: O(n + e), for storing the adjacency list and the visited array.
'''
Approach:
1. Build an adjacency list representation of the graph from the given edges.
2. Initialize a visited array to keep track of visited nodes.
3. Define a DFS function that traverses the graph, counting the number of nodes and the sum of their degrees in the connected component.
4. For each unvisited node, perform DFS to find the connected component it belongs to.
5. Calculate the number of edges in the component by dividing the degree sum by 2 (since each edge contributes to the degree of two nodes).
6. Check if the number of edges matches the expected number of edges for a complete graph with the same number of nodes (k*(k-1)/2).
7. If it matches, increment the count of complete components.
'''