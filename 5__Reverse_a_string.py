# with O(1) space - no extra array/string
def ReverseString(s):
    left, right=0, len(s)-1
    while left<right:
        s[left], s[right]=s[right], s[left]
        left +=1
        right -=1
    return s

print(ReverseString(["o","l","l","e","H"]))