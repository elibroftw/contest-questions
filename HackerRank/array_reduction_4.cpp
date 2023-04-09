/*
The developers of Hackerland are working on an array reduction algorithm that takes in an array of n integers say arrand does the following until the array arr is empty

- Initialize an array result as an empty array
- Choose an integer k such that  1 ≤ k ≤ length of the array
- Append the MEX of the first k elements of the array arr to the array result
Remove first k elements of the array arr<

Given an array arr, find the lexicographically maximum array result that can be obtained using the above algorithm.

Note:

- An array x is lexicographically greater than an array y if in the first position where x and y differ x_i y_i or if |x| |y| and y is a prefix of x (where |x| denotes the size of the array x).
- The MEX of a set of non-negative integers is the minimal non-negative integer such that it is not in the set. For example, MEX({1,2,3}) = 0 and MEX({0,1,2,4,5}) = 3.

Example

Given n = 4, arr = [0,1,1,0], one of the optimal ways to make array result lexicographically maximum is as follows -


- Take k = 2, the MEX of the 1^st and 2^nd element of arr is 2. So arr = [1,0] and result = [2].
- Take k = 2, the MEX of the 1^st and 2^nd element of arr is 2. So arr = [] and result = [2,2].


arr is now empty and the answer is [2,2].

Function Description

Complete the function getMaxArray in the editor below.

getMaxArray has the following parameter:

    arr[n]:  An array of integers

Returns

    int[]: The lexicographically maximum array result that can be obtained using the above algorithm

Constraints


- 1 ≤ n ≤ 10^5

- 0 ≤ arr[i] ≤ n


Input Format For Custom Testing

The first line contains an integer, n, the number of elements in arr.<br>
Each line i of the n subsequent lines (where 0 ≤ i &lt; n) contains an integer, arr[i].
Sample Case 0

Sample Input For Custom Testing

n = 8
2  arr = [2, 2, 3, 4, 0, 1, 2, 0]
2
3
4
0
1
2
0

Sample Output

5
1
Explanation
Given n = 8, arr = [2,2,3,4,0,1,2,0]

- Take k = 6, the MEX of the first 6 elements of arr is 5. So arr = [2,0] and result = [5].
- Take k = 2, the MEX of the 1^st and 2^nd element of arr is 1. So arr = [] and result = [5,1].

Sample Input For Custom Testing

6        n = 6
0        arr = [0, 1, 2, 3, 4, 6]
1
2
3
4
6

Sample Output

5
0

Explanation

Given n = 6, arr = [0,1,2,3,4,6]




- Take k = 5, the MEX of the first 5 elements of arr is 5. So arr = [6] and result = [5].
- Take k = 2, the MEX of the 1^st element of arr is 0. So arr = [] and result = [5,0].
*/
