class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        mxx = 0
        hs = defaultdict(list)
        for i, j, w in edges:
            hs[i].append((j, w))
            mxx = max(mxx, w)

        def check(target):
            heap = []
            heapq.heappush(heap, (0, 0))
            seen = defaultdict(int)

            while heap:
                sm, node = heapq.heappop(heap)
                if node == len(online) - 1:
                    return True

                if node in seen and seen[node] <= sm:
                    continue

                seen[node] = sm

                for n, w in hs[node]:
                    if sm + w > k:
                        continue
                    if not online[n]:
                        continue
                    if w < target:
                        continue
                    heapq.heappush(heap, (sm+w, n))

            return False

        l = -1
        r = mxx + 1

        while l <= r:
            mid = (l+r)//2

            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return (r) if r >= 0 else -1
    

#Time Complexity: O(E log V log W) where E is the number of edges, V is the number of vertices, and W is the maximum weight of the edges.
#Space Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
'''
Algorithm Explanation:
1.  We first build an adjacency list representation of the graph from the given edges and also keep
    track of the maximum weight of the edges.

2.  We define a helper function `check(target)` that checks if there exists a path from the starting node (0) 
    to the ending node (len(online) - 1) such that all edges in the path have weights greater than or equal to 
    `target` and the total weight of the path does not exceed `k`. This is done using a modified Dijkstra's 
    algorithm with a priority queue (min-heap).

3.  We perform a binary search on the possible edge weights (from -1 to the maximum weight of the edges)
    to find the maximum edge weight that allows for a valid path from the starting node to the ending node.
    If such a path exists for a given weight, we search for higher weights; otherwise, we search for lower weights.

4. Finally, we return the maximum edge weight found that allows for a valid path, or -1 if no such path exists.
'''