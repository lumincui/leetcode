"""
153. Find Minimum in Rotated Sorted Array
难度: Medium | 类型: binary_search
链接: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

题目描述:
    假设一个按非递减顺序排序的数组在某个 pivot 处被旋转了
    （例如 [0,1,2,4,5,6,7] 可能变成 [4,5,6,7,0,1,2]）。
    给你一个这样的数组，找出其中的最小元素。必须 O(log n) 时间。

示例:
    示例 1:
    输入: [3,4,5,1,2]
    输出: 1

    示例 2:
    输入: [4,5,6,7,0,1,2]
    输出: 0

    示例 3:
    输入: [11,13,15,17]
    输出: 11

约束:
    - 数组中的所有元素都不同
    - 数组在某个 pivot 处被旋转
    - 1 <= nums.length <= 1000
"""

from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


def run_tests():
    test_cases = [
        ([3,4,5,1,2], 1, "示例1"),
        ([4,5,6,7,0,1,2], 0, "示例2"),
        ([11,13,15,17], 11, "示例3未旋转"),
        ([1], 1, "单元素"),
        ([2,1], 1, "两元素"),
        ([2,3,1], 1, "最小在末尾"),
        ([3,1,2], 1, "最小在中间"),
        ([5,1,2,3,4], 1, "最小在第二位置"),
    ]

    passed = 0
    for nums, expected, desc in test_cases:
        result = findMin(nums)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()