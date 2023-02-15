/* floyd warshall algorithm in cpp: */

#include "iostream"

using namespace std;

#define nV 4
#define INF 999

void printMatrix(int graph[][nV]);

void floydWarshall(int graph[][nV]){
    int resultMatrix[nV][nV], i, j, k;

    /* copy the matrix*/
    for (int i = 0; i < nV; i ++){
        for (int j = 0; j < nV; j ++){
            resultMatrix[i][j] = graph[i][j];
        }
    }

    /* adding vertices individually: */

    for(k = 0; k < nV; k++){
        for (i = 0; i < nV; i ++){
            for (j = 0; j < nV; j ++){
                if (resultMatrix[i][k] + resultMatrix[k][j] < resultMatrix[i][j]){
                    resultMatrix[i][j] = resultMatrix[i][k] + resultMatrix[k][j];
                }
            }
        }
    }

    printMatrix(resultMatrix);
}


/* utility function to print the result matrix: */

void printMatrix(int graph[][nV]){
    for (int i = 0; i < nV; i ++){
        for (int j = 0; j < nV; j ++){
            if( graph[i][j] == INF){
                cout << "INF" << " ";
            } else{
                cout << graph[i][j] << " ";
            }
        }
        cout << endl;
    }
}
/* driver code: */

int main(){
    int graph[nV][nV] = {{0, 3, INF, 5},
                        {2, 0, INF, 4},
                        {INF, 1, 0, INF},
                        {INF, INF, 2, 0}};
  floydWarshall(graph);
}