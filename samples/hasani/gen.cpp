#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <string>

using namespace std;

void GenRandomGraphs(long long int NOEdge, long int NOVertex)
{
   long long int i, j, edge[NOEdge][2], count;
   i = 0;
   int situation;
   while(i < NOEdge)
   {
      edge[i][0] = rand()%NOVertex+1;
      edge[i][1] = rand()%NOVertex+1;
      situation = 1;
      //Print the connections of each vertex, irrespective of the direction.
      if(edge[i][0] == edge[i][1])
         continue;
      else
      {
         for(j = 0; j < i; j++)
         {
            if((edge[i][0] == edge[j][0] &&
            edge[i][1] == edge[j][1]) || (edge[i][0] == edge[j][1] &&
            edge[i][1] == edge[j][0]))
            {
                i--;
                situation = 0;
            }

         }
      }
      if(situation == 1)
      {
          cout << edge[i][0] << ' ' << edge[i][1] << "\n";
      }

      i++;
   }
}
int main(int argc, char* argv[]) {
    srand(stoi(argv[argc-1]));
    /*int n = stoi(argv[1]);
    int m = stoi(argv[2]);
    int max_ai = stoi(argv[3]);*/
    long int n = rand()%99997 + 3;
    int max_edge = min(100000ll, 1ll*n*(n-1)/2);
    long long int m = rand()%(max_edge)+1;
    cout << n << ' ' << m << '\n';
    GenRandomGraphs(m, n);
}
