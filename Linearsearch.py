def Linear_Search(arr,key):

    for i in range(len(arr)):
        if arr[i]== key:
            return "Key Found"
        
    return "Key Not Found"

arr = list(map(int,input().split()))
key = int(input())

print(Linear_Search(arr,key))