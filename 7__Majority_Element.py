def MajorityElement(nums):
    map1={}
    for i,val in enumerate(nums):
        map1[val]=map1.get(val,0)+1
    for key in map1:
        if map1[key]> len(nums)//2:
            return key

print(MajorityElement([2,2,1,1,1,2,2]))