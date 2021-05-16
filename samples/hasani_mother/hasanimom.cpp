#include <limits.h>
#include <stdio.h>
#include <iostream>
#include <vector>
#define int long long
using namespace std;

class Graph
{
    int n, edges;
    vector<pair<int, int> > *adj;
    int minDistance(int dist[], bool sptSet[]);

public:
    Graph(int n, int edges); // Constructor
    void addEdge(int u, int v, int w); // To add edge
    void dijkstra(int src);

};

Graph::Graph(int n, int edges)
{
    this->n = n+2;
    this->edges = edges;
    adj = new vector<pair<int, int> >[n+2];
}

void Graph::addEdge(int u, int v, int w)
{
    adj[u].push_back({v, w});
    adj[v].push_back({u, w});

}




int Graph::minDistance(int dist[], bool sptSet[])
{
	int min = LONG_LONG_MAX, min_index;

	for (int v = 0; v < n; v++)
		if (sptSet[v] == false && dist[v] <= min)
			min = dist[v], min_index = v;

	return min_index;
}

void Graph::dijkstra(int src)
{
	int dist[n]; // dist[i] will hold the shortest
	// distance from src to i

	bool sptSet[n]; // sptSet[i] will be true if vertex i is included in shortest
	// path tree or shortest distance from src to i is finalized

	// Initialize all distances as INFINITE and stpSet[] as false
	for (int i = 0; i < n; i++)
		dist[i] = LONG_LONG_MAX, sptSet[i] = false;

	// Distance of source vertex from itself is always 0
	dist[src] = 0;

	// Find shortest path for all vertices
	for (int count = 0; count < n - 1; count++) {
		// Pick the minimum distance vertex from the set of vertices not
		// yet processed. u is always equal to src in the first iteration.
		int u = minDistance(dist, sptSet);

		// Mark the picked vertex as processed
		sptSet[u] = true;

		// Update dist value of the adjacent vertices of the picked vertex.
		for (auto v : adj[u]){
		     if(dist[u] != LONG_LONG_MAX && dist[u] + v.second < dist[v.first])
                            dist[v.first] = dist[u] + v.second;
		}


	}

	if(dist[n-1] == LONG_LONG_MAX){
        cout << -1 << endl;
    }else{
        cout << dist[n-1] << endl;
    }
}

int32_t main()
{
    int n, m;
    cin >> n >> m;
    Graph g(n, m);

    for(int i = 0; i < m; i++){
        int a, b, w;
        cin >> a >>b >> w;
        g.addEdge(a, b, w);
    }

	g.dijkstra(0);

	return 0;
}
