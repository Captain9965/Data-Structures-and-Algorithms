/* longest common subsequence in cpp: */

#include "iostream"
#include "cstring"

using namespace std;

void lcsAlgo(char * S1, char* S2, int m, int n){
    int lcsTable[m + 1][n + 1];
    /*building the matrix in a bottom up way:*/

    for (int i = 0; i <= m; i++){
        for (int j = 0; j <= n; j++){
            if(i == 0 || j == 0){
                lcsTable[i][j] = 0;
                }
            else if(S1[i - 1] == S2[j - 1]){
                lcsTable[i][j] = lcsTable[i - 1][j - 1] + 1;
                }
            else{
                lcsTable[i][j] = max(lcsTable[i - 1][j] , lcsTable[i][j - 1]);
            }
            }
        }
    int index = lcsTable[m][n];
    char lcsAlgo[index + 1];
    lcsAlgo[index] = '\0';

    int i = m, j = n;

    while(i > 0 && j > 0){
        if(S1[i - 1] == S2[j - 1]){
            lcsAlgo[index - 1] = S1[i - 1];
            i --;
            j --;
            index --;
        } else if(lcsTable[i - 1][j] > lcsTable[i][j - 1]){
            i --;
        } else{
            j --;
        }
    }

    /* printing the subsequence: */
    cout << " S1: " << S1 << endl << "S2: " << S2 << endl << " LCS: " << lcsAlgo << endl;

}


/* driver code: */

int main(){
    char S1[] = "ACADB";
    char S2[] = "CBDA";

    int m = strlen(S1);
    int n = strlen(S2);

    lcsAlgo(S1, S2, m, n);

}