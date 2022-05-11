# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class UnbalancedTreeError(Exception):
    pass


class Solution:
    def height(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        left = self.height(root.left) + 1
        right = self.height(root.right) + 1

        if abs(left - right) > 1:
            raise UnbalancedTreeError()

        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        try:
            self.height(root)
        except UnbalancedTreeError:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('c', 'cv'))