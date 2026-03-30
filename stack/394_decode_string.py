'''
394. Decode String
难度: Medium | 类型: 栈
链接: https://leetcode.com/problems/decode-string/

题目描述:
    给你一个编码字符串 s，按以下规则解码后返回字符串：
    编码规则：k[encoded_string]，表示方括号内的 encoded_string 重复 k 次。
    输入字符串总是有效的，数字只表示重复次数，支持嵌套。

示例:
    Input: s = "3[a]2[bc]"       -> Output: "aaabcbc"
    Input: s = "3[a2[c]]"        -> Output: "accaccacc"
    Input: s = "2[abc]3[cd]ef"   -> Output: "abcabccdcdcdef"

约束:
    - 1 <= s.length <= 30
    - s 由小写英文字母、数字和方括号 '[]' 组成
    - s 保证是有效输入
    - 所有整数取值范围为 [1, 300]
'''


def decodeString(s: str) -> str:
    stack = []
    for c in s:
        if c == ']':
            sub = ''
            while stack and stack[-1] != '[':
                sub = stack.pop() + sub

            _ = stack.pop()

            times = ''
            while stack and stack[-1] >= '0' and stack[-1] <= '9':
                times = stack.pop() + times

            times = int(times)
            stack.append(sub * times)
        else:
            stack.append(c)

    return ''.join(stack)

def run_tests():
    test_cases = [
        (("3[a]2[bc]",),       "aaabcbc"),
        (("3[a2[c]]",),        "accaccacc"),
        (("2[abc]3[cd]ef",),   "abcabccdcdcdef"),
        (("abc",),             "abc"),          # 无编码，直接返回
        (("10[a]",),           "aaaaaaaaaa"),   # 多位数字
        (("1[b]",),            "b"),            # k=1 边界
    ]
    all_pass = True
    for i, (inputs, expected) in enumerate(test_cases):
        result = decodeString(*inputs)
        if result == expected:
            print(f"PASS: Case {i+1}  '{inputs[0]}' -> '{result}'")
        else:
            print(f"FAIL: Case {i+1}  '{inputs[0]}' | Expected: '{expected}', Got: '{result}'")
            all_pass = False
    print()
    print("All tests passed!" if all_pass else "Some tests FAILED.")


if __name__ == '__main__':
    run_tests()
