'''
105. Construct Binary Tree from Preorder and Inorder Traversal
难度: Medium | 类型: 树 / 递归
链接: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

题目描述:
    给你两个整数数组 preorder 和 inorder，其中 preorder 是二叉树的前序遍历，
    inorder 是同一棵树的中序遍历。请构造并返回这棵二叉树。

示例:
    输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    输出:
        3
       / \
      9  20
        /  \
       15   7

约束:
    - 1 <= preorder.length <= 3000
    - preorder 和 inorder 均无重复元素
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    核心思路：
    1. preorder[0] 是根节点
    2. 在 inorder 中找到根节点位置 idx
       - idx 左边是左子树的 inorder
       - idx 右边是右子树的 inorder
    3. 左子树节点数 left_size = idx
       - preorder[1 : 1+left_size] 是左子树的 preorder
       - preorder[1+left_size :]   是右子树的 preorder
    4. 递归构建左右子树

    优化：用哈希表记录 inorder 中每个值的下标，避免每次 O(n) 查找
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    # 哈希表：值 -> inorder 中的下标
    index_map = {val: i for i, val in enumerate(inorder)}

    def helper(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
        if pre_left > pre_right:
            return None

        # 前序遍历的第一个节点就是根
        root_val = preorder[pre_left]
        root = TreeNode(root_val)

        # 在中序遍历中找根的位置
        in_root = index_map[root_val]

        # 左子树节点数
        left_size = in_root - in_left

        # 递归构建左子树
        root.left = helper(
            pre_left + 1, pre_left + left_size,  # preorder 左子树范围
            in_left, in_root - 1                  # inorder  左子树范围
        )

        # 递归构建右子树
        root.right = helper(
            pre_left + left_size + 1, pre_right,  # preorder 右子树范围
            in_root + 1, in_right                  # inorder  右子树范围
        )

        return root

    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


# ── 辅助函数 ──────────────────────────────────────────────
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def run_tests():
    test_cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
        ([1, 2], [2, 1], [1, 2]),
        ([1, 2], [1, 2], [1, None, 2]),
        ([1, 2, 3], [2, 1, 3], [1, 2, 3]),
    ]
    for i, (pre, ino, expected) in enumerate(test_cases):
        root = buildTree(pre, ino)
        result = tree_to_list(root)
        exp = expected[:]
        while exp and exp[-1] is None:
            exp.pop()
        status = "PASS" if result == exp else "FAIL"
        print(f"{status}: Case {i + 1} | Expected: {exp}, Got: {result}")


if __name__ == '__main__':
    run_tests()
