#include <unordered_set>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int out = 1;
    unordered_set<int> visited;

    for (auto &&integer : A) {
        visited.insert(integer);
        while (visited.count(out)) {
            ++out;
        }
    }
    return out;
}
