#initialising stack using list
def Stackimplement():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0

def push(stack,data):
    stack.append(data)
    print("%d is pushed into stack"%data)

def pop(stack):
    if(isEmpty(stack)):
        print("stack is empty pop is not possible")
        return 
    return stack.pop()
def peek(stack):
    if(isEmpty(stack)):
        print("stack is empty")
        return 
    return stack[len(stack)-1]
stack=Stackimplement()
print(pop(stack))
push(stack,1)
push(stack,2)
push(stack,3)
print("top element of stack is %d"%peek(stack))
print("%d is popped from satck"%pop(stack))





