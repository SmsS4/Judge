#include<bits/stdc++.h>
using namespace std ;

const int max_lg = 30;
const int maxs = 200000*(max_lg+1) ;
multiset<int> s ;
int trie[maxs][2] ;
int zir[maxs] ;
int sz ;

void trieRef(int y, int d){

    int w = 0 ;
    for(int i = max_lg; i >= 0; i--){

        int x = y&(1<<i) ;
        if(x > 0)
            x = 1 ;
        if(!trie[w][x]){

            trie[w][x] = ++sz ;

        }
        zir[w]+=d ;

        w = trie[w][x] ;

    }
    zir[w]+=d ;

}

void trieDel(int x){

    trieRef(x, -1) ;

}
void trieAdd(int x){

    trieRef(x, +1) ;

}

int trieXor(int y){

    int ans = 0 ;
    int w = 0 ;
    for(int i = max_lg; i >= 0; i--){

        int x = y&(1<<i) ;
        if(x > 0)
            x = 1 ;
        x = 1 - x ;
        if(!trie[w][x]){

            trie[w][x] = ++sz ;

        }

        if(!zir[trie[w][x]]){

            x = 1-x ;

        }

        ans += (1<<i)*x ;
        w = trie[w][x] ;

    }

    return ans ;

}

int main(){
    int n ;

    cin >> n ;
    trieAdd(0) ;
    for(int i = 0; i < n; i++){

        char q ;
        int x ;
        cin >> q >> x ;
        if(q == '+'){

            trieAdd(x) ;

        }else if(q == '-'){

            trieDel(x) ;

        }else {

            int y = trieXor(x) ;
            cout << (x ^ y) << endl ;

        }

    }

}