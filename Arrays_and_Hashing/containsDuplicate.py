def containsDuplicate(nums):
    num = set()
    for i in range(0,len(nums)):
        num.add(nums[i])
    if(len(num)==len(nums)):
        return False
    return True

print(containsDuplicate([1,2,1,3]))