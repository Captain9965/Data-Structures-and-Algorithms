/* rabin karp implentation in cpp: */
#include "bits/stdc++.h"

using namespace std;

#define d 256

void search(char * pat, char * txt, int q){
    int m = strlen(pat);
    int n = strlen(txt);
    int i, j;
    int p = 0; /* hash value for pattern*/
    int t = 0; /* hash value for txt*/
    int h = 1;

    /* the value of h would be "pow(d, M-1)%q"*/
    for (int i = 0; i < m - 1; i ++){
        h = (h * d) % q;
    }

    /* calculate the hash value of pattern and first window of text:*/
    for (i = 0; i < m; i ++){
        p = (d * p + pat[i]) % q;
        t = (d * t + txt[i]) % q;
    }

    /* slide the pattern over text one by one: */
    for (i = 0; i <= n - m; i++){
        /* check the hash values of current window of text and pattern. If they match
         then and only then do we check one by one: */
         if (p == t){
            /* check for the characters one by one: */
            for (j = 0; j < m; j ++){
                if (txt[i + j] != pat[j]){
                    break;
                }
            }
            /*if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]*/

            if(j == m){
                cout << "Pattern found at index " << i << endl;
            }
         }

         /* calculate the hash value for the next window of text, remove the leading digit and add trailing digit*/
         if (i < n - m ){
            t = (d * (t - txt[i] * h) + txt[i + m]) % q;

            if (t < 0){
                t = t + q;
            }
         }
    }

}
/* driver code: */

int main(){
    char txt[] = "FOOD FIRST FOR FOOLS";
    char pat[] = "FOO";
    /* we mod to avoid overflowing value but we should take as big q as possible to avoid collision*/
    int q = INT_MAX;
    search(pat, txt,q);
    return 0;
}