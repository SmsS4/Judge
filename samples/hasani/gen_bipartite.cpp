#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <stdio.h>


using namespace std;
const int MAX_N = 100000;
long long int edges[MAX_N][2];

int main(int argc, char* argv[]) {
    srand(time(0));
    //int m = rand()%500+1;
    long int n = rand()%(99997)+3;
    long int m = rand()%(n/2) + 1;
    long long int edge = rand()%min(100000ll, (1ll*m*(n-m)/2) + 1);


    cout << n << ' ' << edge << '\n';

    long long int i=0;
    long long int j;
    int situation;

    while (i < edge){
        edges[i][0] = rand()%(n-m) + 1;
        edges[i][1] = (rand()%m) + 1 + n - m;
        situation = 1;

        if(edges[i][0] == edges[i][1])
            continue;
        else{
            for(j = 0; j < i; j++)
            {
                if((edges[i][0] == edges[j][0] &&
                edges[i][1] == edges[j][1]) || (edges[i][0] == edges[j][1] &&
                edges[i][1] == edges[j][0]))
                {
                    i--;
                    situation = 0;
                }

            }
        }
        if(situation ==1)
            cout << edges[i][0] << ' ' << edges[i][1] << '\n';
        i++;
    }
   ///GenRandomGraphs(m, n,edge);
}

