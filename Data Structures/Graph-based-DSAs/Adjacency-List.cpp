/* Adjacency List in cpp*/

#include "bits/stdc++.h"

using namespace std;

void add_edge(vector<int> adj[], int s, int d){
    adj[s].push_back(d);
    adj[d].push_back(s);
}

void print_graph(vector<int> adj[], int V){
    for (int d = 0; d < V; ++d){
        cout << "\n vertex" << d << ":";
        for (auto x: adj[d]){
            cout << "->" << x;
        }
        cout <<endl;
    }
}

int main(){
    int V = 5;

    vector<int> graph[V];
    add_edge(graph, 0, 1);
    add_edge(graph, 0, 2);
    add_edge(graph, 0, 3);
    add_edge(graph, 1, 2);

    print_graph(graph, V);
}