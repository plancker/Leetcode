# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self is not None:
            left = self.left
            right = self.right
            return str({"val": self.val, "left": TreeNode.__str__(left), "right": TreeNode.__str__(right)})
        else:
            return None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if t1 == None and t2 == None:
                return True
            elif t1 == None != t2 == None:
                return False
            else:
                return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        return isMirror(root, root)


arr = [2,3,3,4,5,5]


def construct_tree(root):
    if root < len(arr):
        return TreeNode(arr[root], construct_tree(2 * root + 1), construct_tree(2 * root + 2))
    else:
        return None


X = Solution
print(X.isSymmetric(X, construct_tree(0)))
