def selection_sort(arr,n):
    for i in range(n-1):
        min_I=i
        for j in range(i,n):
            if arr[j]<arr[min_I]:
                min_I=j
            
        if min_I!=i:
            temp=arr[i]
            arr[i]=arr[min_I]
            arr[min_I]=temp

arr=[10,5,2,8,7]
n=len(arr)
selection_sort(arr,n)
print(arr)