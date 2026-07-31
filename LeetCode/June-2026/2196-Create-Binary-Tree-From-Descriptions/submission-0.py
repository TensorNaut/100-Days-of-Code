# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, isleft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if isleft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        
            children.add(child)

        root_val = (set(nodes.keys()) - children).pop()
        return nodes[root_val]
    



# Time Complexity: O(n)
# Space Complexity: O(n)
'''The algorithm iterates through the list of descriptions once, 
which takes O(n) time. The space complexity is O(n) because we are 
storing each unique node in a dictionary, and in the worst case, 
all nodes could be unique. Additionally, we are using a set to keep 
track of child nodes, which also contributes to the space complexity.'''   