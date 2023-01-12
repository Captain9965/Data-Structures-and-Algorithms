/* hash table implementation in cpp:*/

#include "bits/stdc++.h"

using namespace std;

class HashTable{
    public:
        HashTable(int V);
        void insertItem(int key, int data);
        void deleteItem(int key, int data);
        bool checkprime(int n);
        int getprime(int n);
        int hashfunction(int key);
        void displayHash();

    private:
        int capacity;
        list<int> * table;
};

HashTable::HashTable(int V){
    int size = getprime(V);
    this->capacity = size;
    table = new list<int> [capacity];
}

bool HashTable::checkprime(int n){
    int i;
    if (n == 0 || n == 1){
        return false;
    }

    for (i = 2; i < n/2; i ++){
        if (n % i == 0)return false;
    }
    return true;

}
int HashTable::getprime(int n){
    if (n % 2 == 0){
        n ++;
    }
    while(!checkprime(n)){
        n += 2;
    }
    return n;

}

int HashTable::hashfunction(int key){
    return(key % capacity);
}

void HashTable::insertItem(int key, int data){
    int index = hashfunction(key);
    table[index].push_back(data);
}

void HashTable::deleteItem(int key, int data){
    int index = hashfunction(key);

    list<int>::iterator i;

    for(i = table[index].begin(); i != table[index].end(); i ++){
        if(*i == data){
            break;
        }
    }

    if (i != table[index].end()){
        table[index].erase(i);
    }

}

void HashTable::displayHash(){
    for (int i = 0; i < capacity; i ++){
        cout <<"Table["<< i <<"]";
        for (auto x: table[i]){
            cout << "--> " << x;
        }
        cout << endl;
    }
}

int main(){
    int key[] = {231, 321, 212, 321, 433, 262};
    int data[] = {123, 432, 523, 43, 423, 111};
    int size = sizeof(key)/ sizeof(key[0]);

    HashTable ht(size);

    for(int i = 0; i < size; i ++){
        ht.insertItem(key[i], data[i]);
    }
    ht.displayHash();
    ht.deleteItem(212, 523);

    cout <<"\nAfter deleting key 212:\n";
    ht.displayHash();
}