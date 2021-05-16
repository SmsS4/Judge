#include<bits/stdc++.h>
using namespace std;

const int MAX_N = 1e5+10;
vector<int> adj[MAX_N];
bool seen[MAX_N];
int h[MAX_N];

pair<int, int> dfs(int root, int high){
    h[root] = high;
    pair<int, int> res = {1, 0};
    for (auto x : adj[root]){
        if (h[x] == 0){
            pair<int, int> child = dfs(x, high+1);
            res.first += child.second;
            res.second += child.first;
        }else if(h[x]%2 == h[root]%2){
            cout << 0 << ' ' << 1 << '\n';
            exit(0);
        }
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    long long n, m;
    cin >> n >> m;
    if (m == 0){
        cout << 3 << ' ' << (n*(n-1)*(n-2)/6) << '\n';
        return 0;
    }
    for (int i = 0; i < m; i++){
        int x, y; cin >> x >> y; x--, y--;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    long long ans = 0;
    for (int i = 0; i < n; i++){
        if(h[i] == 0){
            pair<int, int> res = dfs(i, 1);
            if(!res.first || !res.second){
                continue;
            }
            ans += ((long long)res.first*(res.first-1)/2);
            ans += ((long long)res.second*(res.second-1)/2);

        }
    }
    if(ans) cout << 1 << ' ' << ans << '\n';
    else cout << 2 << ' ' << m*(n-2) << '\n';

}