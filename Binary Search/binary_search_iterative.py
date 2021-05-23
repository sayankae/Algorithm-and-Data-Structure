#Binary Search Iterative Approach
#Binary Search only works on Sorted Array
#Binary Search compare the key with the pivot element and then set the boundaries for search
#Pivot is always the middle element
#Time complexity is O(logn) and Auxilary Space required is O(1)

def binarySearch(arr,key):
    if len(arr) == 0:
        return "No elements in array"
    else:
        left = 0
        right = len(arr)-1
        index = None
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == key:
                index = mid
                break
            elif arr[mid]>key:
                right = mid-1
            else:
                left = mid+1
        if index == None:
            return "Element Not Found" 
        else:
            return index 

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 222
    print(binarySearch(arr,key))
else:
    pass