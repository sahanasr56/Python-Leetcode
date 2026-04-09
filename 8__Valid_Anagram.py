def isAnagram(s, t):
    map1={}
    map2={}
    for i,val in enumerate(s):
        map1[val]=map1.get(val, 0)+1
    for i,val in enumerate(t):
        map2[val]=map2.get(val, 0)+1
    return map1==map2

print(isAnagram("anagram", "nagaram"))