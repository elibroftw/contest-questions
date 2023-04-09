/*
A cyber security firm is building a team of hackers to take down a network of cybercriminals. The skill level of the ith hacker of team A is team_a[i] and of team B is team_b[i]. A team is considered strong if for each index i a hacker is selected either from team A or team B, and the skill levels of the selected team are non-decreaseing.

Given two arrays team_a and team_b of n integers each, choose two indices i and j such that the subarrays [team_a[i], team_a[i+1]... team_a[j]] and [team_b[i], team_b[i+1]... team_b[j]] can form a strong team. Find the maximum possible value of (j - 1 + 1). i.e. the length of the chosen subarray.

Given, n = 3, team_a = [5, 2, 4, 1] and team_b = [3, 6, 2, 2], the subarray would be [2, 4, 1] and [6, 2, 2] giving a strong team of [2, 2, 2]

Complete the function getMaxSubarrayLen which has the following parameters:
int team_a[n]: skill levels of team A
int team_b[n]: skill levels of taam B

Returns

int: the maximum subarray length that can be chosen to form a strong team

13/15
*/

#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'getMaxSubarrayLen' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY team_a
 *  2. INTEGER_ARRAY team_b
 */


int getMaxSubarrayLen(vector<int> team_a, vector<int> team_b) {
    size_t n = team_a.size();
    size_t max_len = 1;
    // i vs. j
    size_t prev_value = 0;
    // could do a DFS instead. Not in the mood
    for (size_t i = 0; i < n; i++) {
        for (size_t j = i; j < n; j++) {
            if (i == j) {
                prev_value = min(team_a.at(j), team_b.at(j));
            } else if (prev_value <= team_a.at(j) || prev_value <= team_b.at(j)) {
                // team_a or team_b maintains non-decreasing order
                // pick the player with the lower player skill level still >= previous player
                if (team_b[j] < prev_value) {
                    prev_value = team_a[j];
                }  else if (team_a[j] < prev_value || team_b[j] < team_a[j]) {
                    prev_value = team_b[j];
                } else {
                    prev_value = team_a[j];
                }
                if (j - i + 1 > max_len) max_len = j - i + 1;
            } else {
                if (team_a[j] >= prev_value && team_b[j] >= prev_value) {
                    i = j;
                }
                prev_value = 0;
                break;
            }
        }
    }
    return max_len;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string team_a_count_temp;
    getline(cin, team_a_count_temp);

    int team_a_count = stoi(ltrim(rtrim(team_a_count_temp)));

    vector<int> team_a(team_a_count);

    for (int i = 0; i < team_a_count; i++) {
        string team_a_item_temp;
        getline(cin, team_a_item_temp);

        int team_a_item = stoi(ltrim(rtrim(team_a_item_temp)));

        team_a[i] = team_a_item;
    }

    string team_b_count_temp;
    getline(cin, team_b_count_temp);

    int team_b_count = stoi(ltrim(rtrim(team_b_count_temp)));

    vector<int> team_b(team_b_count);

    for (int i = 0; i < team_b_count; i++) {
        string team_b_item_temp;
        getline(cin, team_b_item_temp);

        int team_b_item = stoi(ltrim(rtrim(team_b_item_temp)));

        team_b[i] = team_b_item;
    }

    int result = getMaxSubarrayLen(team_a, team_b);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
