#include <iostream>

using namespace std;

#include <cmath>
#include <vector>

bool is_prime(int x) {
    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0)
            return false;
    }
    return true;
}

int count9Divisors(int b) {
    int count1 = 0;
    int count2 = 0;
    // 质数的八次方
    double small_b = pow((double) b, 0.125);
    for (int i = 2; i <= small_b; i++) {
        if (is_prime(i)) {
            count1++;
        }
    }
    //cout << "count 1:" << count1 <<endl;
    vector<int> list;
    for (int i = 2; i <= sqrt(b); i++) {
        if (is_prime(i)) {
            list.push_back(i);
        }
    }
    for (int i = 0; i < list.size(); i++) {
        for (int j = i + 1; j < list.size(); j++) {
            if (pow((double) list[i], 2.0) * pow((double) list[j], 2.0) < b) {
                count2++;
            } else {
                break;
            }
        }
    }
    return count2 + count1;
}

int main() {
    int b, num;
    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> b;
        cout << count9Divisors(b) << endl;
    }
    return 0;
}