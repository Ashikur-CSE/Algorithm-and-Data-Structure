def LinearSearch(arr,x,n):
    for i in range(0,n):
        if arr[i] == x:
            return i

    return -1


arr=[23,55,33,3,7,6,3,88,7,2,6,99,4,7,-5,74]
x=int(input())
n=len(arr)

res = LinearSearch(arr,x,n)
print(res)
