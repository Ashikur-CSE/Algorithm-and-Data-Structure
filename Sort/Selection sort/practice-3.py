def selection_sort(arr,n):
    for i in range(n-1):
        min_index=i
        for j in range(i,n):
            if arr[j]<arr[min_index]:
                min_index=j
            if min_index!=i:
                temp=arr[i]
                arr[i]=arr[min_index]
                arr[min_index]=temp


arr=[10,5,2,8,7]
n=len(arr)
selection_sort(arr,n)
print(arr)