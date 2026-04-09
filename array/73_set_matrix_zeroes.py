"""
73. Set Matrix Zeroes
难度: Medium | 类型: array
链接: https://leetcode.com/problems/set-matrix-zeroes/

题目描述:
    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设置为 0。
    你需要原地修改矩阵。

示例:
    示例 1:
    输入: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    输出: [[1,0,1],[0,0,0],[1,0,1]]

    示例 2:
    输入: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    输出: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

约束:
    - m == matrix.length
    - n == matrix[0].length
    - 1 <= m, n <= 200
    - -2^31 <= matrix[i][j] <= 2^31 - 1
"""

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    zeros = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0 :
                zeros.append((row, col))

    for row, col in zeros:
        for i in range(len(matrix[row])):
            matrix[row][i] = 0
        for i in range(len(matrix)):
            matrix[i][col] = 0


def run_tests():
    test_cases = [
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]], "示例1"),
        ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]], "示例2"),
        ([[0]], [[0]], "单元素为0"),
        ([[1]], [[1]], "单元素非0"),
        ([[1,2,3],[4,0,6],[7,8,9]], [[1,0,3],[0,0,0],[7,0,9]], "中间位置0"),
        ([[0,1,2,3],[4,5,6,7],[8,9,10,11]], [[0,0,0,0],[0,5,6,7],[0,9,10,11]], "第一行有0"),
        ([[1,2,3],[4,5,6],[7,8,0]], [[1,2,0],[4,5,0],[0,0,0]], "最后一位为0"),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [[1,2,3,4],[5,6,7,8],[9,10,11,12]], "无0"),
    ]

    passed = 0
    for input_matrix, expected, desc in test_cases:
        matrix = [row[:] for row in input_matrix]
        setZeroes(matrix)
        if matrix == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {matrix}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()