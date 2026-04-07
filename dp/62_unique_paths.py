"""
62. Unique Paths - 不同路径
难度: Medium | 类型: dp
链接: https://leetcode.com/problems/unique-paths/

题目描述:
    机器人位于 m x n 网格左上角。
    机器人只能向下或向右移动。
    求到达右下角的不同路径数。

示例:
    输入: m = 3, n = 7
    输出: 28

    输入: m = 3, n = 2
    输出: 3

约束:
    1 <= m, n <= 100
"""

from typing import List


def unique_paths(m: int, n: int) -> int:
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    return dp[-1][-1]


def run_tests():
    test_cases = [
        ((3, 7), 28, "官方示例1: 3x7网格"),
        ((3, 2), 3, "官方示例2: 3x2网格"),
        ((1, 1), 1, "1x1网格最小情况"),
        ((1, 10), 1, "1行多列只有向下或向右一条路径"),
        ((10, 1), 1, "多行1列只有向下或向右一条路径"),
        ((2, 2), 2, "2x2网格"),
        ((7, 3), 28, "交换m和n位置应相同"),
        ((3, 3), 6, "3x3网格"),
    ]

    passed = 0
    for args, expected, desc in test_cases:
        result = unique_paths(*args)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
