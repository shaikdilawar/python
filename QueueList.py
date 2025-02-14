#QUEUE USING ARRAY
def Enqueue(data):
    global front
    global rear
    if front == -1  and rear == -1:
        queue.append(data)
        front = 0 ; rear = 0
        print(queue[rear],"is Enqueued into queue")
    else:
        rear += 1
        queue.append(data)
        print(queue[rear],"is Enqueued into queue")

def Dequeue():
    global front 
    global rear
    if front== -1 and rear==-1:
        print("Queue is empty")
    elif front == 0 and rear == 0:
        print(queue[front],"is Dequeued from queue")
        queue.pop(0)
        front = -1
        rear = -1
    else:
        print(queue[front],"is Dequeued from queue")
        queue.pop(0) 
        rear -= 1

def Display():
    if queue:
        print(queue)
    else:
        print("Queue is Empty")

if __name__ == "__main__":
    queue = []
    front = -1
    rear = -1

    print("\n***********WELCOME TO QUEUE OPERATIONS***********")
    print("Enter 1 into Enqueue an element into Queue")
    print("Enter 2 into Dequeue an element from Queue")
    print("Enter 3 to Display all elements in Queue")
    print("Enter 4 to Exit\n")

    while(True):
        ip = int(input("Enter your choice :- "))
        if ip ==1:
            data = int(input("Enter your Enqueue value :- "))
            Enqueue(data)
        elif ip ==2:
            Dequeue()
        elif ip ==3:
            Display()
        elif ip ==4:
            print("You have exited the program")
            break
        else:
            print("Invalid choice ")

        