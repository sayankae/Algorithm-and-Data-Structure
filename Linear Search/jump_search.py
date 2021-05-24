#Jump Search
#Jump Search only works on the sorted array
#In Jump Search, searching happens by skipping sqrt(sizeOfArray) index until the key is found
#If key is is smaller than the given element then linearly search upto m space backward until key is found
#Time complexity is O(sqrt(n)) and Auxilary Space required is O(1)
import math

def jumpSearch(arr,key):
    jump = math.floor(math.sqrt(len(arr)))
    curr = 0
    while curr<len(arr):
        if arr[curr] == key:
            return curr
        elif arr[curr]>key:
            while jump>0:
                if arr[curr-jump] == key:
                    return curr-jump
                else:
                    jump = jump-1
            return "Not Found"
        else:
            curr = curr+jump

    return "Not found"

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 2
    print(jumpSearch(arr,key))
else:
    pass