#include <unordered_set>
#include <vector>

using namespace std;

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(string &S) {
    // write your code in C++14 (g++ 6.2.0)
    int pointing_up = 0;
    int pointing_down = 0;
    int pointing_left = 0;
    int pointing_right = 0;
    // count directions
    for (auto &&arrow : S) {
        if (arrow == '^') ++pointing_up;
        else if (arrow == 'v') ++pointing_down;
        else if (arrow == '<') ++pointing_left;
        else /* (arrow == '>') */ ++pointing_right;
    }
    // figure out which direction is the most prominent
    // sum of rest will be the smallest then
    if (pointing_up >= pointing_down && pointing_up >= pointing_right && pointing_up >= pointing_left) {
        return pointing_down + pointing_left + pointing_right;
    } else if (pointing_down >= pointing_right && pointing_down >= pointing_left) {
        return pointing_up + pointing_left + pointing_right;
    } else if (pointing_right >= pointing_left) {
        return pointing_up + pointing_down + pointing_left;
    }
    // arrows pointing left is max
    return pointing_up + pointing_down + pointing_right;
}
