"""
28. Find the Index of the First Occurrence
难度: Medium | 类型: string
链接: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

题目描述:
    给定字符串 haystack 和 needle，返回 needle 在 haystack 中首次出现的索引，不存在则返回 -1。

示例:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1

约束:
    1 <= haystack.length, needle.length <= 10^4
    haystack 和 needle 只含小写字母
"""

from typing import List

def make_lps(needle):
    lps = [0] * len(needle)
    i, j = 1, 0
    while i < len(needle):
        if needle[i] == needle[j]:
            j = j + 1
            lps[i] = j
            i = i + 1
        elif j > 0:
            j = lps[j-1]
        else:
            lps[i] = 0
            i = i + 1
    return lps

def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    lps = make_lps(needle)

    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            j = j + 1
            i = i + 1
            if j == len(needle):
                return i - len(needle)
        elif j > 0:
            j = lps[j-1]
        else:
            i = i + 1

    return -1


def run_tests():
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("aaa", "aaaa", -1),
        ("abc", "c", 2),
        ("abc", "abc", 0),
        ("abc", "abcd", -1),
        ("mississippi", "issip", 4),
        ("", "", 0),
        ("a", "a", 0),
    ]

    for i, (haystack, needle, expected) in enumerate(test_cases):
        try:
            result = str_str(haystack, needle)
            if result == expected:
                print(f"PASS: case {i+1} - str_str({haystack!r}, {needle!r}) = {result}")
            else:
                print(f"FAIL: case {i+1} - str_str({haystack!r}, {needle!r}) = {result}, expected {expected}")
        except Exception as e:
            print(f"ERROR: case {i+1} - str_str({haystack!r}, {needle!r}) raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    run_tests()
