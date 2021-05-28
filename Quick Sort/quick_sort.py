#Quick Sort
#Quick Sort is an inplace sort in its different version
#It sort the elements by arranging all the smaller elements to its one side and bigger element to the other side by comparing with a pivot
#Time complexity is θ(nlogn) and O(n*n) and Auxilary Space required is O(n) during recursion

def quickSort(arr,left,right):
    if left<right:
        pivot = partition(arr,left,right)
        arr = quickSort(arr,left,pivot-1)
        arr = quickSort(arr,pivot+1,right)
        return arr
    else:
        return arr


def partition(arr,left,right):
    pivot = arr[left]
    i = left+1
    j = right
    while i<j:
        while arr[i]<pivot:
            i = i+1
        while arr[j]>pivot:
            j = j-1
        if i<j:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    
    temp = arr[j]
    arr[j] = arr[left]
    arr[left] = temp
    return j

if __name__ == "__main__":
    arr = [1,19,3,10,7,9,45,4,222]
    print(quickSort(arr,0,len(arr)-1))
else:
    pass