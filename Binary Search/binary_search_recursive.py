#Binary Search Recursive Approach
#Binary Search only works on Sorted Array
#Binary Search compare the key with the pivot element and then set the boundaries for search
#Pivot is always the middle element
#Time complexity is O(logn) and Auxilary Space required is O(logn)

def binarySearch(arr,left,right,key):
    if left>right:
        return 
    else:
        mid = (left+right)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]>key:
            return binarySearch(arr,left,mid-1,key)
        else:
            return binarySearch(arr,mid+1,right,key)

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 5
    print(binarySearch(arr,0,len(arr)-1,key))
else:
    pass 