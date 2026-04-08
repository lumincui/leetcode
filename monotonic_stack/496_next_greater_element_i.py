"""
496. Next Greater Element I - 下一个更大元素 I
难度: Easy | 类型: monotonic_stack
链接: https://leetcode.com/problems/next-greater-element-i/

题目描述:
    给定两个没有重复元素的数组 nums1 和 nums2，其中 nums1 是 nums2 的子集。
    对于 nums1 中的每个元素，找出其在 nums2 中对应位置的下一个更大元素。
    如果不存在，则返回 -1。

示例:
    示例 1:
    输入: nums1 = [4,1,2], nums2 = [1,3,4,2]
    输出: [-1, 3, -1]

    示例 2:
    输入: nums1 = [2,4], nums2 = [1,2,3,4]
    输出: [3, -1]

约束:
    - 1 <= nums1.length <= nums2.length <= 1000
    - 0 <= nums1[i], nums2[i] <= 10000
    - nums1 和 nums2 中的所有整数都是唯一的
    - nums1 是 nums2 的子集
"""

from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    单调栈解法：
    1. 从右向左遍历 nums2，维护一个单调递减栈
    2. 对于每个元素，栈顶就是它的下一个更大元素
    3. 用哈希表存储 nums2 中每个元素及其下一个更大元素的映射
    4. 最后遍历 nums1，查表获取结果
    """
    pass


def run_tests():
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1], "官方示例1"),
        ([2, 4], [1, 2, 3, 4], [3, -1], "官方示例2"),
        ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7], "单调递减数组"),
        ([1], [1], [-1], "单元素无更大"),
        ([1], [0, 1], [1], "单元素有更大"),
        ([3, 1, 2], [1, 2, 3], [2, -1, -1], "多个无更大"),
    ]

    passed = 0
    for nums1, nums2, expected, desc in test_cases:
        result = next_greater_element(nums1, nums2)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
