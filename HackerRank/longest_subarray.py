"""
<div style="display:none;font-size:1px;color:#333333;line-height:1px;overflow:hidden;">Find the length of the longest subarray whose elements sum to a number less than <em>k</em>.</div>

<p>A subarray of array <em>a</em> is defined as a contiguous block of <em>a</em>'s elements having a length that is less than or equal to the length of the array. For example, the subarrays of array <em>a = [1, 2, 3]</em> are <em>[1]</em>, <em>[2]</em>, <em>[3],</em>&nbsp;<em>[1, 2]</em>, <em>[2, 3]</em>, and <em>[1, 2, 3]</em>. Given an integer, <em>k = 3,</em> the subarrays having elements that sum to a number <em>≤ k</em> are <em>[1]</em>, <em>[2]</em>, and <em>[1, 2]</em>. The <em>longest</em> of these subarrays is <em>[1, 2]</em>, which has a length of <em>2</em>. Given an array, <em>a</em>, determine its longest subarray that sums to less than or equal to a given value <em>k</em>.</p>

<p>&nbsp;</p>

<p><strong>Function Description </strong></p>

<p>Complete the function <em>maxLength</em> in the editor below. The function must return an integer that represents the length of the longest subarray of <em>a</em> that sums to a number ≤ <em>k</em>.</p>

<p>&nbsp;</p>

<p>maxLength has the following parameter(s):</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;<em>a[a[0],...a[n-1]]:</em>&nbsp; an array of integers</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;<em>k:</em> an integer</p>

<p>&nbsp;</p>

<p><strong>Constraints</strong></p>

<ul>
	<li><em>1 ≤ n ≤ 10<sup>5</sup></em></li>
	<li><em>1 ≤ a[i] ≤ 10<sup>3</sup></em></li>
	<li><em>1 ≤ k ≤ 10<sup>9</sup></em></li>
</ul>

<p>&nbsp;</p>
<!-- <StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details><summary class="section-title">Input Format For Custom Testing</summary>

<div class="collapsable-details">
<p>Input from stdin will be processed as follows and passed to the function.</p>

<p>&nbsp;</p>

<p>The first line contains a single integer, <em>n</em>, that denotes the number of elements in array <em>a</em>.</p>

<p>Each line <em>i</em> of the <em>n</em> subsequent lines (where <em>0 ≤ i &lt; n</em>) contains an integer that describes element <em>a[i]</em>.</p>

<p>The last line contains an integer, <em>k</em>.</p>

<p>&nbsp;</p>
</div>
</details>
<!-- </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details open="open"><summary class="section-title">Sample Case 0</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing</p>

<p><strong>Sample Input 0</strong></p>

<pre>3
1
2
3
4</pre>

<p>&nbsp;</p>

<p><strong>Sample Output 0</strong></p>

<pre>2
</pre>

<p>&nbsp;</p>

<p><strong>Explanation 0</strong></p>

<p>The subarrays of <em>[1, 2, 3]</em> having elements that sum to a number <em>≤ (k = 4)</em> are <em>[1]</em>, <em>[2]</em>, <em>[3]</em>, and <em>[1, 2]</em>. The longest of these is <em>[1, 2]</em>, which has a length of <em>2</em>. Return <em>2</em> as the answer.</p>

<p>&nbsp;</p>
</div>
</details>

<details><summary class="section-title">Sample Case 1</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing</p>

<p><strong>Sample Input 1</strong></p>

<pre>4
3
1
2
1
4</pre>

<p>&nbsp;</p>

<p><strong>Sample Output 1</strong></p>

<pre>3</pre>

<p>&nbsp;</p>

<p><strong>Explanation 1</strong></p>

<p>The subarrays of <em>[3, 1, 2, 1]</em> having elements that sum to a number <em>≤ (k = 4)</em> are <em>[3]</em>, <em>[1]</em>, <em>[2]</em>, <em>[1]</em>, <em>[3, 1]</em>, <em>[1, 2]</em>, <em>[2, 1]</em>, and <em>[1, 2, 1]</em>. The longest of these is <em>[1, 2, 1]</em>, which has a length of <em>3</em>. Return <em>3</em> as the answer.</p>

<p>&nbsp;</p>
</div>
</details>
"""


def maxLength(a, k):
    n = len(a)
    sums = [0]
    for i in range(1, n+1):
        sums.append(sums[-1] + a[i - 1])
    start, end, max_len = 0, 0, 0
    while end < n:
        if sums[end + 1] - sums[start] <= k:
            max_len = max(max_len, end - start + 1)
            end += 1
        else:
            start += 1
    return max_len
