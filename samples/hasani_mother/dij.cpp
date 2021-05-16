#include<bits/stdc++.h>
using namespace std;
#define int long long
const int MAX_N = 1e5+100;
const int INF = 1e18;
vector<pair<int, int>> adj[MAX_N];
int d[MAX_N];

int32_t main() {
    ios::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    n ++;
    fill(d, d+n+1, INF);
    for (int i = 0; i < m; i++){
        int x, y, w;
        cin >> x >> y >> w;
        adj[x].push_back({y, w});
        adj[y].push_back({x, w});
    }
    set<pair<int, int> > st;
    st.insert({0, 0});
    d[0] = 0;
    while(st.size()) {
        int x = st.begin()->second;
        st.erase(st.begin());
        for (auto y : adj[x]) if(d[x] + y.second < d[y.first]){
            st.erase({d[y.first], y.first});
            d[y.first] = d[x] + y.second;
            st.insert({d[y.first], y.first});

        }
    }
    if(d[n] != INF) cout << d[n] << '\n';
    else cout << -1 << '\n';
}