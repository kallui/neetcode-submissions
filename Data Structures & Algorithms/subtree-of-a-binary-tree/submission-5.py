# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def dfs(curr, sub):
            if not curr:
                return False
            
            # check if head of subroot matches with a node in root
            if curr.val == sub.val:
                if checkSub(curr.left, sub.left) and checkSub(curr.right, sub.right):
                    return True
            
            return dfs(curr.left, sub) or dfs(curr.right, sub)
         
        def checkSub(curr,sub):
            if not curr and not sub:
                return True
            if not curr or not sub or curr.val != sub.val:
                return False

            return checkSub( curr.left, sub.left) and checkSub(curr.right, sub.right)
            
        return dfs(root, subRoot)