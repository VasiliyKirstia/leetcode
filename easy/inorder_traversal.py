from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        nodes_to_visit = [root]
        result = []

        while nodes_to_visit:
            if nodes_to_visit[-1].left is not None:
                nodes_to_visit.append(nodes_to_visit[-1].left)
                nodes_to_visit[-2].left = None

            else:
                node = nodes_to_visit.pop()
                result.append(node.val)

                if node.right is not None:
                    nodes_to_visit.append(node.right)

        return result
