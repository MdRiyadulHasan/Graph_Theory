class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        def height(root):
            nonlocal diameter
            if not root:
                return 0
                
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter,left+right)
            return 1+max(left,right)
        diameter = 0
        height(root)
        return diameter
if __name__ == '__main__':
    root = TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(4)
    root.left.left.left=TreeNode(8)
    root.left.left.left.left = TreeNode(10)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.right.left.left=TreeNode(9)
    root.left.right.left.left.right = TreeNode(11)
    root.right = TreeNode(3)
    ob = Solution()
    ans = ob.diameterOfBinaryTree(root)


