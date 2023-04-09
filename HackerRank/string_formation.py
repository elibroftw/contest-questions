"""
Given an array of strings, each of the same length, and a target string, construct the target string using characters from the strings in the given array such that the indices of the characters in the order in which they are used form a strictly increasing sequence. Here the index of a character is the position at which it appears in the string. Note that it is acceptable to use multiple characters from the same string.
Determine the number of ways to construct the target string. One construction is different from another if either the sequences of indices they use are different or the sequences are the same but there exists a character at some index such that it is chosen from a different string in these constructions. Since the answer can be very large, return the value modulo (10^9 + 7).
Consider an example with **n = **3 strings, each of length 3. Let the array of strings be **words = ["adc", "aec", "efg"],** and the target string **target = "ac"**. There are 4 ways to reach the target:


- Select the 1^st character of "adc" and the 3^rd character of "adc".
- Select the 1^st character of "adc" and the 3^rd character of "aec".
- Select the 1^st character of "aec" and the 3^rd character of "adc".
- Select the 1^st character of "aec" and the 3^rd character of "aec".

Function Description

Complete the function **numWays** in the editor below. It must return an integer, modulo** (10^9 + 7).**

**numWays **has the following parameter(s):

    string **words[n]**: an array of strings

    string **target**: the target string

Constraints

- 1 ≤ **n** ≤ 10^3

- 1 ≤ length of **words[i]** ≤ 3000
- All **words[i]** are of equal length per test case.
- The sum of the lengths of all **words[i]** is ≤ 10^5.

- 1 ≤ length of **target** ≤ length of **words[i]**

- All characters are lowercase English letters.
Input Format For Custom Testing

The first line contains an integer, **n,** the number of elements in **words.**

The next **n **lines each contain one string, **words[i]**.

The last line contains one string, **target.**
Sample Case 0

Sample Input For Custom Testing

```STDIN       Function
-----       --------
3      →    words[] size n = 3
valya  →    words = ['valya', 'lyglb', 'vldoh']
lyglb
vldoh
val    →    target = 'val'
```

Sample Output

```4```

Explanation

There are 4 ways to construct the string "val" such that the indices will be in strictly increasing order.

- Select the 1^st character of "valya", the 2^nd character of "valya" and the 3^rd character of "valya".
- Select the 1^st character of "valya", the 2^nd character of "valya" and the 4^th character of "lyglb".
- Select the 1^st character of "vldoh", the 2^nd character of "valya" and the 3^rd character of "valya".
- Select the 1^st character of "vldoh", the 2^nd character of "valya" and the 4^th character of "lyglb".

Sample Case 1

Sample Input For Custom Testing

```STDIN    Function
-----    --------
5    →   words[] size n = 5
xzu  →   words = ['xzu', 'dfw', 'eor', 'mat', 'jyc']
dfw
eor
mat
jyc
cf   →   target = 'cf'
```

Sample Output

```0```

Explanation

There is no way to construct the string "cf" such that the indices will be in strictly increasing order.
"""
