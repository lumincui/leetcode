"""
438. Find All Anagrams in a String - 找到字符串中所有字母异位词
难度: Medium | 类型: sliding_window
链接: https://leetcode.com/problems/find-all-anagrams-in-a-string/

题目描述:
    给定两个字符串 s 和 p，找到 s 中所有 p 的字母异位词的起始索引，
    并按任意顺序返回这些索引。

    字母异位词指由相同字母重排列形成的字符串。

示例:
    输入: s = "cbaebabacd", p = "abc"
    输出: [0, 6]
    解释:
        起始索引 0 对应子串 "cba"，是 "abc" 的异位词。
        起始索引 6 对应子串 "bac"，是 "abc" 的异位词。

    输入: s = "abab", p = "ab"
    输出: [0, 1, 2]

约束:
    1 <= s.length, p.length <= 3 * 10^4
    s 和 p 仅包含小写英文字母
"""

from typing import List, Tuple


def index(c):
    return ord(c)-ord('a')


def find_anagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    pattern = [0] * 26
    window = [0] * 26

    result = []

    for i in range(len(p)):
        pattern[index(p[i])] += 1
        window[index(s[i])] += 1

    for i in range(len(p)-1, len(s)):
        if i > len(p)-1:
            window[index(s[i])] += 1
            window[index(s[i-len(p)])] -= 1

        if pattern == window:
            result.append(i-len(p)+1)

    return result


def run_tests() -> None:
    test_cases: List[Tuple[str, str, List[int]]] = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("aaaaaaaaaa", "aaaaaaaaaaaa", []),
        ("baa", "aa", [1]),
        ("abc", "def", []),
        ("z", "z", [0]),
    ]

    passed = 0
    total = len(test_cases)

    print("Running tests for 438. Find All Anagrams in a String")
    print("-" * 60)

    for i, (s, p, expected) in enumerate(test_cases, start=1):
        try:
            actual = find_anagrams(s, p)
            if actual == expected:
                passed += 1
                print(f"[PASS] Case {i}: s={s!r}, p={p!r} -> {actual}")
            else:
                print(
                    f"[FAIL] Case {i}: s={s!r}, p={p!r} -> expected {expected}, got {actual}"
                )
        except Exception as exc:
            print(f"[ERROR] Case {i}: s={s!r}, p={p!r} -> {type(exc).__name__}: {exc}")

    print("-" * 60)
    print(f"Passed {passed}/{total} cases")


if __name__ == "__main__":
    run_tests()
