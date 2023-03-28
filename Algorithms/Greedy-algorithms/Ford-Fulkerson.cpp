/* Ford Fulkerson implementation in cpp:*/

#include "iostream"
#include "bits/stdc++.h"

#define V 6

using namespace std;

bool bfs(int residualGraph[V][V], int s, int t, int * parent){
    bool visited[V];
    memset(visited, 0, sizeof(visited));

    queue<int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;

    while(!q.empty()){
        int u = q.front();
        q.pop();

        for (int v = 0; v < V; v ++){
            if (visited[v] == false && residualGraph[u][v] > 0){
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }

    }
    return (visited[t] == true);
}

/* applying ford Fulkerson algorithm:*/

int fordFulkerson(int graph[V][V], int s, int t){
    int u, v;

    int residualGraph[V][V];
    for (u = 0; u < V; u ++){
        for(v = 0; v < V ;v ++){
            residualGraph[u][v] = graph[u][v];
        }
    }

    int parent[V];
    int maxFlow = 0;

    /* updating the residual values in the graph:*/
    while(bfs(residualGraph, s, t, parent)){
        int pathFlow = INT_MAX;
        for (v = t; v != s; v = parent[v]){
            u = parent[v];
            pathFlow = min(pathFlow, residualGraph[u][v]);
        }

        for (v = t; v != s; v = parent[v]){
            u = parent[v];
            residualGraph[u][v] -= pathFlow;
            residualGraph[v][u] += pathFlow;
        }

        /* adding the path flows:*/
        maxFlow += pathFlow;
    }

    return maxFlow;
    
}

int main(){
    int graph[V][V] = {{0, 8, 0, 0, 3, 0},
                        {0, 0, 9, 0, 0, 0},
                        {0, 0, 0, 0, 7, 2},
                        {0, 0, 0, 0, 0, 5},
                        {0, 0, 7, 4, 0, 0},
                        {0, 0, 0, 0, 0, 0}};
    cout << "Max flow is -> " << fordFulkerson(graph, 0, 5) << endl;
    return 0;
}