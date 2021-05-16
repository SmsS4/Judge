#include <bits/stdc++.h>
using namespace std;
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define LL long long
#define rep1(i,a,b) for (int i = a;i <= b;i++)
#define rep2(i,a,b) for (int i = a;i >= b;i--)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define rei(x) scanf("%d",&x)
#define rel(x) scanf("%I64d",&x)
#define pri(x) printf("%d",x)
#define prl(x) printf("%I64d",x)
 
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
 
const int MAXN = 1e5+10;
const int dx[9] = {0,1,-1,0,0,-1,-1,1,1};
const int dy[9] = {0,0,0,-1,1,-1,1,-1,1};
const double pi = acos(-1.0);
 
int n,m;
int f[MAXN],num[MAXN],cnt[2];
int color[MAXN];
vector <int> g[MAXN];
queue <int> dl;
 
int ff(int x)
{
    if (f[x]==x) return x;
    else
        f[x] = ff(f[x]);
    return f[x];
}
 
int main()
{
    memset(color,255,sizeof color);
    rei(n);rei(m);
    rep1(i,1,n)
        f[i] = i,num[i] = 1;
    rep1(i,1,m)
    {
        int x,y;
        rei(x);rei(y);
        g[x].pb(y);
        g[y].pb(x);
        int r1 = ff(x),r2 = ff(y);
        if (r1!=r2)
        {
            f[r1]=r2;
            num[r2]+=num[r1];
        }
    }
    int ma = 1;
    LL ans = 0;
    rep1(i,1,n)
    {
        int r = ff(i);
        ma = max(ma,num[r]);
    }
    if (ma == 1)
    {
        printf("3 %lld\n",1LL*n*(n-1)*(n-2)/6);
        return 0;
    }
    else
        if (ma==2)
        {
            printf("2 %lld\n",1LL*(n-2)*m);
            return 0;
        }
        else
        {
            rep1(i,1,n)
                if (color[i]==-1)
                {
                    memset(cnt,0,sizeof cnt);
                    color[i] = 0;
                    cnt[0] = 1;
                    dl.push(i);
                    bool ok = true;
                    while (!dl.empty())
                    {
                        int x = dl.front();
                        dl.pop();
                        int len = g[x].size();
                        rep1(j,0,len-1)
                        {
                            int y = g[x][j];
                            if (y==x) continue;
                            if (color[y]==-1)
                            {
                                color[y] = 1-color[x];
                                cnt[color[y]]++;
                                dl.push(y);
                            }
                            else
                                if (color[y]==color[x])
                                {
                                    ok = false;
                                    break;
                                }
                        }
                        if (!ok) break;
                    }
                    if (!ok)
                    {
                        printf("0 1\n");
                        return 0;
                    }
                    if (cnt[0]>=2)
                        ans+=1LL*cnt[0]*(cnt[0]-1)/2;
                    if (cnt[1]>=2)
                        ans+=1LL*cnt[1]*(cnt[1]-1)/2;
                }
        }
    cout <<"1 "<< ans << endl;
    return 0;
}