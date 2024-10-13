#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> nums(n);
        for (int i = 0; i < n; ++i) {
            if (!(cin >> nums[i])) {
                cerr << "Invalid input" << endl;
                return 1;
            }
        }

        unordered_map<int, int> count;
        vector<int> unique_indexes;
        vector<int> uniques;

        for (int i = 0; i < n; ++i) {
            count[nums[i]]++;
        }

        for (int i = 0; i < n; ++i) {
            if (count[nums[i]] == 1) {
                unique_indexes.push_back(i + 1);
                uniques.push_back(nums[i]);
            }
        }

        if (unique_indexes.empty()) {
            cout << -1 << endl;
        } else {
            auto min_it = min_element(uniques.begin(), uniques.end());
            int min_index = distance(uniques.begin(), min_it);
            cout << unique_indexes[min_index] << endl;
        }
    }

    return 0;
}