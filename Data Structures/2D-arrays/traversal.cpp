#include "bits/stdc++.h"

using namespace std;

int printMatrix(vector<vector<bool>> & vec);

void dfs(vector<vector<int>> & array, vector<int> & values , vector<vector<bool>> & visited, int directions[4][2], int row = 0, int column = 0){
    /* if we hit the boundary conditions, return*/
    if(row < 0 || column < 0 || row >= array.size() || column >= array[0].size() or visited[row][column] == true) return;

    visited[row][column] = true;
    values.push_back(array[row][column]);
    for (int i = 0 ; i < 4; i++){
        dfs(array, values, visited, directions, row + directions[i][0], column + directions[i][1]);
    }
    
}

vector<int> dfs_array(vector<vector<int>> & array){
    vector<int> values = {};
    if (array.empty()) return values;
    int directions[4][2] ={{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    vector<vector<bool>> visited(array.size(), vector<bool>(array[0].size(), false));

    printMatrix(visited);
    dfs(array, values, visited, directions);
    printMatrix(visited);
    return values;

}
void bfs(vector<vector<int>> & array, vector<int> & values , queue<vector<int>> & queue, vector<vector<bool>> & visited, int directions[4][2]){

    while (!queue.empty()){

        vector<int> pos = queue.front();
        queue.pop();
        
        int row = pos[0];
        int column = pos[1];

        if(row < 0 || column < 0 || row >= array.size() || column >= array[0].size() || visited[row][column]) continue;

        values.push_back(array[row][column]);
        visited[row][column] = true;

        for (int i = 0 ; i < 4; i++){

            int new_row = row + directions[i][0];
            int new_column = column + directions[i][1];
            queue.push({new_row, new_column});  
        }
    }

    cout << "queue is now done!" << endl;
   
}

vector<int> bfs_array(vector<vector<int>> &array){
    vector<int> values;
    if(array.empty()) return values;
    int directions[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    vector<vector<bool>> visited (array.size(), vector<bool>(array[0].size(), false));

    queue <vector<int>> queue;
    queue.push({2, 2});
    cout << "Begin with : " << array[2][2] << endl;

    bfs(array, values, queue, visited, directions);
    return values;

}

int printVector(vector<int> & vec){
    if (!vec.empty()){
        cout << "\n[";
        for (vector<int>::iterator it = vec.begin(); it != vec.end(); it++){
            cout << *it << ",";
        }
        cout << "]" << endl;
        return vec.size();
    }
    else{
        cout<< "the vector is empty"<<endl;
        return -1;
    }
}

int printMatrix(vector<vector<bool>> & vec){
    if (!vec.empty()){
        cout << "\n[";
        for (vector<vector<bool>>::iterator it = vec.begin(); it != vec.end(); it++){
            cout << "[";
            for(vector<bool>::iterator v = it->begin(); v != it->end(); v ++){
                cout << *v << ",";
            }
            cout << "]";
                
        }
        cout << "]" << endl;
        return vec.size();
    }
    else{
        return -1;
    }
}

int main(){
    vector<vector<int>> array = {{10, 2, 3, 4, 5, 6},
                                    {7, 8, 9, 10, 11,12},
                                    {13, 14, 15, 16, 17, 18}};
    vector<int> result = bfs_array(array);
    printVector(result);
}




