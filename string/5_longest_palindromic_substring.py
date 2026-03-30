"""
5. Longest Palindromic Substring - 最长回文子串
难度: Medium | 类型: string
链接: https://leetcode.com/problems/longest-palindromic-substring/

题目描述:
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1:
输入: s = "babad"
输出: "bab"
解释: "aba" 同样是符合题意的答案。

示例 2:
输入: s = "cbbd"
输出: "bb"

约束:
- 1 <= s.length <= 1000
- s 仅由数字和英文字母组成
"""

def longestPalindrome(s: str) -> str:
    result = ""
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        if len(s[left+1:right]) > len(result):
            result = s[left+1:right]

        if i + 1 < len(s) and s[i] == s[i+1]:
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right + 1

            if len(s[left+1:right]) > len(result):
                result = s[left+1:right]
    return result

def run_tests():
    test_cases = [
        ("babad", ["bab", "aba"]),  # 可能有多个正确答案
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
        ("bb", ["bb"]),
        ("racecar", ["racecar"]),
    ]
    
    passed = 0
    for i, (s, expected_options) in enumerate(test_cases):
        result = longestPalindrome(s)
        
        if result in expected_options:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: s={repr(s)}\n    expected one of={expected_options}\n         got={repr(result)}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
