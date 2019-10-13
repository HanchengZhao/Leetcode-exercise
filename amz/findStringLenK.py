####### Find substring with k distict characters
def findStringLengthK(input, k):
    if k == 0 or not input: return []
    exist = {}
    ret = []
    lo = 0
    for i in range(len(input)):
        if input[i] in exist:
            idx = exist[input[i]]
            for j in range(lo, idx): exist.pop(input[j])
            lo = idx+1
        else: 
            if i - lo + 1 > k: 
                exist.pop(input[lo])
                lo += 1
        exist[input[i]] = i
        if i-lo+1 == k: ret.append(input[lo:i+1])    
    return ret

input = "barfoothefoobarman"
k = 4
print(findStringLengthK(input, k))