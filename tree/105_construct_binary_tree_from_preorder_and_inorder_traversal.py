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
    if not preorder:
        return None

    root = preorder[0]
    i = 0
    for i, v in enumerate(inorder):
        if v == root:
            break

    return TreeNode(
        root,
        buildTree(preorder[1:i+1], inorder[:i]),
        buildTree(preorder[i+1:], inorder[i+1:]),
    )


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
