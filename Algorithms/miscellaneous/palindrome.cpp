#include "iostream"

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int pointer1 = 0, pointer2 = s.size() - 1;
        while(pointer1 < pointer2){
            /* ignore non-alphanumeric characters */
            if(!((s[pointer1] > 47 && s[pointer1] < 58) ||(s[pointer1] > 64 && s[pointer1] < 91) || (s[pointer1] > 96 && s[pointer1] < 123) ))
        {
            pointer1++;
            continue;
        }
        if(!((s[pointer2] > 47 && s[pointer2] < 58) ||(s[pointer2] > 64 && s[pointer2] < 91) || (s[pointer2] > 96 && s[pointer2] < 123) ))
        {
            pointer2--;
            continue;
        }
        if(tolower(s[pointer1]) != tolower(s[pointer2])){
            return false;
        }
        pointer1++;
        pointer2--;
        
        }
        return true;
    }
};

int main(){
    Solution instance;
    string str = "A man, a plan, a canal: Panama";
    cout << (bool)instance.isPalindrome(str) << endl;

}