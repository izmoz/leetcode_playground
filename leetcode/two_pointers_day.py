def sortedSquares(nums):
    left, right = 0, len(nums) - 1
    res = [0]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        if abs(nums[left]) > abs(nums[right]):
            res[i] = nums[left]**2
            left+=1
        else:
            res[i] = nums[right]**2
            right-=1
    return res

# Bad solution
# def rotate(self, nums, k):
#     for i in range (k):
#         n = nums[0]
#         nums[0]=nums[-1]
#         for j in range(1,len(nums)):
#             (n,nums[j]) = (nums[j],n)

# Better one
# def rotate(self, nums, k):
#     m=[0] * len(nums)
#     for i in range(len(nums)):
#         m[(i+k)%len(nums)] = nums[i]
#     for i in range(len(nums)):
#         nums[i]=m[i]
#     print(nums)

def rev(m, i, j):
    while i<j:
        (m[i],m[j]) = (m[j],m[i])
        i+=1
        j-=1

# The best solution
def rotate(self, nums, k):
    if k > len(nums):k%=len(nums)
    rev(nums,0,len(nums)-1)
    rev(nums,0,k-1)
    rev(nums,k,len(nums)-1)
    print(nums)

nums = [-1,-100,3,99]
# nums = [-1,-100,3,99]
rotate(None,nums,2)
