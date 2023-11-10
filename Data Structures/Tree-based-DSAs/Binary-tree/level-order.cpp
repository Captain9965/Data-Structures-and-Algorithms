#include "bits/stdc++.h"

using namespace std;

struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> solution;
        if (!root){
            return solution;
        }
        deque<TreeNode *> child_nodes;
        child_nodes.push_back(root);

        int node_count = 0;
        int initial_queue_size = 1;

        vector<int> sibling_vec;

        while (!child_nodes.empty()){

            TreeNode * child_node = *(child_nodes.begin());
            child_nodes.pop_front();
    
            if (child_node->left){
                child_nodes.push_back(child_node->left);
            }

            if(child_node->right){
                child_nodes.push_back(child_node->right);
            }

            node_count++;
            sibling_vec.push_back(child_node->val);

            if(node_count == initial_queue_size){
                /*reset sibling_vec*/
                solution.push_back(sibling_vec);
                sibling_vec.clear();
                node_count = 0;
                initial_queue_size = child_nodes.size();
            }
            
        }
        return solution;
    }
};

int printVector(vector<vector<int>> & vec){
    if (!vec.empty()){
        cout << "\n[";
        for (vector<vector<int>>::iterator it = vec.begin(); it != vec.end(); it++){
            cout << "[";
            for(vector<int>::iterator v = it->begin(); v != it->end(); v ++){
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
    TreeNode * tree = new TreeNode(20);
    tree->left = new TreeNode(40);
    tree->right =new TreeNode(70);

    Solution instance;
    vector<vector<int>> result = instance.levelOrder(tree);
    printVector(result);
}