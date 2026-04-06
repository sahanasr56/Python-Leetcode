def Duplicate(nums):
    # return len(nums)!=lens(set(nums))
    map1={}
    for i, val in enumerate(nums):
        if val in map1:
            return True
        map1[val]=i
    return False

print(Duplicate(['1','2','3','1']))