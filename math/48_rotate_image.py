"""
48. Rotate Image - 旋转图像
难度: Medium | 类型: array / math
链接: https://leetcode.com/problems/rotate-image/

题目描述:
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

示例 1:
输入: matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出: [[7,4,1],[8,5,2],[9,6,3]]

示例 2:
输入: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

约束:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000
"""

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # TODO: 在这里写你的解法
    pass


def run_tests():
    test_cases = [
        (
            [[1,2,3],[4,5,6],[7,8,9]], 
            [[7,4,1],[8,5,2],[9,6,3]]
        ),
        (
            [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], 
            [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        ),
        (
            [[1]], 
            [[1]]
        ),
        (
            [[1,2],[3,4]], 
            [[3,1],[4,2]]
        )
    ]
    
    passed = 0
    for i, (matrix, expected) in enumerate(test_cases):
        # 创建深拷贝以进行测试，因为函数是原地修改
        matrix_copy = [row[:] for row in matrix]
        rotate(matrix_copy)
        
        if matrix_copy == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL:\n    original={matrix}\n    expected={expected}\n         got={matrix_copy}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
