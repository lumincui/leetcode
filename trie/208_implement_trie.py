"""
208. Implement Trie (Prefix Tree) - 实现 Trie (前缀树)
难度: Medium | 类型: trie
链接: https://leetcode.com/problems/implement-trie-prefix-tree/

题目描述:
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
- Trie() 初始化前缀树对象。
- void insert(String word) 向前缀树中插入字符串 word 。
- boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
- boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

示例:
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

约束:
- 1 <= word.length, prefix.length <= 2000
- word 和 prefix 仅由小写英文字母组成
- insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次
"""

class Trie:

    def __init__(self):
        # TODO: 在这里写你的初始化逻辑
        pass

    def insert(self, word: str) -> None:
        # TODO: 在这里写你的 insert 逻辑
        pass

    def search(self, word: str) -> bool:
        # TODO: 在这里写你的 search 逻辑
        pass

    def startsWith(self, prefix: str) -> bool:
        # TODO: 在这里写你的 startsWith 逻辑
        pass


def run_tests():
    def run_sequence(ops, args):
        trie = None
        results = []
        for op, arg in zip(ops, args):
            if op == "Trie":
                trie = Trie()
                results.append(None)
            elif op == "insert":
                results.append(trie.insert(arg[0]))
            elif op == "search":
                results.append(trie.search(arg[0]))
            elif op == "startsWith":
                results.append(trie.startsWith(arg[0]))
        return results

    test_cases = [
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True]
        ),
        (
            ["Trie", "insert", "startsWith"],
            [[], ["hello"], ["hell"]],
            [None, None, True]
        ),
        (
            ["Trie", "search"],
            [[], ["any"]],
            [None, False]
        )
    ]
    
    passed = 0
    for i, (ops, args, expected) in enumerate(test_cases):
        result = run_sequence(ops, args)
        if result == expected:
            print(f"Test {i+1} PASS")
            passed += 1
        else:
            print(f"Test {i+1} FAIL:\n  Operations: {ops}\n  Args: {args}\n  Expected: {expected}\n  Got:      {result}")
            
    print(f"\nTotal: {len(test_cases)} tests, {passed} passed, {len(test_cases) - passed} failed.")

if __name__ == "__main__":
    run_tests()
