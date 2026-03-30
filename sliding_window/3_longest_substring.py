"""
3. Longest Substring Without Repeating Characters - 无重复字符的最长子串
难度: Medium | 类型: sliding_window
链接: https://leetcode.com/problems/longest-substring-without-repeating-characters/

题目描述:
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

约束:
- 0 <= s.length <= 5 * 10^4
- s 由英文字母、数字、符号和空格组成

思路提示:
- 考虑使用双指针（滑动窗口）来维护一个不包含重复字符的区间。
- 可以使用哈希表或集合来快速判断字符是否重复。
"""

def lengthOfLongestSubstring(s: str) -> int:
    # TODO: 在这里写你的解法
    pass


def run_tests():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ]
    
    passed = 0
    for i, (s, expected) in enumerate(test_cases):
        result = lengthOfLongestSubstring(s)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL: input={repr(s)}, expected={expected}, got={result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
