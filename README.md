# Programming Challenges Solution Repository

Includes solutions for uWaterloo's CCC, Hackerrank, GeeksForGeeks, LeetCode, Google Kickstart, and some useful graph algorithms in python 3.

NOTE: I made this so that others may learn from the techniques I have used to solve problems that may or may not be mainstream. An example of this is
[2012 S4](CCC/2012/S4%20A%20Coin%20Game.py). The solution found online for Python3 is made by 4/5 people, uses a technique as if they were programming in C++, and barely passed the test cases (in terms of time). I had first created a solution that couldn't pass on time, but only because I had never used the `set` data structure in Python. As soon as I changed the algorithm to use a `set` instead of a `list`, my solution became more efficient than the existing online Python3 solution. I now use sets a lot and always look for this easy optimization.

Another note: I've also noticed that there is a lack of organization / design / aesthetic when it comes to programmers sharing their solutions, and so this repository aims fill that void. I'm obviously not the smartest programmer and I like to create projects so this repository might not have everything you look for.

## Canadian Computing Competition

https://cemc.math.uwaterloo.ca/contests/computing.html

| **Year**  |  **Type**  |  **Completed**  | **Total Score**
|---|---|---|---
| [2019](CCC/2019) |  *Junior* | X - X  | 0/75
| [2019](CCC/2019) |  *Senior* | 1 - 3  | 40/75
| [2018](CCC/2018) |  *Junior* | 1 - 4  | 60/75
| [2018](CCC/2018) |  *Senior* | 1 - 4  | 60/75
| [2017](CCC/2017) |  *Junior* | 1 - 5  | 75/75
| [2017](CCC/2017) |  *Senior* | 1 - 3  | 45/75
| [2016](CCC/2016) |  *Junior* | 1 - 5  | 75/75
| [2016](CCC/2016) |  *Senior* | X - X  | 0/75
| [2015](CCC/2015) |  *Junior* | 1 - 5  | 75/75
| [2015](CCC/2015) |  *Senior* | X - X  | 0/75
| [2014](CCC/2014) |  *Junior* | X - X  | 0/75
| [2014](CCC/2014) |  *Senior* | X - X  | 0/75
| [2013](CCC/2013) |  *Junior* | X - X  | 0/75
| [2013](CCC/2013) |  *Senior* | X - X  | 0/75
| [2012](CCC/2012) |  *Junior* | 1 - 5  | 75/75
| [2012](CCC/2012) |  *Senior* | 4 - 5  | 30/75
| [2011](CCC/2011) |  *Junior* | 1 - 5  | 60/75
| [2011](CCC/2011) |  *Senior* | X - X  | 0/75
| [2010](CCC/2010) |  *Junior* | 1 - 5  | 75/75
| [2010](CCC/2010) |  *Senior* | 1 - 2  | 30/75

## Optimization Tricks

- [Convex Hull Dynamic Programming Optimization](https://jeffreyxiao.me/blog/convex-hull-trick)
  - Test knowledge on [Z-Frog 3](https://atcoder.jp/contests/dp/tasks/dp_z)
    - [Solution](https://youtu.be/HnZKQJtGeHs)
  - "technique is "obvious" to anybody who has learned the [sweep line algorithm](https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms) for the [line segment intersection problem](https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/)."
  - Introduced by Brucker, P. (1995). Efficient algorithms for some path partitioning problems. Discrete Applied Mathematics, 62(1-3), 77-85.
