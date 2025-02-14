def PUSH(data):
    if len(stack)<capacity:
        stack.append(data)
    else:
        print("stack is Over flow!")
def POP() :
    if stack:
        print(stack[-1],"Poped element ")
        stack.pop()          
    else:
        print("Stack is underFlow")    
def PEEK():
    print(stack[-1],"is PEEK element")     
def Display():
    if stack:
        print(stack) 
    else:
        print("stack is empty!")          
capacity=int(input("Enter the Capacity: "))
stack=[]
print(".................WELCOME TO STACK OPERATIONS..................")
print()
print("enter 1 for PUSH an element")
print("enter 2 for POP an element")
print("enter 3 for PEEK element")
print("enter 4 for display stack")
print("enter -1 exit the console")
while True:
    ch=int(input("enter the choice : "))
    if ch==1:
        data=int(input("enter the data"))
        PUSH(data)
    elif ch==2:
        POP()
    elif ch==3:
        PEEK()
    elif ch==4:
        Display()
    elif ch==-1:
        print("You Have EXITED the program ")
    else:
        print("Invalid input")            

