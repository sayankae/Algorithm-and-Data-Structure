#Merge Sort
#Merge sort in not a inplace sort
#It sort the elements by using divide and conquer method 
#Time complexity is O(nlogn) and Auxilary Space required is O(n)

def mergeSort(arr,left,right):
    if left<right:
        pivot = (left+right)//2
        mid = (len(arr))//2
        left_part = arr[:mid]
        right_part = arr[mid::]
        mergeSort(left_part,left,pivot)
        mergeSort(right_part,pivot+1,right)
        i = 0
        j = 0
        k = 0
        while i<len(left_part) and j<len(right_part):
            if left_part[i]<right_part[j]:
                arr[k] = left_part[i]
                i = i+1
            else:
                arr[k] = right_part[j]
                j = j+1
            k = k+1

        if i<len(left_part):
            arr[k] = left_part[i]
            k = k+1
            i = i+1
        if j<len(right_part):
            arr[k] = right_part[j]
            k = k+1
            j = j+1
        return arr
    else:
        return arr

if __name__ == "__main__":
    arr = [1,19,3,10,7,9,45,4,222]
    print(mergeSort(arr,0,len(arr)-1))
else:
    pass