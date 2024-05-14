# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxLevel = -1

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rightSideViewRecursive(curNode, level, arr):
            if curNode:
                if level > self.maxLevel:
                    arr.append(curNode.val)
                    self.maxLevel = level

                if curNode.right:
                    rightSideViewRecursive(curNode.right, level+1, arr)
                
                if curNode.left:
                    rightSideViewRecursive(curNode.left, level+1, arr)

            return arr

        maxLevel = -1
        return rightSideViewRecursive(root, 0, [])
        