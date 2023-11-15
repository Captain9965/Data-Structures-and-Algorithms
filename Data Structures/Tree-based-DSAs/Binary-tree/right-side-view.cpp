#include "bits/stdc++.h"
using namespace std;

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

/* with Bfs */
    vector<int> rightSideViewBfs(TreeNode* root) {
        vector<int> solution;
        if (!root){
            return solution;
        }
        deque<TreeNode *> child_nodes;
        child_nodes.push_back(root);

        int node_count = 0;
        int initial_queue_size = 1;

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


            if(node_count == initial_queue_size){
                /*reset sibling_vec*/
                solution.push_back(child_node->val);
                node_count = 0;
                initial_queue_size = child_nodes.size();
            }
            
        }
        return solution;       
    }

    /*with dfs*/
    vector<int> rightSideViewDfs(TreeNode* root){
        vector<int> result;
        if(!root){
            return result;
        }
        
        dfs(root, result);
        return result;
    } 

    void dfs(TreeNode * root, vector<int> & result, int level = 0){
        if(!root){
            return;
        }
        int vec_size = result.size();
        if (level >= vec_size){
            result.push_back(root->val);
        } else{
            result[level] = root->val;
        }

        dfs(root->left, result, level + 1);

        dfs(root->right, result, level + 1);
        return;
    }
    
};