#Linear Search Iterative Approach
#Linear Search with both sorted and unsorted array
#Linear Search compare the key with each element
#Time complexity is O(n) and Auxilary Space required is O(1)

def linearSearch(arr,key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index
    
    return "Not Found"

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 45
    print(linearSearch(arr,key))
else:
    pass
