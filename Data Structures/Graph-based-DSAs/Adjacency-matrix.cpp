/*Adjacency matrix implementation in cpp:*/

#include "iostream"

using namespace std;

class Graph{
    private:
        bool ** adjMatrix = nullptr;
        int numVertices;
    public:
        Graph(int numVertices){
            this->numVertices = numVertices;
            adjMatrix = new bool * [numVertices];
            for (int i = 0; i < numVertices; i++){
                adjMatrix[i] = new bool [numVertices];
                for (int j= 0; j < numVertices; j++){
                    adjMatrix[i][j] = false;
                }
            }

        }

        void add_edge(int i, int j){
            adjMatrix[i][j] = true;
            adjMatrix[j][i] = true;
        }

        void remove_edge(int i, int j){
            adjMatrix[i][j] = false;
            adjMatrix[j][i] = false;
        }

        void print_matrix(){
            for (int i = 0; i < numVertices; i ++){
                cout << i << " : ";
                for (int j = 0; j < numVertices; j++){
                    cout << adjMatrix[i][j] << " ";
                }
                cout << endl;
            }
        }

        ~Graph(){
            for (int i = 0; i < numVertices ; i++){
                delete[] adjMatrix[i];
            }
            delete[] adjMatrix; 
        }
};

int main(){
    Graph g(5);
    g.add_edge(0, 1);
    g.add_edge(0, 2);
    g.add_edge(1, 2);
    g.add_edge(2, 0);
    g.add_edge(2, 3);
    g.print_matrix();
}