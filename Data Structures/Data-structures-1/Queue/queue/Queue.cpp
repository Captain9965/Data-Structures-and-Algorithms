/* queue implementation in cpp */

#include "iostream"
#include "cstdlib"
#define SIZE 5

using namespace std;

class Queue
{
private:
    int items[SIZE], front,rear;
public:
    Queue();
    ~Queue();
    bool isFull();
    bool isEmpty();
    bool justEmpty();
    void resetQueue();
    int enqueue(int item);
    int dequeue(int &element);
    int printQueue();

};

Queue::Queue()
{
    resetQueue();
}

Queue::~Queue()
{

}
bool Queue::isFull()
{
    return front == 0 && rear >= SIZE - 1;
}

bool Queue::isEmpty()
{
    return front == -1;
}

bool Queue::justEmpty(){
    return front >=rear && (front != -1);
}

int Queue::enqueue(int item){
    if(isFull()){
        cout << "The queue is full!" << endl;
        return -1;
    }
    if(isEmpty()){
        front++;
    }
    cout << "Added item "<< item << endl;
    items[++rear] = item;
    cout <<"Front "<< front <<" Rear " <<rear <<endl;
    return 0;
    
}

void Queue::resetQueue(){
    front = -1;
    rear = -1;
}


int Queue::dequeue(int &element){
    if(isEmpty()){
        cout <<"The queue is already empty!" << endl;
        return -1;
    }
    element = items[front];
    cout <<"Removed element is " << items[front] << endl;
    if (justEmpty()){
        cout<<"Queue is now empty..resetting " <<endl;
        resetQueue();
    } else{
        front++;
    }
    return 0;
}

int Queue::printQueue(){
    if(isEmpty()){
        cout << "the queue is empty" <<endl;
    }

    for (int i = front; i<= rear; i++){
        cout<< items[i] << " ";
    }
    cout <<endl;
    return 0;
}

int main(){
    Queue* q = new Queue();
    for(int i =0; i <=7 ; i++){
        q->enqueue(i);
    }
    q->printQueue();
    int element;
    for (int i=0; i<=7; i++){
        q->dequeue(element);
    }
    q->printQueue();
    delete q;
}


