"""
75. Sort Colors - 颜色分类
难度: Medium | 类型: two_pointers
链接: https://leetcode.com/problems/sort-colors/

题目描述:
    给定一个包含红色、白色和蓝色，共 n 个元素的数组 nums，
    需要将它们按照 0(红)、1(白)、2(蓝) 的顺序进行排序。
    要求原地排序，不使用排序库。

示例:
    示例1:
    nums = [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]

    示例2:
    nums = [2,0,1]
    输出: [0,1,2]

约束:
    n == nums.length
    1 <= n <= 300
    nums[i] 为 0、1 或 2
"""

from typing import List


def sort_colors(nums: List[int]) -> None:
    left, i, right = 0,0, len(nums)-1

    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
        else:
            i = i+1

def run_tests():
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2], "官方示例1"),
        ([2, 0, 1], [0, 1, 2], "官方示例2"),
        ([0], [0], "单元素"),
        ([1, 0], [0, 1], "两元素"),
        ([2, 2, 0, 0, 1, 1], [0, 0, 1, 1, 2, 2], "全排列"),
        ([2, 1, 2, 1, 0, 0], [0, 0, 1, 1, 2, 2], "复杂排列"),
        ([1, 1, 1], [1, 1, 1], "全1"),
        ([2, 2, 2, 0, 0], [0, 0, 2, 2, 2], "开头两0"),
    ]
    
    passed = 0
    for input_nums, expected, desc in test_cases:
        nums = input_nums.copy()
        sort_colors(nums)
        if nums == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {nums}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
