def binarySearch(arr,left,right,x):
    while(left <= right):
        mid=left+(right-left)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1


arr=[1,4,6,7,10,19,22,23,30,35,39,46,49,50,52,55,61,67,70,71]
left=0
right=(len(arr))-1
x=int(input())

res = binarySearch(arr,left,right,x)
print(res)