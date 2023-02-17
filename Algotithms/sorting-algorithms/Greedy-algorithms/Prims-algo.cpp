#include "bits/stdc++.h"

using namespace std;

#define V 5

int minKey(int * key, bool * mstSet){
    int min = INT_MAX;
    int minIndex;
    for (int v = 0; v < V; v++){
        if (mstSet[v] == false && key[v] < min){
            min = key[v];
            minIndex = v;
        }
    }

    return minIndex;

}

void printMst(int parent[], int graph[V][V]){
    cout << "Edge \t\t Weight" << endl;
    for (int i = 1; i < V; i++){
        cout << parent[i] << "-" << i << "\t" << graph[i][parent[i]] << endl;
    }
}

void primMst(int graph[V][V]){
    int parent[V];
    int key[V];
    bool mstSet[V];

    for (int i = 0; i < V; i++){
        key[i] = INT_MAX;
        mstSet[i] = false;
    }

    key[0] = 0;
    parent[0] = -1;


    /* The mst will have V vertices: */

    for (int count = 0; count < V - 1; count ++){
        int u = minKey(key, mstSet);
        mstSet[u] = true;
        /* update the key value and the  parent index of the adjacent vertex:*/

        for (int v = 0; v < V; v++){
            if(graph[u][v] && mstSet[v] == false && graph[u][v] < key[v]){
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }

    }

    printMst(parent, graph);
}


/* driver code: */

int main(){
    int graph[V][V] = { { 0, 2, 0, 6, 0 },
                        { 2, 0, 3, 8, 5 },
                        { 0, 3, 0, 0, 7 },
                        { 6, 8, 0, 0, 9 },
                        { 0, 5, 7, 9, 0 } };
    primMst(graph);
    return 0;
    
}
