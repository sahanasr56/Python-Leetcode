# First Unique Character in a String (return Index)
def FirstUniqueCh (s):
    hashmap={}
    for i, val in enumerate(s):
        hashmap[val]=(hashmap.get(val, 0))+1
    for i, val in enumerate(s):
        if hashmap[val]==1:
            return i
    return -1

print(FirstUniqueCh("leetcode"))