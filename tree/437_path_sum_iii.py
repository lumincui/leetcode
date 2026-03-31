'''
437. Path Sum III
难度: Medium | 类型: tree
链接: https://leetcode.com/problems/path-sum-iii/

题目描述:
    给定一棵二叉树的根节点 root 和一个整数 targetSum，
    返回路径总和等于 targetSum 的路径数量。

    路径不需要从根节点开始，也不需要在叶节点结束，
    但路径方向必须是向下的（从父节点到子节点）。

示例:
    输入: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    输出: 3

    输入: root = [1,2,3], targetSum = 3
    输出: 2

约束:
    - 树中节点数量范围 [0, 1000]
    - -10^9 <= Node.val <= 10^9
    - -1000 <= targetSum <= 1000
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    routine = {0: 1}
    count = 0
    def dfs(node: Optional[TreeNode], prefixSum: int = 0):
        if not node:
            return

        prefixSum += node.val

        nonlocal count
        count += routine.get(prefixSum-targetSum, 0)

        routine[prefixSum] = routine.get(prefixSum, 0) + 1

        dfs(node.left, prefixSum)
        dfs(node.right, prefixSum)

        routine[prefixSum] = routine[prefixSum] - 1

    dfs(root)
    return count


def build_tree(vals):
    """从列表构建二叉树（层序，None表示空节点）"""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
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
        # (tree_vals, targetSum, expected)
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([1, 2, 3], 3, 2),
        # 空树
        ([], 0, 0),
        # 单节点，匹配
        ([5], 5, 1),
        # 单节点，不匹配
        ([5], 3, 0),
        # 含负数，路径抵消
        ([1, -1, 1], 0, 1),
    ]
    for i, (vals, target, expected) in enumerate(test_cases):
        root = build_tree(vals)
        result = pathSum(root, target)
        if result == expected:
            print(f'PASS: Case {i+1}')
        else:
            print(f'FAIL: Case {i+1} | Expected: {expected}, Got: {result}')


if __name__ == '__main__':
    run_tests()
