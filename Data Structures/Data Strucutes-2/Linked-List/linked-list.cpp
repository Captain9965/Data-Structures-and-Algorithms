/* Linked list operations in cpp: */

#include "iostream"

using namespace std;

struct Node{
    int data;
    struct Node * next = nullptr;
};

void insertAtBeginning(struct Node ** head_ref, int new_data){
    /* Allocate memory to a node:*/
    struct Node * new_node = (struct Node *)malloc(sizeof(struct Node));
    /*insert the data:*/
    new_node->data = new_data;
    new_node->next = (*head_ref);

    /* move head to new node:*/
    (*head_ref) = new_node;
}

/* insert a node after a node:*/
void insertAfter(struct Node *prev_node, int new_data){
    if(prev_node == nullptr){
        cout << "\n The previous node given cannot be null! \n";
        return;
    }

    struct Node * new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
    return;
}

/*Insert at End:*/

void insertAtEnd(struct Node ** head_ref, int new_data){
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    struct Node *last = *head_ref;

    new_node->data = new_data;
    new_node->next = nullptr;

    if (*head_ref == nullptr){
        *head_ref = new_node;
        return;
    }
    while(last->next != nullptr) last = last->next;

    last->next = new_node;
    return;

}

/* delete a certain node*/
void deleteNode(struct Node **head_ref, int key){
    struct Node *temp = *head_ref, *prev;
    
    /* The node is at the beginning: */
    if(temp != nullptr && temp->data == key){
        *head_ref = temp->next;
        free(temp);
        return;
    }

    /* find the key to be deleted:*/
    while(temp != nullptr && temp->data != key){
        prev = temp;
        temp = temp->next;
    }
    /* key is not present:*/
    if(temp == nullptr) return;

    /* remove the node:*/
    prev->next = temp->next;
    free(temp);
    return;
}

/* search a node:*/
bool searchNode(struct Node** head_ref, int key){
    struct Node *current = *head_ref;

    while(current != nullptr){
        if(current->data == key)return true;
        current = current->next;
    }
    return false;
}

/* sort the linked list with Bubble sort algorithm:*/
void sortLinkedList(struct Node ** head_ref){
    struct Node *current = *head_ref, *index = nullptr;
    
    int temp;

    if(head_ref == nullptr)return;
    else{
        while(current != nullptr){
            /* index points to the node next to current:*/
            index = current->next;
            while(index != nullptr){
                if(current->data > index->data){
                    temp = current->data;
                    current->data = index->data;
                    index->data = temp;
                }
                index = index->next;
            }
            current = current->next;

        }
    }
}
/* print the linked list:*/

void printLinkedList(struct Node * node){
    while(node != nullptr){
        cout << node->data << " ";
        node = node->next;
    }
}

int main(){
    struct Node * head = nullptr;
    insertAtEnd(&head, 1);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 3);
    insertAtEnd(&head, 4);
    insertAfter(head->next,5);
    
    cout << "\n Linked List ->\n";
    printLinkedList(head);
    cout <<"\nAfter deleting an element (3)-> \n";
    deleteNode(&head, 3);
    printLinkedList(head);
    if (searchNode(&head, 3)){
        cout<< "\n 3 is found\n";
    }else{
        cout <<"\n 3 is not found\n";
    }

    sortLinkedList(&head);
    cout <<"\nSorted Linked List -> \n";
    printLinkedList(head);

}