/* stack implementation in cpp */

#include "cstdlib"
#include "iostream"

using namespace std;

#define MAX 10

int size = 0;

typedef struct stack{
    int items[MAX];
    int top;
}stack_t;

stack st;

void createEmptyStack(stack* st){
    st->top = -1;
    return;
}

bool isFull(stack* st){
    return st->top >= MAX-1;
}

bool isEmpty(stack* st){
    return st->top < 0;
}

int push(stack* st, int new_item){
    if(isFull(st)){
        cout << "Stack is already full" << endl;
        return -1;
    }
    st->items[++st->top] = new_item;
    cout << "Pushed item is -> " << st->items[st->top] <<endl;
    return 0;
}

int pop(stack* st){
    if(isEmpty(st)){
        cout<< "Stack is already empty"<<endl;
        return -1;
    }
    cout << "Item popped is -> " << st->items[st->top--] <<endl;
    return 0;
}

int printStack(stack* st){
    if (isEmpty(st)){
        cout << "The stack is empty" << endl;
        return -1;
    }
    for(int i = 0; i <= st->top; i++){
        cout << st->items[i] <<" ";
    }
    cout <<endl;
    return 0;
}


int main(){
    stack* st = new stack;
    //or:
    // stack* st = (stack *)malloc(sizeof(stack));
    createEmptyStack(st);
    push(st, 1);
    push(st, 23);
    push(st,34);
    push(st, 56);

    printStack(st);
    //pop all out
    for (int i = 0; i < 6; i++){
        pop(st);
    }

    cout << "After popping -> " <<endl;
    printStack(st);
    //cleanup:
    delete st;
    // free(st);
    // st = nullptr;

}

