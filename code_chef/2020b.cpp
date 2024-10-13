#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;  // Read number of test cases

    while (t--) {
        long long k;
        cin >> k;  // Read the value of k

        // The smallest n such that there are exactly k perfect squares is k^2
        long long n = k * k;
        cout << n << endl;
    }

    return 0;
}