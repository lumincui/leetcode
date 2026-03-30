"""
33. Search in Rotated Sorted Array - 搜索旋转排序数组
难度: Medium | 类型: binary_search
链接: https://leetcode.com/problems/search-in-rotated-sorted-array/

题目描述:
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

示例 3:
输入: nums = [1], target = 0
输出: -1

约束:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums 中的每个值都 独一无二
- 题目数据保证 nums 在预先未知的某个下标上进行了旋转
- -10^4 <= target <= 10^4
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    return search_by_pos(nums, 0, len(nums)-1, target)

def search_by_pos(nums: List[int], begin, end, target: int) -> int:
    if end - begin < 4:
        for i in range(begin, end+1):
            if nums[i] == target:
                return i
        return -1

    head, mid, tail = begin, (begin+end)//2 ,end
    if nums[head] < nums[mid] and nums[mid] < nums[tail]:
        if nums[head] <= target and target <= nums[mid]:
            return search_by_pos(nums, head,mid, target)
        else:
            return search_by_pos(nums, mid,tail, target)
    else:
        left = search_by_pos(nums,head,mid, target)
        if left != -1:
            return left
        return search_by_pos(nums,mid,tail, target)

def run_tests():
    test_cases = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([5,1,3], 5, 0),
        ([4,5,6,7,8,1,2,3], 8, 4),
        ([3,1], 1, 1),
    ]
    
    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases):
        result = search(nums, target)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: nums={nums}, target={target}, expected={expected}, got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
