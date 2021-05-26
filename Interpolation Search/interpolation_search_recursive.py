#Interpolation Search Recursive Approach
#Interpolation Search with sorted array
#Interpolation Search compare the key with each element
#Time complexity is O(logn) and Auxilary Space required is O(1)

def interpolationSearch(arr,key,left,right):
    if left<=right and key>=arr[left] and key<=arr[right]:
        pos = left+((key-arr[left])*(right-left))//(arr[right]-arr[left])
        if arr[pos] == key:
            return pos
        elif arr[pos]>key:
            return interpolationSearch(arr,key,left,pos-1)
        else:
            return interpolationSearch(arr,key,pos+1,right)
    else:
        return "Not Found"

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 56
    print(interpolationSearch(arr,key,0,len(arr)-1))
else:
    pass