# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1

        minDist = float('inf')
        maxDist = -1

        while curr.next:
            next_node = curr.next

            if ((curr.val > prev.val and curr.val > next_node.val) or 
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    first = index
                else:
                    distance = index - last

                    minDist = min(minDist, distance)
                    maxDist = index - first
                
                last = index

            prev = curr
            curr = next_node
            index += 1

        if first == -1 or first == last:
            return [-1, -1]
        
        return [minDist, maxDist]

#Time Complexity: O(n), where n is the number of nodes in the linked list.
#Space Complexity: O(1), as we are using a constant amount of extra space.
'''
Approach:
1. Initialize pointers `prev` and `curr` to traverse the linked list, starting with `prev` at the head and `curr` at the second node. Also, initialize an index counter to keep track of the position of the current node.
2. Use variables `first` and `last` to store the indices of the first and last critical points found in the linked list. Initialize `minDist` to infinity and `maxDist` to -1 to keep track of the minimum and maximum distances between critical points.
3. Traverse the linked list using a while loop until `curr.next` is None. For each node, check if it is a critical point by comparing its value with the values of the previous and next nodes. A node is a critical point if it is either a local maximum or a local minimum.
4. If a critical point is found, update the `first` and `last` indices accordingly. If it's the first critical point, set `first` to the current index. If it's not the first, calculate the distance from the last critical point and update `minDist` and `maxDist` as needed.
5. After traversing the list, check if there are at least two critical points (i.e., `first` and `last` are not the same). If not, return [-1, -1]. Otherwise, return the minimum and maximum distances found.  
'''