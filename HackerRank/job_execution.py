"""
There are **n **jobs that can be executed in parallel on a processor, where the execution time of the **i^th** job is **executionTime[i]**. To speed up execution, the following strategy is used.
In one operation, a job is chosen, the **major job**, and is executed for **x **seconds. All other jobs are executed for **y** seconds where **y &lt; x**.

A job is complete when it has been executed for at least **executionTime[i] **seconds, then it exits the pool. Find the minimum number of operations in which the processor can completely execute all the jobs if run optimally.

Example

Consider **n = 5, executionTime = [3, 4, 1, 7, 6], x = 4 **and **y = 2.**

The following strategy is optimal using 1-based indexing.


- Choose job 4 as the <i>major job and reduce the execution times of job 4 by </i>**x = 4** and of other jobs by **y = 2**. Now **executionTime = [1, 2, -1, 3, 4]. **Job 3 is complete, so it is removed.
- Choose job 4, **executionTime = [-1, 0, -, -1, 2]. **So, jobs 1, 2, and 4 are now complete.
- Choose job 5, **executionTime = [-, -, -, -, -2]. **Job 5 is complete.

It takes 3 operations to execute all the jobs so the answer is 3.

Function Description

Complete the function **getMinimumOperations** in the editor below.



**getMinimumOperations** has the following parameters:

    **int executionTime[n]:** the execution times of each job

    **int x**: the time for which the major job is executed

    **int y**: the time for which all other jobs are executed



Returns

**int: **the minimum number of operations in which the processor can complete the jobs



Constraints
- 1 ≤ **n** ≤ 10^5
- 1 ≤ **executionTime[i]** ≤ 10^9
- 1 ≤ **y** &lt; **x** ≤ 10^9

Input Format For Custom Testing

The first line contains an integer, **n**, that denotes the number of elements in **executionTime[]**.

Each line **i** of the **n** subsequent lines (where **0 ≤ i &lt; n**) contains an integer that describes **executionTime[i].**

The next line contains an integer, **x**

The last line contains an integer, **y**

Sample Case 0

Sample Input For Custom Testing

```STDIN        FUNCTION
-----        --------
5       →    executionTime[] size, n = 5
3       →    executionTime = [3, 3, 6, 3, 9]
3
6
3
9
3       →    x = 3
2       →    y = 2
```

Sample Output

```3```

- Choose job 5, then **executionTime = [1, 1, 4, 1, 6]. **All jobs are still in the pool.
- Choose job 5, then **executionTime = [-1, -1, 2, -1, 3]. **So, jobs 1, 2, and 4 are complete.
- Choose job 5, then **executionTime = [-, -, 0, -, 0]. **Jobs 3 and 5 are complete.

Sample Case 1

Sample Input For Custom Testing

```STDIN        FUNCTION
-----        --------
3       →    executionTime[] size, n = 3
2       →    executionTime = [2, 3, 5]
3
5
3       →    x = 3
1       →    y = 1
```

Sample Output

```3```

Explanation




- Choose job 3, then **executionTime = [1, 2, 2]. **All jobs are still in the pool.
- Choose job 3, then **executionTime = [0, 1, -1]. **Jobs 1 and 3 are complete.
- Choose job 2, then **executionTime = [-, -2, -]. **Job 2 is complete.

"""
