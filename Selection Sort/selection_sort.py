#Selection Sort
#Selection sort in a inplace sort
#It sort the elements by selecting the next smallest number and then putting it after the sorted array
#Time complexity is O(n*(n-1)) and Auxilary Space required is O(1)

def selectionSort(arr):
    for curr_index in range(len(arr)-1):
        small = 1000000
        at_index = 0
        for next in range(curr_index,len(arr)):
            if small>arr[next]:
                at_index = next
                small = arr[next]

        temp = arr[curr_index]
        arr[curr_index] = small
        arr[at_index] = temp

    return arr

if __name__ == "__main__":
    arr = [1,19,3,10,7,9,45,4,222]
    print(selectionSort(arr))
else:
    pass
        