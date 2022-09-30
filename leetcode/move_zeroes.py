# def moveZeroes(self, nums):
#     res = [0]*len(nums)
#     i,j = 0,len(nums)-1
#     k = 0
#     while i <= j:
#         if nums[k] == 0:
#             res[j] = nums[k]
#             j-=1
#         else:
#             res[i] = nums[k]
#             i+=1
#         k+=1
def moveZeroes(self, nums):
    i,j=0,0
    while j < len(nums):
        if nums[j] != 0:
            (nums[i],nums[j]) = (nums[j],nums[i])
            i+=1
        j+=1
    return nums

assert moveZeroes(None,[0,1,0,3,12]) == [1,3,12,0,0]
assert moveZeroes(None,[0]) == [0]
assert moveZeroes(None,[1,0,0]) == [1,0,0]
assert moveZeroes(None,[0,0,1]) == [1,0,0]
assert moveZeroes(None,[1,0,1]) == [1,1,0]
