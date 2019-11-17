#include <iostream>
#include <iomanip>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL)

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

// CONSTANTS GO UNDER HERE
// LESSON LEARNED: store every computation to a map

int main() {
    fast_cin();
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        int n, m, q;
        set <int> torn_out_set;
        map <int, int> duplicate_reader;
        cin >> n >> m >> q;
        for (int j = 0; j < m; j++)
        {
            int page;
            cin >> page;
            torn_out_set.insert(page - 1);
        }
        ll pages_read = 0;
        for (int r = 0; r < q; r++)
        {
            int reader; 
            cin >> reader;
            if (!duplicate_reader.count(reader)){
                int reader_read = 0;
                for (int pr = reader - 1; pr < n; pr += reader)
                {
                    if(!torn_out_set.count(pr)) {
                        reader_read ++;
                    }
                }
                duplicate_reader[reader] = reader_read;
            }
            pages_read += duplicate_reader[reader];
        }
        cout << "Case #" << i << ": " << pages_read << '\n';
    }
    return 0;
}