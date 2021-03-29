#include<bits/stdc++.h>
using namespace std;


int main(int argc, char* argv[]) {
    srand(stoi(argv[argc-1]));
    int n = stoi(argv[1]);
    int q = stoi(argv[2]);
    cout << n << ' ' << q << '\n';
    for (int i = 0; i < n; i++){
        cout << i+1;
        if(i != n-1) cout << ' ';

    }
    cout << '\n';
    for (int i = 0; i < q; i++) cout << 1+i+n << '\n';
}