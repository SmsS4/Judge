#include<bits/stdc++.h>
using namespace std;

const int MAX_N = 100;
int a[10000];

int main(int argc, char *argv[]) {
    srand(stoi(argv[argc-1]));
    int n  = stoi(argv[1]);
    int m = stoi(argv[2]);
    int t = stoi(argv[3]);
    cout << n << ' ' << m << '\n';
    for (int i = 0; i < n; i++) {
        a[i] = rand()%MAX_N+1;
    }
    sort(a, a+n);
        for (int i = 0; i < n; i++) cout << a[i] << ' ';
    cout << '\n';
    for (int i = 0; i < n; i++) {
        if(t == 1){
            cout << 1 << ' ';
        }else if(t == 2){
            cout << 2 << ' ';
        }else {
            cout << i%2+1 << ' ';
        }
    }
    cout << '\n';

}