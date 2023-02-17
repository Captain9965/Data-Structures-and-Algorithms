/* cpp STL implementation of dijkstra's algorithm: Has O(E log V) complexity in time */

#include "bits/stdc++.h"
#include "limits.h"

using namespace std;

typedef pair<int, int> iPair;

class Graph{
    private:
        int V;

        /* in a weighted graph, we need to store vertex and weight pair for every single edge: */
        list<pair<int, int> >* adj;
    public:
        Graph(int V);
        void addEdge(int u, int v, int w);
        void shortestPath(int src);
};

Graph::Graph(int V){
    this->V = V;
    adj = new list<iPair>[V];
}

void Graph::addEdge(int u, int v, int w){
    adj[u].push_back(make_pair(v, w));
    adj[v].push_back(make_pair(u, w));
}

void Graph::shortestPath(int src){
    /* priority queue that stores the vertices that are being processed: */
    priority_queue<iPair, vector<iPair>, greater<iPair> > pq;

    /* create a vector for distances and initialize all as infinite*/
    vector< int > dist(V, INT_MAX);

    /* insert source in priority queue and intialize distance as zero: */
    pq.push(make_pair(0, src));
    dist[src] = 0;
    
    /* looping till priority queue becomes empty: */
    while(!pq.empty()){
        /* the first vertex in pair is the minimum distance vertex, extracted from the 
        priority queue. label is stored in the second of the pair 3*/

        int u = pq.top().second;
        pq.pop();


        list<iPair >::iterator i;

        for (i = adj[u].begin(); i != adj[u].end(); ++i){
            /* get vertex label and weight of current adjacent of u*/

            int v = (*i).first;

            int weight = (*i).second;

            /* if there is a shorter path v through u:*/
            if (dist[v] > dist[u] + weight){
                /* update the distance of v: */
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }

    /* print shortest distances stored in dist[]: */
    cout << "Vertex" << "\t\t" << "Distance from source"<< endl;

    for (int i = 0; i < V; i ++){
        cout << i << "\t\t\t\t" << dist[i]<< endl;
    }
}

/* driver code: */
int main(){
    /* create the graph: */
    int V = 9;
    Graph g(V);

    g.addEdge(0, 1, 4);
    g.addEdge(0, 7, 8);
    g.addEdge(1, 2, 8);
    g.addEdge(1, 7, 11);
    g.addEdge(2, 3, 7);
    g.addEdge(2, 8, 2);
    g.addEdge(2, 5, 4);
    g.addEdge(3, 4, 9);
    g.addEdge(3, 5, 14);
    g.addEdge(4, 5, 10);
    g.addEdge(5, 6, 2);
    g.addEdge(6, 7, 1);
    g.addEdge(6, 8, 6);
    g.addEdge(7, 8, 7);
 
    g.shortestPath(0);
    return 0;
}