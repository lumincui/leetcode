"""
239. Sliding Window Maximum - 滑动窗口最大值
难度: Hard | 类型: sliding_window / deque
链接: https://leetcode.com/problems/sliding-window-maximum/

题目描述:
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。

示例:
    输入: nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出: [3,3,5,5,6,7]

    输入: nums = [1], k = 1
    输出: [1]

约束:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""

from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    stack = []

    result = []
    for i, num in enumerate(nums):
        for j in range(len(stack)-1, -1, -1):
            if stack[j] >= num:
                break
            stack.pop(j)

        stack.append(num)
        if i < k-1:
            continue

        result.append(stack[0])

        if nums[i-k+1] == stack[0]:
            stack.pop(0)

    return result



def run_tests() -> None:
    test_cases = [
        # 题目示例
        {
            "nums": [1, 3, -1, -3, 5, 3, 6, 7],
            "k": 3,
            "expected": [3, 3, 5, 5, 6, 7],
        },
        {"nums": [1], "k": 1, "expected": [1]},
        # 边界与常见情况
        {"nums": [9, 8, 7, 6], "k": 2, "expected": [9, 8, 7]},
        {"nums": [1, 2, 3, 4], "k": 2, "expected": [2, 3, 4]},
        {"nums": [4, 4, 4, 4], "k": 2, "expected": [4, 4, 4]},
        {"nums": [-1, -3, -2, -5], "k": 2, "expected": [-1, -2, -2]},
        {"nums": [5, 1, 3], "k": 3, "expected": [5]},
    ]

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        got = max_sliding_window(tc["nums"], tc["k"])
        ok = got == tc["expected"]
        if ok:
            passed += 1
            print(f"[PASS] case #{i}: got={got}")
        else:
            print(
                f"[FAIL] case #{i}: nums={tc['nums']}, k={tc['k']}, "
                f"expected={tc['expected']}, got={got}"
            )

    print(f"\nResult: {passed}/{total} passed")


if __name__ == "__main__":
    run_tests()
