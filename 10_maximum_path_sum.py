class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        def maxPath(root):
            nonlocal maxSum
            if not root:
                return 0
            left = maxPath(root.left)
            right = maxPath(root.right)
            maxSum = max(maxSum,left+right+root.val)
            return max(left+root.val,right+root.val,0)

        maxSum = float('-inf')
        maxPath(root)
        return maxSum
if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    ob = Solution()
    ans = ob.maxPathSum(root)
    print(ans)
