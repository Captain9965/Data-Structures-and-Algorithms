/* bfs in cpp for adjacency list: */

#include "bits/stdc++.h"

using namespace std;


int printVector(vector<char> & vec){
    if (!vec.empty()){
        cout << "\nElements are: ";
        for (vector<char>::iterator it = vec.begin(); it != vec.end(); it++){
            cout << *it << " ";
        }
        return vec.size();
    }
    else{
        cout<< "the vector is empty"<<endl;
        return -1;
    }
}

char showmap(map<char, vector<char>> &map_){
    if (!map_.empty()){
        for (map<char, vector<char>>::iterator it = map_.begin(); it != map_.end(); it++){
            cout << it->first << ": [";
            for(auto v = it->second.begin(); v != it->second.end() ;v++){
                    cout << *v << ",";
            }
            cout <<"]" << endl;
        }
    }else{
        cout << "\n The map is empty " << endl;
    }
    return map_.size();
}

int showset(set<char> &s){
    if (!s.empty()){
         for (set<char,less<char>>::iterator it = s.begin() ; it != s.end() ; it++){
        cout << *it << " " ;
    }
    cout << endl;
    } else{
        cout << " The set is empty!" << endl;
    }
    return s.size();
}

vector<char> traversal_bfs(map<char, vector<char>> &adj, set<char> &visited, char root){
    queue<char> queue;
    vector<char> values;
    queue.push(root);
    while(!queue.empty()){
        char element_popped = queue.front();

        queue.pop();
        auto it = adj.find(element_popped);
        values.push_back(element_popped);
        visited.insert(element_popped);

        if (it == adj.end()){
            cout << "Fatal error: invalid graph" << endl;
            return values;
        }

        vector<char> neighbours = it->second;

        for (auto it = neighbours.begin(); it != neighbours.end(); it ++){
            char neighbour = *it;
            if (visited.find(neighbour) == visited.end()){ // neighbour not yet visited, add to visited and to queue
                    
                    queue.push(neighbour);
            }
        }
    }
    return values;
}

vector<char> traversal_dfs(map<char, vector<char>> &adj, set<char> &visited, char root, vector<char> &values){
    values.push_back(root);
    visited.insert(root);

    auto it = adj.find(root);
    if (it == adj.end())return values;

    vector<char>neighbours = it->second;

    for(auto it = neighbours.begin(); it!= neighbours.end(); it ++){
        char neighbour = *it;
        if(visited.find(neighbour) == visited.end())traversal_dfs(adj, visited, neighbour, values);
    }
    return values;

}

int main(){
    map<char, vector<char>> graph;
    graph.insert(pair<char, vector<char>>('0',{'1','3'}));
    graph.insert(pair<char, vector<char>>('1',{'0'}));
    graph.insert(pair<char, vector<char>>('3',{'0','4','5','2'}));
    graph.insert(pair<char, vector<char>>('2',{'3','8'}));
    graph.insert(pair<char, vector<char>>('4',{'3','6'}));
    graph.insert(pair<char, vector<char>>('5',{'3'}));
    graph.insert(pair<char, vector<char>>('6',{'4','7'}));
    graph.insert(pair<char, vector<char>>('7',{'6'}));
    graph.insert(pair<char, vector<char>>('8',{'2'}));

    showmap(graph);
    set<char> visited_bfs, visited_dfs;
    vector<char> dfs_values;
    vector<char> values = traversal_bfs(graph, visited_bfs, '0');
    traversal_dfs(graph, visited_dfs,'0', dfs_values);
    
    printVector(values);
    printVector(dfs_values);
}