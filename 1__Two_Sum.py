def TwoSum (nums, target):
    hashMap={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[nums[i]]=i
        print(hashMap)

result=TwoSum([1,3,6,4], 5)
print(result)
