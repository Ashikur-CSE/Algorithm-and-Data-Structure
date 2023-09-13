def bainary_search(arr,left,right,x):
    while (left<=right):
        mid =(left+right)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1
        
arr=[1,4,6,7,10,19,22,23,30,35,39,46,49,50,52,55,61,67,70,71]
n=len(arr)
x=23
left=0
right=len(arr)-1
res=bainary_search(arr,left,right,x)
if res!=-1:
    print('Index:',res)
else:
    print("Not Found")