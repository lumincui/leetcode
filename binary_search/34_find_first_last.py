"""
34. Find First and Last Position of Element in Sorted Array
难度: Medium | 类型: binary_search
链接: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

题目描述:
    给定一个按非递减顺序排序的整数数组 nums，找到目标值 target 的起始和结束位置。
    如果数组中不存在 target，返回 [-1, -1]。
    你必须设计并实现 O(log n) 算法。

示例:
    示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3, 4]

    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1, -1]

    示例 3:
    输入: nums = [], target = 0
    输出: [-1, -1]

约束:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - nums 是一个非递减数组
    - -10^9 <= target <= 10^9
"""

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def findBound(findFirst):
        left, right = 0, len(nums) - 1
        bound = -1

        while 0 <= left <= right <= len(nums) - 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                bound = mid
                if findFirst:
                    right = mid - 1
                else:
                    left = mid + 1

        return bound

    return [findBound(True), findBound(False)]



def run_tests():
    test_cases = [
        ([5,7,7,8,8,10], 8, [3, 4], "示例1"),
        ([5,7,7,8,8,10], 6, [-1, -1], "示例2"),
        ([], 0, [-1, -1], "示例3空数组"),
        ([1], 1, [0, 0], "单元素找到"),
        ([1], 0, [-1, -1], "单元素未找到"),
        ([2,2], 2, [0, 1], "两元素相同"),
        ([1,2,3,4,5], 3, [2, 2], "中间位置"),
        ([1,2,3,4,5], 1, [0, 0], "首元素"),
        ([1,2,3,4,5], 5, [4, 4], "尾元素"),
        ([1,2,2,2,3], 2, [1, 3], "重复元素"),
    ]

    passed = 0
    for nums, target, expected, desc in test_cases:
        result = searchRange(nums, target)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()