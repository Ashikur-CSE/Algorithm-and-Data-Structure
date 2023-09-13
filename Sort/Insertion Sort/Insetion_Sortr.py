def insertion_sort(arr,n):
    for i in range(1,n):
        item=arr[i]
        j=i-1
        while(j>=0 and arr[j]>item):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=item

arr=[5,4,3,2,1]
n=len(arr)
insertion_sort(arr,n)
print(arr)
