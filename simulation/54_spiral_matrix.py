"""
54. Spiral Matrix - 螺旋矩阵
难度: Medium | 类型: simulation
链接: https://leetcode.com/problems/spiral-matrix/

题目描述:
    给定 m x n 矩阵，按螺旋顺序返回所有元素。
    顺序: 右→下→左→上，依次遍历。

示例:
    输入: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出: [1,2,3,6,9,8,7,4,5]

    输入: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出: [1,2,3,4,8,12,11,10,9,5,6,7]

约束:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    result = []

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


def run_tests():
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5], "3x3螺旋"),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7], "3x4螺旋"),
        ([[1,2,3,4]], [1,2,3,4], "1行"),
        ([[1],[2],[3],[4]], [1,2,3,4], "1列"),
        ([[1,2],[3,4]], [1,2,4,3], "2x2"),
        ([[1]], [1], "1x1"),
        ([[6,9,7]], [6,9,7], "单行3列"),
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
