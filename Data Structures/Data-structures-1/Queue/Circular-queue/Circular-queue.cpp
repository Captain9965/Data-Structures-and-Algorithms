
/**
 * circular queue implementation in cpp:
*/
#include "iostream"
#include "cstdio"

using namespace std;

class CircularQueue{
    private:
        //define the maximum queue size:
        static const int size = 5;
        int items[size], front, rear;
    public:
        CircularQueue(){
            front = -1;
            rear = -1;
        }
        bool isFull(){
            if(front == 0 && rear == size - 1){
                return true;
            }
            if (front == rear + 1){
                return true;
            }
            return false;
        }

        bool isEmpty(){
            if (front == -1){
                return true;
            }
            return false;
        }

        void enqueue(int element){
            if (isFull()){
                cout << "The circular queue is full!" << endl;
                return;
            } else{
                if (front == -1){
                    front = 0;
                }
                rear = (rear + 1) % size;
                items[rear] = element;
                cout << "Inserted " << element << endl;
                return;
            }
        }

        int dequeue(){
            int element;
            if(isEmpty()){
                cout << "The queue is empty" << endl;
                return -1;
            } else{
                element = items[front];
                /* queue has only one element therefore reset the queue*/
                if (front == rear){
                    front, rear = -1;
                } else{
                    front = (front + 1) % size;
                }
                return element;

            }
        }

        void printQueue(){
            int i;
            if(isEmpty()){
                cout << "Queue is empty!" << endl;
                return;
            } else{
                cout << "Front ->" << front << endl << "Items ->";
                for (i = front; i != rear; i = (i + 1)% size){
                    cout << items[i] << " ";
                }
                cout << items[i] << endl << "Rear -> " << rear << endl;
                return;
            }
        }
};

int main(){
    CircularQueue q;
    /* should fail as queue is empty*/
    q.dequeue();
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    /* should fail as queue is full*/
    q.enqueue(6);
    q.printQueue();

    if(int element = q.dequeue() != -1){
        cout << " Deleted -> " << element << endl;
    }
    q.printQueue();
    q.enqueue(7);
    q.printQueue();

    /*should fail*/
    q.enqueue(8);
}