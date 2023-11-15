#include "bits/stdc++.h"
 /* Definition for a binary tree node.*/
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 

using namespace std;

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (!root)return true;

       return dfs(root, numeric_limits<long long int>::min(), numeric_limits<long long int>::max());
    }

    bool dfs(TreeNode * root, long long int min, long long max){
        /* return if we are outside of our boundaries */
        if (!root) return true;

        if(root->val <= min || root->val >= max) return false;
        return dfs(root->left, min, root->val) && dfs(root->right, root->val, max);
    }

};

int main(){
    TreeNode node(2147483647);
    Solution instance;
    cout << instance.isValidBST(&node) <<endl;
}