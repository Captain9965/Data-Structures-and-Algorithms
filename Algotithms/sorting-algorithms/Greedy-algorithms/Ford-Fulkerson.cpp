/* Ford Fulkerson implementation in cpp:*/

#include "iostream"
#include "bits/stdc++.h"

#define V 6

using namespace std;

bool bfs(int ** residualGraph, int s, int t, int * parent){
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

int fordFulkerson(int ** graph, int s, int t){
    int u, v;

    int residualGraph[V][V];
    for (u = 0; u < V; u ++){
        for(v = 0; v < V ;v ++){
            residualGraph[u][v] = graph[u][v];
        }
    }
    
}