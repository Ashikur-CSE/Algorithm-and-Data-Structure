def linear_search(arr,x,n):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

arr=[23,55,33,3,7,6,3,88,7,2,6,99,4,7,-5,74]
n=len(arr)
x=int(input("Enter search item:"))
res=linear_search(arr,x,n)
if res==-1:
    print("Not Found")
else:
    print(f'{x} found in index:',res+1)