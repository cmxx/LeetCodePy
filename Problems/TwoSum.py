#
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hashmap:
            return [hashmap[compliment], i]
        hashmap[nums[i]] = i
        print(hashmap)



test = [2, 5, 3, 6, 7]
target = 12
print(twoSum(test,target))