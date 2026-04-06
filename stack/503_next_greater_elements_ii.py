"""
503. Next Greater Element II - 下一个更大元素 II
难度: Medium | 类型: monotonic_stack
链接: https://leetcode.com/problems/next-greater-element-ii/

题目描述:
    给定一个循环数组 nums，返回每个元素下一个更大元素的下标。
    下一个更大元素是指该元素在数组中右侧第一个比它大的元素。
    数组是循环的，即最后一个元素的下一个元素是数组的第一个元素。

示例:
    示例1:
    输入: [1,2,1]
    输出: [2,-1,2]
    解释: 第一个1的下一个更大是2；最后一个1的下一个更大是2（因为循环）；2没有更大元素

    示例2:
    输入: [5,4,3,2,1]
    输出: [-1,5,-1,5,5]

约束:
    2 <= nums.length <= 10^3
    1 <= nums[i] <= 10^6
"""

from typing import List


def next_greater_elements(nums: List[int]) -> List[int]:
    stack = []
    greater = [-1] * len(nums)

    for i in range(len(nums)*2):
        i = i%len(nums)
        num = nums[i]
        while stack and num > nums[stack[-1]]:
            pos = stack.pop()
            greater[pos] = num

        stack.append(i)

    return greater


def run_tests():
    test_cases = [
        ([1, 2, 1], [2, -1, 2], "官方示例1"),
        ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5], "官方示例2"),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4], "有重复值"),
        ([1], [-1], "单元素"),
        ([2, 1], [-1, 2], "两元素递减"),
        ([1, 1], [-1, -1], "两元素相同"),
        ([3, 2, 1, 2, 3], [-1, 3, 2, 3, -1], "循环峰值"),
    ]
    
    passed = 0
    for nums, expected, desc in test_cases:
        result = next_greater_elements(nums)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
