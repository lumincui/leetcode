"""
912. Sort an Array - 排序数组
难度: Medium | 类型: array / quicksort
链接: https://leetcode.com/problems/sort-an-array/

题目描述:
    给你一个整数数组 nums，请将该数组升序排列。
    本练习要求你使用原地快速排序实现，不要使用内置排序函数。

示例:
    示例 1:
    输入: nums = [5,2,3,1]
    输出: [1,2,3,5]

    示例 2:
    输入: nums = [5,1,1,2,0,0]
    输出: [0,0,1,1,2,5]

约束:
    - 1 <= nums.length <= 5 * 10^4
    - -5 * 10^4 <= nums[i] <= 5 * 10^4
    - 请原地修改 nums，并返回 nums
"""

from typing import List


def sort_array(nums: List[int]) -> List[int]:
    def partition(left, right):
        pivot = nums[right]

        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1

        nums[i], nums[right] = nums[right], nums[i]
        return i

    def sort(left, right):
        if left >= right:
            return

        p = partition(left, right)
        sort(left, p-1)
        sort(p+1, right)

    sort(0, len(nums)-1)
    return nums


def run_tests():
    test_cases = [
        ([5, 2, 3, 1], [1, 2, 3, 5], "官方示例1"),
        ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5], "官方示例2"),
        ([1], [1], "单元素"),
        ([2, 1], [1, 2], "两个元素逆序"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "已经升序"),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "完全逆序"),
        ([3, 3, 3, 3], [3, 3, 3, 3], "全部相等"),
        ([-1, 5, 0, -3, 8, -3], [-3, -3, -1, 0, 5, 8], "包含负数和重复值"),
        ([10, -10, 7, 7, 0, 2, -1], [-10, -1, 0, 2, 7, 7, 10], "正负混合"),
    ]

    passed = 0
    for input_nums, expected, desc in test_cases:
        nums = input_nums.copy()
        original_id = id(nums)
        result = sort_array(nums)

        if id(nums) != original_id:
            print(f"FAIL: {desc} - nums 对象不应被替换")
        elif result is not nums:
            print(f"FAIL: {desc} - 应返回原 nums 对象")
        elif nums == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {nums}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
