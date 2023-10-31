#include "iostream"
#include "bits/stdc++.h"

using namespace std;


class Solution {
public:
    string minRemoveToMakeValid(string s) {
        if (s.length() < 1) return s;
        vector<int> st;
        for (int i = 0; i < s.length(); i ++){
            if (s[i] == '('){
                st.push_back(i); // store the index of '('
            } else if(s[i] == ')'){
                // see whether it has a partner:
                if(!st.empty()){
                    st.pop_back();
                } 
                else{
                    s[i] = ' ';
                }
            }
        }
        while(!st.empty()){
            int index = st.back();
            st.pop_back();
            s[index] = ' ';
        }
        s.erase(std::remove(s.begin(), s.end(), ' '), s.end());
        return s;
    }
};

int main(){
    string s = "))(())";
    Solution sol;
    cout << sol.minRemoveToMakeValid(s) << endl;
}