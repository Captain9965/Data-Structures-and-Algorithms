/* dequeue implementation in cpp:*/
#include "iostream"
#define MAX 10
using namespace std;

class Dequeue{
    private:
        int items[MAX], front, rear, size;
    public:
        Dequeue(int size);
        void enqueueFront(int key);
        void enqueuetRear(int key);
        int dequeueFront();
        int dequeueRear();
        bool isFull();
        bool isEmpty();
        int getFront();
        int getRear();    
};

Dequeue::Dequeue(int size){
    front = -1;
    rear = 0;
    this->size = size;
}

bool Dequeue::isFull(){
    return ((front == 0 && rear == size - 1)|| front == rear + 1);
}


void Dequeue::enqueueFront(int key){

}