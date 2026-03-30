'''
199. Binary Tree Right Side View
难度: Medium | 类型: tree
链接: https://leetcode.com/problems/binary-tree-right-side-view/

题目描述:
    给定一棵二叉树的根节点，想象自己站在树的右侧，
    返回从上到下你能看到的节点值列表（每层最右边的节点）。

示例:
    输入: root = [1,2,3,null,5,null,4]
    输出: [1,3,4]

    输入: root = [1,2,3,4,null,null,null,5]
    输出: [1,3,4,5]

    输入: root = [1,null,3]
    输出: [1,3]

    输入: root = []
    输出: []

约束:
    - 树中节点数范围：[0, 100]
    - -100 <= Node.val <= 100
'''

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    # TODO: 在这里写你的解法
    pass


# ---- 辅助函数：从列表构建树（LeetCode 层序格式）----
def build_tree(vals):
    if not vals or vals[0] is None:
        return None
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
        # (树的层序列表, 期望输出)
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
        ([1, None, 3], [1, 3]),
        ([], []),
        ([1], [1]),
    ]
    for i, (vals, expected) in enumerate(test_cases):
        root = build_tree(vals)
        result = rightSideView(root)
        if result == expected:
            print(f'PASS: Case {i+1}')
        else:
            print(f'FAIL: Case {i+1} | Expected: {expected}, Got: {result}')


if __name__ == '__main__':
    run_tests()
