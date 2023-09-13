def binary_search(arr,left,right,x):
    while(left<=right):
        mid=left+(right-left)//2
        if x==arr[mid]:
            return mid
        elif x>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1


arr=[1,4,6,7,10,19,22,23,30,35,39,46,49,50,52,55,61,67,70,71]
n=len(arr)
left=0
right=n-1
x=int(input())
res=binary_search(arr,left,right,x)

if res==-1:
    print("Not Found")
else:
    print(f"{x} is found in index:",res)