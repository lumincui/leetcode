"""
347. Top K Frequent Elements - 前 K 个高频元素
难度: Medium | 类型: heap
链接: https://leetcode.com/problems/top-k-frequent-elements/

题目描述:
    给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率最高的 k 个元素。
    按任意顺序返回答案。

示例:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

    输入: nums = [1], k = 1
    输出: [1]

约束:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 题目需保证答案唯一
"""

from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    times = {}
    for num in nums:
        times[num] = times.get(num, 0) + 1

    heap = []
    for num, tm in times.items():
        heapq.heappush(heap, (tm, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in heap]



def run_tests():
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2], "官方示例1"),
        ([1], 1, [1], "官方示例2"),
        ([1, 1, 2, 2, 3, 3, 3], 2, [2, 3], "两个高频"),
        ([1], 1, [1], "单元素"),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2], "有负数"),
    ]

    passed = 0
    for nums, k, expected, desc in test_cases:
        result = sorted(topKFrequent(nums, k))
        expected_sorted = sorted(expected)
        if result == expected_sorted:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected_sorted}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
