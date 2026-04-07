"""
496. Next Greater Element I - 下一个更大元素 I
难度: Easy | 类型: monotonic_stack
链接: https://leetcode.com/problems/next-greater-element-i/

题目描述:
    给定两个没有重复元素的数组 nums1 和 nums2，nums1 是 nums2 的子集。
    对于 nums1 中每个元素，找出其在 nums2 中对应位置的下一个更大元素。

示例:
    输入: nums1 = [4,1,2], nums2 = [1,3,4,2,5]
    输出: [-1,3,-1]

    输入: nums1 = [2,4], nums2 = [1,2,3,4]
    输出: [3,-1]

约束:
    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 10000
    nums1 和 nums2 没有重复元素
"""

from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    result = {}

    for i, num in enumerate(nums2):
        while stack and nums2[stack[-1]] <= num:
            pos = stack.pop()
            value = nums2[pos]
            result[value] = num
        stack.append(i)

    return [result[x] if x in result else -1 for x in nums1]



def run_tests():
    test_cases = [
        (([4,1,2], [1,3,4,2,5]), [5,3,5], "订正示例1: 右侧最近更大"),
        (([2,4], [1,2,3,4]), [3,-1], "官方示例2"),
        (([1,2,3], [3,2,1]), [-1,-1,-1], "递减序列"),
        (([1,2,3], [1,2,3]), [2,3,-1], "子集等于自身"),
        (([3], [1,2,3]), [-1], "单元素无更大"),
        (([5], [1,2,3,4,5]), [-1], "单元素是最大"),
        (([1,3,5,2,4], [1,3,5,2,4]), [3,5,-1,4,-1], "nums1等于nums2"),
    ]

    passed = 0
    for args, expected, desc in test_cases:
        result = next_greater_element(*args)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
