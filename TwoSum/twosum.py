def twoSum(nums,target):
    map = {}
    #Building the #Map
    for i in range(0,len(nums)):
        map[nums[i]] = i

    for i in range(0,len(nums)):
        complement = target-nums[i]
        if (complement in map and i != map[complement]):
            return [i,map[complement]]

print(twoSum([1,3,5,6],7))