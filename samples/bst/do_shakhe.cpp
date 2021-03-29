#include<bits/stdc++.h>
using namespace std;


int main(int argc, char* argv[]) {
    srand(stoi(argv[argc-1]));
    int n = stoi(argv[1]);
    int q = stoi(argv[2]);
    cout << n << ' ' << q << '\n';
    for (int i = 0; i < n; i++)
    {
        if (i%2 == 0)
            cout << 5+n+q+i;
        else
            cout << 5+n+q-i;

        if(i != n-1) cout << ' ';
    }
    cout << '\n';
    for (int i = 0; i < q; i++)
    {
        if (i%2 == 0)
            cout << 5+2*n+q+i << '\n';
        else
            cout << 5+q-i << '\n';
    }
}