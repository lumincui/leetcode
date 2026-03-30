"""
215. Kth Largest Element in an Array - 数组中的第K个最大元素
难度: Medium | 类型: heap
链接: https://leetcode.com/problems/kth-largest-element-in-an-array/

题目描述:
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

约束:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    # TODO: 在这里写你的解法
    pass


def run_tests():
    test_cases = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([-1, -1], 2, -1),
        ([99, 99], 1, 99),
        ([7, 6, 5, 4, 3, 2, 1], 5, 3),
    ]
    
    passed = 0
    for i, (nums, k, expected) in enumerate(test_cases):
        # 传入副本，避免原数组被原地排序方法修改
        result = findKthLargest(nums[:], k)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: nums={nums}, k={k}, expected={expected}, got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
