def search(nums, target):
    low,high = 0,len(nums)-1
    while(low<=high):
        mid = (low+high)//2
        if target == nums[mid]:  return mid
        if target < nums[mid]:   high = mid - 1
        elif target > nums[mid]: low = mid + 1
    return -1

bad = 1
def isBadVersion(n): return n>=bad
def firstBadVersion(n):
    l,h = 1,n
    while l<=h:
        m=(l+h)//2
        if isBadVersion(m) == False and isBadVersion(m+1) == True: return m+1
        elif isBadVersion(m) == True:h=m-1
        else: l = m+1
    return 1
    
def searchInsert(nums, target):
    low,high=0,len(nums)-1
    while low<=high:
        mid=(low+high) // 2
        if target==nums[mid]:return mid
        if target < nums[mid] : high = mid - 1
        elif target > nums[mid] : low = mid + 1
    return low

nums = [1,3,5,6]
t = 3
print(searchInsert(nums,t))