#Ternary Search Iterative Approach
#Ternary Search with only sorted array
#Ternary Search divides the array into three parts i.e two mid or pivot and compare it with the two mid
#Time complexity is O(log3(n)) and Auxilary Space required is O(1)

def ternarySearch(arr,key):
    left = 0
    right = len(arr)-1
    while left<=right:
        first_part = left+(right-left)//3
        second_part = right-(right-left)//3

        if arr[first_part] == key:
            return first_part
        elif arr[second_part] == key:
            return second_part
        elif arr[first_part]>key:
            right = first_part-1
        elif arr[second_part]>key:
            right = second_part-1
        else:
            left = second_part+1
    
    return "Not Found"

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 5
    print(ternarySearch(arr,key))
else:
    pass