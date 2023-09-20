#include <iostream>
using namespace std;
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        int backSpaceCount1 = 0, backSpaceCount2 = 0, charIndex1 = s.size() - 1, charIndex2 = t.size() - 1;


        while(charIndex1 >= 0 || charIndex2 >= 0){
            if ((charIndex1 >= 0 && s[charIndex1] == '#') || (charIndex2 >= 0 && t[charIndex2] == '#')){
                if (charIndex1 >= 0 && s[charIndex1] == '#'){
                    backSpaceCount1++;
                    charIndex1 --;
                }
                if (charIndex2 >= 0 && t[charIndex2] == '#'){
                    backSpaceCount2++;
                    charIndex2 --;
                }
                continue;
            }
            if ((charIndex1 >= 0 && backSpaceCount1 > 0) || (charIndex2 >= 0 && backSpaceCount2 > 0)){
                if (charIndex1 >= 0 && backSpaceCount1 > 0){
                    charIndex1 --;
                    backSpaceCount1 --;
                }
                if (charIndex2 >= 0 && backSpaceCount2 > 0){
                    charIndex2 --;
                    backSpaceCount2 --;
                }
                continue;
            }
           
        
            if((charIndex1 >= 0 ) && (charIndex2 >= 0 )){

                if ((s[charIndex1] != t[charIndex2])){
                    cout << s[charIndex1] << " " << t[charIndex2] << endl;
                    return false;
                }
                
                charIndex1 --;
                charIndex2 --;

            } else {
                return false;
            }

  
        }
        return true;

    }
};

int main(){
    Solution instance;
    string string1 = "bxj##tw";
    string string2 = "bxo#j##tw";

    instance.backspaceCompare(string1, string2) ? cout << "True" << endl : cout << "false" << endl;
}