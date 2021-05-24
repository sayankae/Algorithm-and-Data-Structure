#Ternary Search Recursive Approach
#Ternary Search with only sorted array
#Ternary Search divides the array into three parts i.e two mid or pivot and compare it with the two mid
#Time complexity is O(log3(n)) 

def ternarySearch(arr,left,right,key):
    if right<left:
        return "Not Found"
    else:
        first_part = left+(right-left)//3
        second_part = right-(right-left)//3

        if arr[first_part] == key:
            return first_part
        elif arr[second_part] == key:
            return second_part
        elif arr[first_part]>key:
            return ternarySearch(arr,left,first_part-1,key)
        elif arr[second_part]>key:
            return ternarySearch(arr,left,second_part-1,key)
        else:
            return ternarySearch(arr,second_part+1,right,key)


if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    key = 45
    print(ternarySearch(arr,0,len(arr)-1,key))
else:
    pass
