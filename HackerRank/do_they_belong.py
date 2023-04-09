"""
Determine how two points relate to a triangle.

A triangle formed by the three points a(x1, y1), b(x2, y2) and c(x3, y3) is a non-degenerate triangle if the following rules are respected (|ab| is the length of the line between points a and b):


- |ab| + |bc| &gt; |ac|
- |bc| + |ac| &gt; |ab|
- |ab| + |ac| &gt; |bc|


A point belongs to a triangle if it lies somewhere on or inside the triangle. Given two points p = (xp, yp) and q = (xq, yq), return the correct scenario number:

-
0: If the triangle abc does not form a validnon-degenerate triangle.
-
1: If point p belongs to the triangle but point q does not.
-
2: If point q belongs to the triangle but point p does not.
-
3: If both points p and q belong to the triangle.
-
4: If neither point p nor point q belong to the triangle.


Example


```
1 = a(x1,y1): (2,2)
2 = b(x2,y2): (7,2)
3 = c(x3,y3): (5,4)
p = p(xp, yp): (4,3)
q = q(xq, yq): (7,4)
```

https://hrcdn.net/s3_pub/istreet-assets/mzOMunOfJVfoOClDgdxT9A/do_they_belong_example.svg


First, the triangle abc forms a valid non-degenerate triangle

- |ab| = 7 - 2 = 5. |bc| = sqrt((7-5)<sup>2</sup> + (4-2)<sup>2</sup>) = sqrt(2<sup>2</sup> + 2<sup>2</sup>)=sqrt(8) = 2.82.|ac| =sqrt((5 - 2)<sup>2</sup> + (4 - 2)<sup>2</sup>) = (3<sup>2 + </sup>2<sup>2</sup>)=sqrt(13) =3.6.
- |ab| + |bc| &gt; |ac| =&gt; 5 + 2.82 &gt; 3.6
- |bc| + |ac| &gt; |ab|=&gt; 2.82 +3.6 &gt; 5
- |ab| + |ac| &gt; |bc|=&gt; 5 +3.6 &gt; 2.82


Second, the point p(5, 4) belong to the triangle abc and the point q(7, 4) does not as show in the graphic above. So, the answer is 1.
Function Description
Complete the function pointsBelong  in the editor below.
pointsBelong has the following parameter(s):

int  x1, y1, x2, y2, x3, y3: integer coordinates of the three points that may create a valid triangle
int xp, yp, xq, yq: integer coordinates of the two points p and q

Returns:

int : an integer value that represents the scenario

The function must return one of the following integers:


- 0: If points (x[1], y[1]), (x[2], y[2]), and (x[3], y[3]) do not form a valid, <a href="https://en.wikipedia.org/wiki/Degeneracy_(mathematics)#Triangle" target="_blank" title="Wikipedia Definition of Triangle Degeneracy">non-degenerate</a> triangle.
- 1: If point p belongs to the triangle but point q does not.
- 2: If point q belongs to the triangle but point p does not.
- 3: If both points p and q belong to the triangle.
- 4: If neither point p nor point q belong to the triangle.

Constraints

- 0 ≤ x1, y1, x2, y2, x3, y3, xp, yp, xq, yq ≤ 2000

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

Each of the following values is an integer on its own line in the order given: x1, y1, x2, y2, x3, y3, xp, yp, xq, yq

Input Format

The first line contains an integer denoting x1.
The next line contains an integer denoting y1.
The next line contains an integer denoting x2.
The next line contains an integer denoting y2.
The next line contains an integer denoting x3.
The next line contains an integer denoting y3.
The next line contains an integer denoting xP.
The next line contains an integer denoting yP.
The next line contains an integer denoting xQ.
The next line contains an integer denoting yQ.

Sample Case 0

Sample Input 0

```
STDIN  Function
-----  --------
0→  (x1,y1) = (0,0)
0
2→  (x2,y2) = (2,0)
0
4→  (x3,y3) = (4,0)
0
2→  p = (xp,yp) = (2,0)
0
4→  q = (xq,yq)=(4,0)
0
```

Sample Output 0

```
0
```

Explanation 0

https://hrcdn.net/s3_pub/istreet-assets/u7De0fGOVii8dFGEHkh5Ig/do_they_belong_sample_0.svg

First, the lines do not form a validnon-degenerate triangle: The three points a, b, c lie on the same line, so it is impossible to form a triangle. The answer is 0.

Sample Case 1

Sample Input 1

```
STDIN  Function
-----  --------
3→ (x1,y1) =  (3, 1)
1
7→ (x2,y2) =  (7, 1)
1
5→ (x3,y3) =  (5, 5)
5
3→  p = (xp,yp) = (3, 1)
1
0→  q = (xq,yq) = (0, 0)
0
</pre>

<p class="section-title">Sample Output 1

<pre>1</pre>

<p class="section-title">Explanation 1

<img src="https://hrcdn.net/s3_pub/istreet-assets/hmnSiM3mmdnLRQS-CYTOFQ/do_they_belong_sample_1.svg" width="366" height="300">

First, the lines form a validnon-degenerate triangle, where a(3, 1), b(7, 1), and c(5, 5),


- |ab| = 7 -3 = 4. |bc| =sqrt(4<sup>2</sup> + 2<sup>2</sup>)=sqrt(20) =4.47.|ac| =sqrt(2<sup>2</sup> + 4<sup>2</sup>)=sqrt(20) =4.47.

- |ab| + |bc| &gt; |ac| =&gt; 4 + 4.47 &gt; 4.47

- |bc| + |ac| &gt; |ab|=&gt; 4.47 +4.47 &gt; 4
- |ab| + |ac| &gt; |bc|=&gt; 4 +4.47 &gt; 4.47



Second, the point p(3, 1) belongs to the triangle abc and the point q(0,0) does not. So, the answer is 1.
</div>
</details>

<details title="Click bar to open/close the example."><summary class="section-title">Sample Case 2</summary>

Sample Input 2

```
STDIN  Function
-----  --------
3→ (x1,y1) =  (3, 1)
1
7→ (x2,y2) =  (7, 1)
1
5→ (x3,y3) =  (5, 5)
5
1→  p = (xp,yp) =  =(1, 1)
1
4→  q = (xq,yq) = (4, 3)
3
```

Sample Output 2

```2```

Explanation 2
https://hrcdn.net/s3_pub/istreet-assets/BlJs8knYGNaco7wMEXhVVw/do_they_belong_sample_2.svg

First, the lines form a validnon-degenerate triangle, where a(3, 1), b(7, 1), and c(5, 5),

Second, the point q(4,3) belongs to the triangle but point p(1,1) does not. So, the answer is 2.

Sample Case 3

Sample Input 3

```
STDIN  Function
-----  --------
3→  (x1,y1) = (3, 1)
1
7→  (x2,y2) = (7, 1)
1
5→  (x3,y3) = (5, 5)
5
5→  p = (xp,yp) = (5, 2)
2
6→  q = (xq,yq) = (6, 3)
3
```

Sample Output 3

```
3
```

Explanation 3

https://hrcdn.net/s3_pub/istreet-assets/hylmLSxTY3uxEdNMOJ5dZw/do_they_belong_sample_3.svg"
First, the lines form a validnon-degenerate triangle, where a(3, 1), b(7, 1), and c(5, 5),

Second, both the points p(5,2) and q(6,3) belong to the triangle. So, the answer is 3.

Sample Case 4

Sample Input 4

```
STDIN  Function
-----  --------
3→ (x1,y1) =  (3, 1)
1
7→ (x2,y2) =  (7, 1)
1
5→ (x3,y3) =  (5, 5)
5
1→ p = (xp,yp) = (1, 1)
1
2→ q = (xq,yq) = (2, 2)
2
```

Sample Output 4

```
4
```

Explanation 4

https://hrcdn.net/s3_pub/istreet-assets/PbreJ_bJfgyAKpRArObF8g/do_they_belong_sample_4.svg

First, the lines form a validnon-degenerate triangle, where a(3, 1), b(7, 1), and c(5, 5),

Second, neither the points p(1,1) nor the point q(2,2) belong to the triangle. So, the answer is 4.
"""
import math

