'''
543. Diameter of Binary Tree
难度: Medium | 类型: tree
链接: https://leetcode.com/problems/diameter-of-binary-tree/

题目描述:
    给定一棵二叉树的根节点，返回该树的直径。
    树的直径是指树中任意两节点间最长路径的长度（边的数量）。
    这条路径不一定经过根节点。

示例:
    输入: root = [1,2,3,4,5]
    输出: 3

    输入: root = [1,2]
    输出: 1

约束:
    - 树中节点数量范围 [1, 10^4]
    - -100 <= Node.val <= 100
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        nonlocal diameter
        diameter = max(diameter, left + right)

        return max(left, right) + 1

    dfs(root)
    return diameter


def build_tree(vals):
    """从列表构建二叉树（层序，None表示空节点）"""
    if not vals:
        return None
    from collections import deque
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def run_tests():
    test_cases = [
        # (tree_vals, expected)
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        # 单节点
        ([1], 0),
        # 链状树（左偏）
        ([1, 2, None, 3, None, 4], 3),
        # 路径不过根节点
        ([1, 2, 3, 4, 5, None, None, 6], 4),
    ]
    for i, (vals, expected) in enumerate(test_cases):
        root = build_tree(vals)
        result = diameterOfBinaryTree(root)
        if result == expected:
            print(f'PASS: Case {i+1}')
        else:
            print(f'FAIL: Case {i+1} | Expected: {expected}, Got: {result}')


if __name__ == '__main__':
    run_tests()
