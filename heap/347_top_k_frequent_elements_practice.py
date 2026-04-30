"""
347. Top K Frequent Elements - 前 K 个高频元素
难度: Medium | 类型: hashmap / heap
链接: https://leetcode.com/problems/top-k-frequent-elements/

题目描述:
    给你一个整数数组 nums 和一个整数 k，请返回其中出现频率最高的 k 个元素。
    可以按任意顺序返回答案。

示例:
    示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

    示例 2:
    输入: nums = [1], k = 1
    输出: [1]

约束:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k 的取值范围是 [1, 数组中不相同元素的个数]
    - 题目保证答案唯一
"""

from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # TODO: 返回出现频率最高的 k 个数字，顺序不限。
    # 要求:
    # 1. 不要直接使用 Counter(nums).most_common(k)
    # 2. 你可以使用哈希表 + 小顶堆，也可以使用桶排序
    pass


def run_tests():
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2], "官方示例1"),
        ([1], 1, [1], "官方示例2"),
        ([4, 4, 4, 6, 6, 7, 8], 1, [4], "只取最高频"),
        ([1, 1, 2, 2, 2, 3, 3, 4], 2, [2, 1], "前两个高频"),
        ([-1, -1, -1, 2, 2, 3, 3, 3, 3], 2, [3, -1], "包含负数"),
        ([5, 5, 6, 6, 6, 7, 7, 7, 7, 8], 3, [7, 6, 5], "k 大于 1 且频率分层"),
        ([9, 8, 7, 6], 4, [9, 8, 7, 6], "k 等于不同元素个数"),
    ]

    passed = 0
    for nums, k, expected, desc in test_cases:
        result = top_k_frequent(nums[:], k)
        if len(result) != k:
            print(f"FAIL: {desc} - Expected length {k}, got {len(result)}")
        elif set(result) == set(expected):
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected any order of {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
