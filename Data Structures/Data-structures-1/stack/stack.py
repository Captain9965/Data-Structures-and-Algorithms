
""" Stack implementation in python: """

def create_stack():
    #empty array:
    stack = [] 
    return stack
#checking whether a stack is empty:

def isEmpty(stack):
    return len(stack) == 0
#checking whether a stack is full:

def isFull(stack, max_length = 5):
    return len(stack) >= max_length

#adding of items onto the stack:
def push(stack, item):
    #check whether the stack is full:
    if(isFull(stack, 5)):
        print(f"Im sorry, the stack is full")
        return
    stack.append(item)
    print("pushed item is "+ str(item))

#removing items from the stack:

def pop(stack):
    #check if empty:
    if (isEmpty(stack)):
        print("Stack is already empty")
        return -1
    popped_value = stack.pop()
    print("popped item is " + str(popped_value))
    return popped_value

if __name__ == "__main__":
    stack = create_stack()

    for i in range(6):
        push(stack, i)
    for i in range(6):
        pop(stack)
