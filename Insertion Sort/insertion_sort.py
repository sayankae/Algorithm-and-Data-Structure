#Insertion Sort
#Insertion sort in a inplace sort
#It sort the elements by inserting the element in the remaining sorted array and its correct place
#Time complexity is O(n*(n-1)) and Auxilary Space required is O(1)

def insertionSort(arr):
    for curr_index in range(1,len(arr)):
        temp = arr[curr_index]
        prev = curr_index-1
        while prev>=0:
            if arr[prev]>temp:
                arr[prev+1] = arr[prev]
                prev = prev-1
            else:
                arr[prev+1] = temp
                break
    return arr

if __name__ == "__main__":
    arr = [1,19,3,10,7,9,45,4,222]
    print(insertionSort(arr))
else:
    pass