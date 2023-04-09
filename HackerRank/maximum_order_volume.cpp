/*
https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

DP required

During the day, a supermarket will receive calls from customers who want to place orders.  The supermarket manager knows in advance the number of calls that will be attempted, the start time, duration, and order volume for each call.  Only one call can be in progress at any one time, and if a call is not answered, the caller will not call back.  The manager must choose which calls to service in order to maximize order volume.  Determine the maximum order volume.



Example

start = [10, 5, 15, 18, 30]

duration = [30, 12, 20, 35, 35]

volume = [50, 51, 20, 25, 10]

The following was a comment in the source code for the problem...
<--
Ariana runs a very busy supermarket. Customers need to call the supermarket to place orders. Each call is characterized by the start time, and the call duration. Ariana knows how many calls she will get today, and also, when the calls will be made, the volume of order that will be placed for each call, and the duration of each call. If Ariana doesn&#39;t pick a call when it&#39;s made, the caller will not call again, and Ariana will miss that order. Therefore, she must choose which calls to answer cleverly, in order to get maximum total volume of orders. Can you find the maximum total volume of orders she will receive?
->>

The above data as a table:

If Ariana receives calls such that https://s3.amazonaws.com/istreet-assets/V-CZiBnmz60vXNpz8W_9uA/Calls%20table.png

The first call will start at time = 10, and last until time = 40.

The second call will start at time = 5, and last until time = 17.

The third call will start at time = 15, and last until time = 35.

The fourth call will start at time = 18, and last until time = 53.

The fifth call will start at time = 30, and last until time = 65.



The first call completely overlaps the second and third calls, and partially overlaps the fourth and fifth calls. Choosing calls that do not overlap, and answering the 2<sup>nd</sup> and 4<sup>th</sup> calls leads to the maximum total order volume of 51 + 25 = 76.



<p class="section-title">Function Description

Complete the function phoneCalls in the editor below.



phoneCalls has the following parameter(s):

    int start[n]:  the start times of each call

    int duration[n]:  the durations of each call

    int volume[n]:  the volumes of each order



Returns

    int:  the maximum possible volume of orders that can be received



<p class="section-title">Constraints

<ul>
	<li>1 ≤ n ≤ 10<sup>5</sup></li>
	<li>1 ≤ start[i] ≤ 10<sup>9</sup></li>
	<li>1 ≤ duration[i] ≤ 10<sup>9</sup></li>
	<li>1 ≤ volume[i] ≤ 10<sup>3</sup></li>
</ul>


<!-- <StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details><summary class="section-title">Input Format For Custom Testing</summary>

<div class="collapsable-details">
The first line contains an integer, n, the size of the start array.

Each line i of the n subsequent lines (where 0 ≤ i &lt; n) contains an integer, start[i]

The next line contains repeats the integer, n, the size of the duration array.

Each line i of the n subsequent lines (where 0 ≤ i &lt; n) contains an integer, duration[i]

The next line repeats the integer, n, size of the volume array.

Each line i of the n subsequent lines (where 0 ≤ i &lt; n) contains an integer, volume[i]


</div>
</details>
<!-- </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details open="open"><summary class="section-title">Sample Case 0</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing

<pre>STDIN     Function
-----     --------
3       → start[] size n = 3
1       → start[] = [ 1, 2, 4 ]
2
4
3       →<i> duration</i>[] size n = 3
2       →<i> duration</i>[] = [ 2, 2, 1 ]
2
1
3       → volume[] size n = 3
1       → volume[] = [ 1, 2, 3 ]
2
3</pre>

<p class="section-title">Sample Output

<pre>4</pre>

<p class="section-title">Explanation

The calls happen in the intervals

[1,3]

[2,4]

[4,5]

The first and third calls together make up the order volume 4, and their intervals do not intersect.

The first and second calls intersect, as do the second and third calls. Only one call from either of these pairs can be serviced. The most efficient calls to answer are the first and third, with a total volume of 4.
</div>
</details>

<details><summary class="section-title">Sample Case 1</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing

<pre>STDIN     Function
-----     --------
3       → start[] size n = 3
1       → start[] = [ 1, 10, 100 ]
10
100
3       →<i> duration</i>[] size n = 3
1       →<i> duration</i>[] = [ 1, 10, 100 ]
10
100
3       → volume[] size n = 3
1       → volume[] = [ 1, 10, 100 ]
10
100
</pre>

<p class="section-title">Sample Output

<pre>111</pre>

<p class="section-title">Explanation

The calls happen in the following intervals -

[1 2]

[10 20]

[100 200]

All three calls can be attended. So the total volume is 1 + 10 + 100 = 111
*/
