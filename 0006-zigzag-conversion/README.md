# [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/submissions/2172210157/)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=flat-square)
![Language: python3](https://img.shields.io/badge/Language-python3-blue?style=flat-square)
![Runtime](https://img.shields.io/badge/Runtime-N%2FA-success?style=flat-square)
![Memory](https://img.shields.io/badge/Memory-N%2FA-informational?style=flat-square)


### Topics
`String`

---

### Description

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
**Input:** s = "PAYPALISHIRING", numRows = 3
**Output:** "PAHNAPLSIIGYIR"
```

**Example 2:**

```
**Input:** s = "PAYPALISHIRING", numRows = 4
**Output:** "PINALSIGYAHRPI"
**Explanation:**
P     I    N
A   L S  I G
Y A   H R
P     I
```

**Example 3:**

```
**Input:** s = "A", numRows = 1
**Output:** "A"
```

**Constraints:**

- `1 <= s.length <= 1000`
	
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
	
- `1 <= numRows <= 1000`

---

*Solved on Oct 14, 2026 using **LeetCommit**.*
