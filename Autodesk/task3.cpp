#include <algorithm>
#include <string>
#include <unordered_set>

using namespace std;

int solution(string &S) {
    // write your code in C++14 (g++ 6.2.0)
    // iterate a starting char from left to right
    // iterate again for ending char
    // stop once we got a balanced fragment
    // check if its the smallest encountered so far
    // repeat
    int frag_len = -1;
    unordered_set<char> char_required;
    unordered_set<char> visited;
    for (size_t start = 0; start < S.length(); start++) {
        char_required.clear();
        visited.clear();

        char ch = S.at(start);

        visited.insert(ch);
        if (islower(ch)) {
            char_required.insert(toupper(ch));
        } else {
            char_required.insert(tolower(ch));
        }
        for (size_t end = start; end < S.length(); end++) {
            ch = S.at(end);
            // we only care if we have never encountered the char
            if (!visited.count(ch)) {
                visited.insert(ch);
                if (char_required.count(ch)) {
                    // char improves balance
                    char_required.erase(ch);
                } else if (islower(ch)) {
                    // char needs (U) to be balanced
                    char_required.insert(toupper(ch));
                } else {
                    // char needs (l) to be balanced
                    char_required.insert(tolower(ch));
                }
                if (char_required.empty()) {
                    // no more balancing needed
                    int substrlen = end - start + 1;
                    if (frag_len == -1 || substrlen < frag_len) {
                        frag_len = substrlen;
                    }
                    break;
                }
            }
        }
    }
    return frag_len;
}
