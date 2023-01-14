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
        void dequeueFront();
        void dequeueRear();
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

bool Dequeue::isEmpty(){
    return (front == -1);
}


void Dequeue::enqueueFront(int key){
    if (isFull()){
        cout << " The queue is full "<< endl;
        return;
    } else{
        if(front == -1){
            front = 0;
            rear = 0;
        } else if(front == 0){
            front = size - 1;
        } else{
            front = front - 1;
        }
        items[front] = key;
    }
}

void Dequeue::enqueuetRear(int key){
    if (isFull()){
        cout << " The queue is full" << endl;
        return;
    }else{
        if(front == -1){
            front = 0;
            rear = 0;
        } else if(rear == size - 1){
            rear = 0;
        }else{
            rear = rear + 1;
        }
        items[rear] = key;
    }
}

void Dequeue::dequeueFront(){
    if(isEmpty()){
        cout << "Queue is already empty" << endl;
        return;
    }else{
        if(front == rear){
            front = -1;
            rear = -1;
        } else if(front == size - 1){
            front = 0;
        } else{
            front = front + 1;
        }
    }

}

void Dequeue::dequeueRear(){
    if(isEmpty()){
        cout << " The queue is empty" << endl;
        return;
    } else{
        if(front == rear){
            front = -1;
            rear = -1;
        } else if(rear == 0){
            rear = size - 1;
        } else{
            rear = rear - 1;
        }
    }
}

int Dequeue::getFront(){
    if(isEmpty()){
        cout << "The queue is empty" << endl;
        return -1;
    }
    return items[front];
}

int Dequeue::getRear(){
    if (isEmpty() || rear < 0){
        cout << "The queue is empty" << endl;
        return -1;
    }
    return items[rear];
}

int main(){
    Dequeue q(4);
    cout << "Inserting elements at the rear " << endl;
    q.enqueuetRear(5);
    q.enqueuetRear(11);
    q.enqueuetRear(35);

    cout << "Rear element is -> " << q.getRear() << endl;
    q.dequeueRear();
    cout << "After deleting rear, the last element is -> " << q.getRear() << endl;
    cout << "Inserting element at the front " << endl;

    q.enqueueFront(8);
    cout << "Front element is -> " << q.getFront() << endl;
    q.dequeueFront();
    cout << "After Deleting the front element, the first element is -> " << q.getFront() << endl;



}