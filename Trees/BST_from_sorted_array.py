# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums) -> TreeNode:
    def construct_tree(first, last, grandparent):
        if last-first > 1:
            root = (first + last) // 2
            return TreeNode(nums[root], construct_tree(first, root-1, root), construct_tree(root+1, last, root))
        elif last-first == 1:
            if grandparent > last:
                return TreeNode(nums[last], nums[first], None)
            else:
                return TreeNode(nums[first], nums[last], None)
        elif last - first == 0:
            return TreeNode(nums[first], None, None)
        else:
            return None

    return construct_tree(0, len(nums) - 1)


print(sortedArrayToBST([-10,-3,0,5,9]))
