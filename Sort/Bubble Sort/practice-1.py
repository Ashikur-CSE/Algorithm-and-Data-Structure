def bubble_sort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

arr=[10,5,2,8,7]
n=len(arr)
bubble_sort(arr,n)
print(arr)