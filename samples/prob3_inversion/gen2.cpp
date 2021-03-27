#include<bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {
    srand(stoi(argv[argc-1])+1);
    int n  = stoi(argv[1]);
    int m = stoi(argv[2]);
    cout << n << '\n';
    for (int i = 0; i < n/2; i++) {
        cout << m << ' ';
    }
    for (int i = n/2; i < n; i++) {
        cout << 1 << ' ';
    }
    cout << '\n';
}