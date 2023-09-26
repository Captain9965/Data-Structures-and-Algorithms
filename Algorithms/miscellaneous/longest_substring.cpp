#include "iostream"
#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() < 1){
            return 0;
        }

        int max_count = 0, count = 0;
        int pointer1 = 0, pointer2 = 0;

        map<char, int> seen_chars;
        while (pointer2 < s.size()){
            /* have we seen this character before? */
            auto it = seen_chars.find(s[pointer2]);
            
            if (it != seen_chars.end()){
                if(it->second >= pointer1){
                    pointer1 = (it->second) + 1;
                }
                it->second = pointer2;
            } else{
                seen_chars.insert(pair<char, int>(s[pointer2], pointer2));
                
            }
            count = (pointer2 - pointer1) + 1;
            if (count > max_count)max_count = count;
            pointer2++;
            
        }
        return max_count;
    }
};


int main(){
    Solution instance;
    int length = instance.lengthOfLongestSubstring("abbbbcag");
    cout << length << endl;
}