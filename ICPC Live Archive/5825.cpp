// author: ELijah Lopez
// https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=530&page=show_problem&problem=3836

#include <array>
#include <iostream>
#include <unordered_map>
#include <unordered_set>

using std::cin;
using std::cout;
using std::array;
using std::pair;
using std::unordered_map;
using std::unordered_set;
using std::ios_base;

#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL)
#define MAX_SIZE 1000000  // max is 1,000,000

typedef pair<int, int> pii;

int solve(int n, array<int, MAX_SIZE>& integers) {
  int valid_seqs = n;
  unordered_map<int, pii> sum_cache;
  unordered_set<int> skip_cache;

  for (int i = 0; i < n; i++) {
    int integer = integers[i];
    if (skip_cache.count(i)) break;
    if (integer < 0) {
      int min_index = i - n;
      int temp_sum = integer;
      int j = i - 1;
      valid_seqs--;
      while (j > min_index) {
        int temp_num = integers[j];
        int pos_j = (j + n) % n;
        if (temp_num < 0) {
          if (sum_cache.count(pos_j)) {
            temp_sum += sum_cache.at(pos_j).second;
            int temp_j = sum_cache.at(pos_j).first;
            if (temp_j > j) {
              pos_j = temp_j;
              j = temp_j - n;
            } else {
              pos_j = temp_j + n;
              j = temp_j;
            }
            temp_num = integers[j];
          }
          skip_cache.insert(pos_j);
          temp_sum += temp_num;
          if (temp_sum >= 0) {
            sum_cache[i] = pii(j, temp_sum - temp_num);
            break;
          }
          valid_seqs--;
          j--;
        }
      }
    }
  }
  return valid_seqs;
}

int main(int argc, const char* argv[]) {
  fast_cin();
  int n;
  while (cin >> n, n) {
    if (!n) break;
    array<int, MAX_SIZE> integers;
    for (int i = 0; i < n; i++) {
      cin >> integers[i];
    }
    cout << solve(n, integers) << "\n";
  }
  return 0;
}
