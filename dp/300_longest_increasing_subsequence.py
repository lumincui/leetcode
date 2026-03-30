'''
300. Longest Increasing Subsequence
难度: Medium | 类型: 动态规划 (LIS)
链接: https://leetcode.com/problems/longest-increasing-subsequence/

题目描述:
    给定一个未排序的整数数组 nums，返回最长递增子序列的长度。

示例:
    输入: [10,9,2,5,3,7,101,18]
    输出: 4
    解释: 最长递增子序列是 [2,3,7,101]，长度为4。

    输入: [0,1,0,3,2,3]
    输出: 4

    输入: [7,7,7,7,7,7,7]
    输出: 1

约束:
    - 1 <= nums.length <= 2500
    - -10^4 <= nums[i] <= 10^4
'''

from typing import List

def find(dp, target):
    for i in range(len(dp)):
        if dp[i] >= target:
            return i
    return len(dp)

def lengthOfLIS(nums: List[int]) -> int:
    dp = {}
    for num in nums:
        pos = find(dp, num)
        dp[pos] = num
    return len(dp)


def run_tests():
    test_cases = [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1),
        ([1], 1),
        ([1,3,6,7,9,4,10,5,6], 6),
        ([], 0),  # 空输入
        ([-1,0,1,2,3], 5),  # 负数
        ([5,4,3,2,1], 1),  # 严格递减
    ]
    
    for i, (inputs, expected) in enumerate(test_cases):
        result = lengthOfLIS(inputs)
        if result == expected:
            print(f'PASS: Case {i+1}')
        else:
            print(f'FAIL: Case {i+1} | Expected: {expected}, Got: {result}')

if __name__ == '__main__':
    run_tests()