def find_m_b(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return (m, b)


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # confirm non-degen
    ab = get_distance(x1, y1, x2, y2)
    bc = get_distance(x2, y2, x3, y3)
    ac = get_distance(x1, y1, x3, y3)
    if ab + bc <= ac or bc + ac <= ab or ab + ac <= bc:
        return 0
    pin = True
    qin = True
    # return whether point is within each side length
    # find y = mx + b for each pair

    mab, bab = find_m_b(x1, y1, x2, y2)
    vertex_under = mab * x3 + bab > y3
    # if any point is on the side length (y=mx+b match), set to same as vertex_under
    p_under = mab * xp + bab
    p_under = vertex_under if p_under == yp else p_under > yp
    q_under = mab * xq + bab
    q_under = vertex_under if q_under == yq else q_under > yq
    if p_under != vertex_under:
        pin = False
    if q_under != vertex_under:
        qin = False

    mbc, bbc = find_m_b(x2, y2, x3, y3)
    vertex_under = mbc * x1 + bbc > y1
    # if any point is on the side length (y=mx+b match), set to same as vertex_under
    p_under = mbc * xp + bbc
    p_under = vertex_under if p_under == yp else p_under > yp
    q_under = mbc * xq + bbc
    q_under = vertex_under if q_under == yq else q_under > yq
    if p_under != vertex_under:
        pin = False
    if q_under != vertex_under:
        qin = False

    mac, bac = find_m_b(x1, y1, x3, y3)
    vertex_under = mac * x2 + bac > y2
    # if any point is on the side length (y=mx+b match), set to same as vertex_under
    p_under = mac * xp + bac
    p_under = vertex_under if p_under == yp else p_under > yp
    q_under = mac * xq + bac
    q_under = vertex_under if q_under == yq else q_under > yq
    if p_under != vertex_under:
        pin = False
    if q_under != vertex_under:
        qin = False


    if pin and not qin:
        return 1
    if qin and not pin:
        return 2
    if qin and pin:
        return 3
    if not pin and not qin:
        return 4
