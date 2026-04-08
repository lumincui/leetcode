"""
567. Permutation in String - 字符串的排列
难度: Medium | 类型: sliding_window
链接: https://leetcode.com/problems/permutation-in-string/

题目描述:
    给定两个字符串 s1 和 s2，写一个函数判断 s1 的某个排列是否作为子串存在于 s2 中。
    如果存在，返回 True；否则返回 False。

示例:
    示例 1:
    输入: s1 = "ab", s2 = "eidbaooo"
    输出: True
    解释: s2 包含 "ba" (即 "ab" 的一个排列)

    示例 2:
    输入: s1 = "ab", s2 = "eidboaooo"
    输出: False

    示例 3:
    输入: s1 = "abc", s2 = "cbaebabacd"
    输出: True
    解释: s2 包含 "cba" (即 "abc" 的一个排列)

约束:
    - 1 <= s1.length <= s2.length <= 10000
    - s1 和 s2 只包含小写字母
"""

from typing import List


def check_inclusion(s1: str, s2: str) -> bool:
    references = [0] * 26
    for c in s1:
        index = ord(c)-ord('a')
        references[index] += 1

    for i in range(len(s2)):
        index = ord(s2[i])-ord('a')
        references[index] -= 1

        if i >= len(s1)-1:
            if i > len(s1)-1:
                left_index = ord(s2[i - len(s1)]) - ord('a')
                references[left_index] += 1

            if references[index] == 0 and not any(references):
                return True

    return False


def run_tests():
    test_cases = [
        ("ab", "eidbaooo", True, "官方示例1 - ab在eidbaooo中"),
        ("ab", "eidboaooo", False, "官方示例2 - ab不在eidboaooo中"),
        ("abc", "cbaebabacd", True, "官方示例3 - abc在cbaebabacd中"),
        ("hello", "oolehl", True, "hello的排列在oolehl中"),
        ("abc", "abd", False, "无匹配"),
        ("a", "a", True, "单字符相同"),
        ("a", "b", False, "单字符不同"),
        ("abc", "abc", True, "完全相同"),
        ("abc", "acb", True, "acb是abc的排列"),
        ("abcd", "abc", False, "s1比s2长"),
    ]

    passed = 0
    for s1, s2, expected, desc in test_cases:
        result = check_inclusion(s1, s2)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")

    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
