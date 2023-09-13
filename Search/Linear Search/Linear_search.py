def linear_search(arr,n,item):
    for i in range(0,n):
        if arr[i]==item:
            return i
    return -1


arr=[23,55,33,3,7,6,3,88,7,2,6,99,4,7,-5,74]
n=len(arr)
item=int(input())
res=linear_search(arr,n,item)
if res==-1:
    print("Item Not Found")
else:
    print("Item Found at Index:",res)

#Time Comolexity: O(n)
#Space Complexity: O(1)