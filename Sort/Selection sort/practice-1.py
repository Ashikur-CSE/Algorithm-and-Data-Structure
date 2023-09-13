def selection_sort(arr,n):
    for i in range(n-1):
        min=i
        for j in range(i,n):
            if arr[j]<arr[min]:
                min=j
            
            if i!=min:
                temp=arr[i]
                arr[i]=arr[min]
                arr[min]=temp






arr=[10,5,2,8,7]
n=len(arr)
selection_sort(arr,n)
print(arr)