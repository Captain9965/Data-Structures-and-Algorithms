/* 

This is Korasaju's algorithm to find stongly connected components in cpp:

*/

#include "iostream"
#include "stack"
#include "list"

using namespace std;

class Graph{
    private:
        int V;
        list<int> *adj = nullptr;
        void fill_order(int s, bool visited_vertex[], stack<int> &Stack);
        void dfs(int s, bool visited_vertex[]);

    public:
        Graph(int V);
        void add_edge(int s, int d);
        void print_scc();
        Graph transpose();
};

Graph::Graph(int V){
    this->V = V;
    adj = new list<int>[V];
}

void Graph::dfs(int s ,bool visited_vertex[]){
    visited_vertex[s] = true;
    cout << s <<" ";
    list<int>::iterator i;
    for (i = adj[s].begin(); i != adj[s].end(); i++){
        if (!visited_vertex[*i]){
            dfs(*i, visited_vertex);
        }
    }

}

Graph Graph::transpose(){
    Graph g(V);
    for (int s = 0; s < V; s++){
        list<int>::iterator i;
        for(i = adj[s].begin(); i != adj[s].end(); i++){
            g.adj[*i].push_back(s);
        }
    }
    return g;
}

void Graph::add_edge(int s, int d){
    adj[s].push_back(d);
}

void Graph::fill_order(int s, bool visited_vertex[], stack<int> &Stack){
    visited_vertex[s] = true;
    list<int>::iterator i;
    for (i = adj[s].begin(); i != adj[s].end(); i ++){
        if(!visited_vertex[*i]){
            fill_order(*i, visited_vertex, Stack);
        }
    }
    Stack.push(s);
}

void Graph::print_scc(){
    stack<int> Stack;
    bool * visited_vertex = new bool[V];
    for (int i = 0; i < V; i ++){
        visited_vertex[i] = false;
    }

    for (int i = 0 ;i < V; i++){
        if (visited_vertex[i] == false){
            fill_order(i, visited_vertex, Stack);
        }
    }

    Graph gr = transpose();

    for (int i = 0; i < V; i++){
        visited_vertex[i] = false;
    }

    while (!Stack.empty()){
        int s = Stack.top();
        Stack.pop();

        if (visited_vertex[s] == false){
            gr.dfs(s, visited_vertex);
            cout << endl;
        }
    }
    delete[] visited_vertex;
}

int main(){
    cout << "Strongly connected components with Korasaju's algorithm: " << endl;
    Graph g(8);
    g.add_edge(0, 1);
    g.add_edge(1, 2);
    g.add_edge(2, 3);
    g.add_edge(2, 4);
    g.add_edge(3, 0);
    g.add_edge(4, 5);
    g.add_edge(5, 6);
    g.add_edge(6, 4);
    g.add_edge(6, 7);
    g.print_scc();
}


