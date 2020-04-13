def mergesort(arr): #this is first method of merge sort
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergesort(L)
        mergesort(R)
        merge(arr,L,R)
    return arr

def merge(arr,L,R):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1

arr=[1,6,8,1,0,1,1,4,0,2]
print(mergesort(arr))