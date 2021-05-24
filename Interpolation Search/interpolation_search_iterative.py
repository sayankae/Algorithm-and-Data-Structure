#Interpolation Search Iterative Approach
#Interpolation Search with sorted array
#Interpolation Search compare the key with each element
#Time complexity is O(logn) and Auxilary Space required is O(1)

def interpolationSearch(arr,key):
    left = 0
    right = len(arr)-1
    while left<=right and key>=arr[left] and key<=arr[right]:
        pos = left+((key-arr[left])*(right-left))//(arr[right]-arr[left])
        if arr[pos] == key:
            return pos
        elif arr[pos]>key:
            right = pos-1
        else:
            left = pos+1
    
    return "Not Found"

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 5
    print(interpolationSearch(arr,key))
else:
    pass
