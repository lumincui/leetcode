"""
62. Unique Paths - 不同路径
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/unique-paths/

题目描述:
    一个机器人位于 m x n 网格的左上角（起始点为 (0, 0)）。
    机器人每次只能向下或向右移动一步。
    问：有多少条不同的路径可以到达右下角 (m-1, n-1)？

示例:
    示例 1:
    输入: m = 3, n = 7
    输出: 28
    
    示例 2:
    输入: m = 3, n = 2
    输出: 3

约束:
    - 1 <= m, n <= 100
"""

from typing import List


def unique_paths(m: int, n: int) -> int:
    pass


def unique_paths_optimized(m: int, n: int) -> int:
    pass


if __name__ == "__main__":
    def run_tests():
        test_cases = [
            ((3, 7), 28, "m=3, n=7"),
            ((3, 2), 3, "m=3, n=2"),
            ((1, 1), 1, "1x1 网格"),
            ((1, 10), 1, "单行网格"),
            ((10, 1), 1, "单列网格"),
            ((4, 4), 20, "4x4 网格"),
            ((7, 3), 28, "m=7, n=3"),
        ]

        for i, (args, expected, desc) in enumerate(test_cases):
            result = unique_paths(*args)
            status = "PASS" if result == expected else f"FAIL (expected {expected}, got {result})"
            print(f"Test {i+1}: unique_paths{args} = {result} -> {status}")

        print()
        for i, (args, expected, desc) in enumerate(test_cases):
            result = unique_paths_optimized(*args)
            status = "PASS" if result == expected else f"FAIL (expected {expected}, got {result})"
            print(f"Test {i+1}: unique_paths_optimized{args} = {result} -> {status}")

    run_tests()
