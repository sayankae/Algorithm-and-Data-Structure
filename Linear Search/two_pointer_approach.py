#Two Pointer Approach
#Two pointer approach is mainly used for searching pairs in an sorted array
#The pointer can start from starting index or starting and ending according to the need of question
#Time complexity is O(n) and Auxilary Space required is O(1)

def twoPointer(arr,x):
    left = 0
    right = len(arr)-1
    ans = []
    while left<right:
        if arr[left]+arr[right] == x:
            ans.append([arr[left],arr[right]])
            left = left+1
            right = right-1
        elif arr[left]+arr[right]>x:
            right = right-1
        else:
            left = left+1

    if len(ans) == 0:
        return "Not Found any pair"
    else:
        return ans

if __name__ == "__main__":
    arr = [1,2,3,4,7,9,45,56,222]
    x = 11
    print(twoPointer(arr,x))
else:
    pass