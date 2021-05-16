#include<bits/stdc++.h>
using namespace std;
#define int long long
int32_t main(int argc, char* argv[]) {
    srand(stoi(argv[argc-1]));
    int n = stoi(argv[1]);
    n = rand()%(n/2)+(n/2);
    int m = stoi(argv[2]);
    int max_m = min(m, n*(n+1)/4);
    m = rand()%(max_m/2) + max_m/2;
    int max_w = stoi(argv[3]);
    int connected = stoi(argv[4]);
    max_w --;
    if (connected){
        m = max(m , n);
    }
    cout << n << ' ' << m << '\n';
    n += 2;
    set<pair<int, int>> edges;
    if (connected == 1){
        int t = rand()%(m-1) + 1;
        int last = 0;
        set<int> seen;
        seen.insert(last);
        for (int i = 0; i < t; i++){
            int x, w;
            x = rand()%n;
            w = rand()%max_w+1;
            if(seen.find(x) != seen.end() || i == t-1){
                x = n-1;
            }
            edges.insert({min(last, x), max(last, x)});
            cout << last << ' ' << x << ' ' << w << '\n';
            last = x;
            seen.insert(last);
            if (last == n-1){
                m -= i+1;
                t = 0;
                break;
            }

        }
        m -= t;
    }
    int i = m;
    while(i){
        int x, y, w;
        if (connected != -1){
            x = rand()%n;
            y = rand()%n;
        }else{
            x = rand()%(n/2);
            y = rand()%(n/2);
            if (rand()%2){
                x += (n+1)/2;
                y += (n+1)/2;
            }

        }
        if (x > y) swap(x, y);
        w = rand()%max_w+1;
        if (x == y) continue;
        if (edges.find({x, y}) != edges.end()) continue;
        edges.insert({x, y});
        cout << x << ' ' << y << ' ' << w << '\n';
        i --;
    }
}