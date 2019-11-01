# Swap 2 elements of arr at indices i and j 
def swap(arr, i, j):
    arr[i] = arr[i] + arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] = arr[i] - arr[j]
    #arr[i],arr[j]=arr[j],arr[i]

# Recursively sort elements of arr using bubble sort
def boba_sort(arr):
    def aux(arr, acc=[]):
        if(arr == []):
            return acc

        f=False
        for i in range(0, len(arr)-1):
            if(arr[i] > arr[i+1]):
                f=True
                swap(arr, i, i+1)
        
        if(not f):
            acc=acc + arr
            arr=[]
            return aux(arr, acc) 

        acc=acc + [arr.pop(0)]
        return aux(arr, acc)
            
    return aux(arr)

print(boba_sort([1, 3, 4, 2, 6, 5]))

# Recursively sort elements of arr using selection sort
def selection_sort(arr):
    def aux(arr, acc=[]):
        if(arr == []):
            return acc

        maxElement=arr[0]
        maxIndex=0
        
        f=False

        for i in range(len(arr)-1):
            if(arr[i] > maxElement):
                f=True
                maxElement=arr[i]
                maxIndex=i

        if(f):
            swap(arr, maxIndex, len(arr)-1)

        acc=[arr.pop()]+acc
        return aux(arr, acc)

    return aux(arr)

print(selection_sort([1, 3, 4, 2, 6, 5]))

# Recursively sort elements of arr using insertion sort
def insertion_sort(arr):
    def aux(arr, acc=[]):
        if(arr == []):
            return acc
        
        maxElement=arr[0]
        maxIndex=0

        f=False

        for i in range(len(arr)):
            if(arr[i] > maxElement):
                f=True
                maxElement=arr[i]
                maxIndex=i

        if(not f):
            acc=arr+acc
            arr=[]
        else:
            acc=[arr.pop(maxIndex)]+acc

        return aux(arr, acc)

    return aux(arr)

print(insertion_sort([1, 3, 4, 2, 6, 5]))
