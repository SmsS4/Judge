#include<bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {
    srand(stoi(argv[argc-1])+1);
    int n  = stoi(argv[1]);
    int m = stoi(argv[2]);
    cout << n << '\n';
    for (int i = 0; i < n; i++) {
        cout << 1+rand()%m << ' ';
    }
    cout << '\n';
}