"""
54. Spiral Matrix - 螺旋矩阵
难度: Medium | 类型: simulation
链接: https://leetcode.com/problems/spiral-matrix/

题目描述:
    给你一个 m 行 n 列的矩阵 matrix，请按顺时针螺旋顺序返回矩阵中的所有元素。

示例:
    示例 1:
    输入: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出: [1,2,3,6,9,8,7,4,5]

    示例 2:
    输入: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出: [1,2,3,4,8,12,11,10,9,5,6,7]

约束:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    # TODO: 在这里写你的解法
    pass


def run_tests():
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5], "3x3螺旋"),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            "3x4螺旋",
        ),
        ([[1]], [1], "单元素"),
        ([[1, 2]], [1, 2], "单行两列"),
        ([[1], [2], [3]], [1, 2, 3], "单列三行"),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 3, 4, 8, 7, 6, 5], "2x4螺旋"),
    ]

    passed = 0
    for args, expected, desc in test_cases:
        result = spiral_order(args)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
