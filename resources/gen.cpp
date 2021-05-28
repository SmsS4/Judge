#include<bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {
    srand(stoi(argv[argc-1]));
    int n  = stoi(argv[1]);
    int m = stoi(argv[2]);
    cout << rand()%n << ' ' << rand()%m << '\n';
}