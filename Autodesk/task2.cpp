// you can use includes, for example:
// #include <algorithm>
#include <algorithm>
#include <unordered_set>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
using namespace std;

int solution(string &S) {
    // write your code in C++14 (g++ 6.2.0)
    int num_b = 0;
    int num_a = 0;
    int num_l = 0;
    int num_o = 0;
    int num_n = 0;
    // B A L L O O N
    for (auto &&letter : S) {
        if (letter == 'B') ++num_b;
        else if (letter == 'A') ++num_a;
        else if (letter == 'L') ++num_l;
        else if (letter == 'O') ++num_o;
        else if (letter == 'N') ++num_n;
    }
    // use division to normalize L and O for requiring 2
    num_l /= 2;
    num_o /= 2;
    // should have used this function for the last task...
    return min({num_b, num_a, num_l, num_o, num_n});
}
