"""
3. Longest Substring Without Repeating Characters - 无重复字符的最长子串
难度: Medium | 类型: sliding_window
链接: https://leetcode.com/problems/longest-substring-without-repeating-characters/

题目描述:
    给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

示例:
    输入: s = "abcabcbb"
    输出: 3
    解释: 无重复字符的最长子串是 "abc"，长度为 3。

    输入: s = "bbbbb"
    输出: 1
    解释: 无重复字符的最长子串是 "b"，长度为 1。

    输入: s = "pwwkew"
    输出: 3
    解释: 无重复字符的最长子串是 "wke"，长度为 3。

约束:
    0 <= s.length <= 5 * 10^4
    s 由英文字母、数字、符号和空格组成
"""

from typing import List


def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    window = set()
    longest = 0

    left, right = 0, 0
    while left <= right and right < len(s):
        if s[right] not in window:
            window.add(s[right])
            longest = max(longest, len(window))
            right = right + 1
        else:
            window.remove(s[left])
            left = left + 1

    return longest


def run_tests():
    test_cases = [
        ("abcabcbb", 3, "官方示例1 - abcabcbb"),
        ("bbbbb", 1, "官方示例2 - bbbbb"),
        ("pwwkew", 3, "官方示例3 - pwwkew"),
        
        ("", 0, "空字符串"),
        ("a", 1, "单字符"),
        ("ab", 2, "两字符无重复"),
        ("aa", 1, "两字符相同"),
        ("abcdef", 6, "全不重复"),
        ("abbcd", 3, "部分重复 - abbc 返回3"),
        ("dvdf", 3, "嵌套重复 - dvdf 返回3"),
        ("abba", 2, "回文重复 - abba 返回2"),
    ]
    
    passed = 0
    for args, expected, desc in test_cases:
        if isinstance(args, tuple):
            result = length_of_longest_substring(*args)
        else:
            result = length_of_longest_substring(args)
        if result == expected:
            print(f"PASS: {desc}")
            passed += 1
        else:
            print(f"FAIL: {desc} - Expected {expected}, got {result}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()