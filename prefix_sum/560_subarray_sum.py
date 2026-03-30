"""
560. Subarray Sum Equals K - 和为 K 的子数组
难度: Medium | 类型: prefix_sum
链接: https://leetcode.com/problems/subarray-sum-equals-k/

题目描述:
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。

示例 1:
输入: nums = [1,1,1], k = 2
输出: 2

示例 2:
输入: nums = [1,2,3], k = 3
输出: 2

约束:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    seen = {0:1}
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        remain = prefix_sum-k
        count += seen.get(remain, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


def run_tests():
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 0, 0),
        ([-1, -1, 1], 0, 1),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ]
    
    passed = 0
    for i, (nums, k, expected) in enumerate(test_cases):
        result = subarraySum(nums, k)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: nums={nums}, k={k}\n    expected={expected}\n         got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
