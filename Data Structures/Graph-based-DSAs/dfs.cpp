#include "iostream"
#include "bits/stdc++.h"

using namespace std;

class Graph{
    public:
        Graph(int V);
        void add_edge(int src, int dest);
        void DFS(int vertex);
    private:
        int numVertices;
        list<int> *adjList;
        bool *visited;
};

Graph::Graph(int V){
    numVertices = V;
    adjList = new list <int> [numVertices];
    visited = new bool[numVertices];   
}

void Graph::add_edge(int src, int dest){
    adjList[src].push_front(dest);
}

void Graph::DFS(int vertex){
    visited[vertex] = true;
    cout << vertex << " ";
    list<int>::iterator it = adjList[vertex].begin();
    for (it; it != adjList[vertex].end(); ++it){
        if (!visited[*it]){
            DFS(*it);
        }
    }

}

int main(){
    Graph g(5);
    g.add_edge(0, 1);
    g.add_edge(0, 2);
    g.add_edge(0, 3);
    g.add_edge(1, 2);
    g.add_edge(2,4);

    g.DFS(0);
}