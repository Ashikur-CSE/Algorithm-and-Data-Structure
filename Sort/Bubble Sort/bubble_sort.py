def bubble_sort(arr,n,count):
    for i in range(n):
        for j in range(n-i-1):
            count=count+1
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                


arr=[10,5,2,8,7]
n=len(arr)
count=0
bubble_sort(arr,n,count)
print(arr)
print(count)


# Time Complexity: O(n^2)