#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;
void GenRandomGraphs(int NOEdge, int NOVertex)
{
   int i, j, edge[NOEdge][2], count;
   int degree[NOVertex];
   for(int k=0; k < NOVertex; k++) degree[k] = 0;
   i = 0;
   int situation;
   while(i < NOEdge)
   {
      edge[i][0] = rand()%NOVertex+1;
      edge[i][1] = rand()%NOVertex+1;
      situation = 1;
      //Print the connections of each vertex, irrespective of the direction.
      if(edge[i][0] == edge[i][1] || degree[edge[i][0]-1] > 0 || degree[edge[i][1]-1] > 0)
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
          degree[edge[i][0]-1]++;
          degree[edge[i][1]-1]++;
          cout << edge[i][0] << ' ' << edge[i][1] << "\n";
      }

      i++;
   }
}
int main(int argc, char* argv[]) {
    srand(stoi(argv[argc-1]));
    long int n = rand()%(99997)+3;
    long int m = rand()%(n/2) + 1;
    cout << n << ' ' << m << '\n';
    GenRandomGraphs(m, n);
}
// edges should be n/2 max

