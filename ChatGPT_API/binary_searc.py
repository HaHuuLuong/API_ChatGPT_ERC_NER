def binary_search(arr, x):
    low=0;
    high=len(arr) - 1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if(arr[mid]<x):
            low=mid+1
        elif(arr[mid]>x):
            low=mid-1
        else:
            return mid
    return -1
arr = [2, 3, 4, 10, 40]
x =10
result=binary_search(arr, x)
print(arr[result])