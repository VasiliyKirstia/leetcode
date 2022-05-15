from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_deepest_leaves_sum(self, root: TreeNode, depth):
        if root is None:
            return None, None

        if root.left is None and root.right is None:
            return root.val, depth

        lval, ldepth = self.get_deepest_leaves_sum(root.left, depth + 1)
        rval, rdepth = self.get_deepest_leaves_sum(root.right, depth + 1)

        if lval is None:
            return rval, rdepth
        elif rval is None:
            return lval, ldepth
        else:
            if ldepth == rdepth:
                return lval + rval, ldepth
            elif ldepth > rdepth:
                return lval, ldepth
            else:
                return rval, rdepth

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        sum_, deph = self.get_deepest_leaves_sum(root, 0)
        return sum_
