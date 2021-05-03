def solution(n, lost, reserve):
    dic = {i:1 for i in range(1, n+1)}

    for l in lost:
        dic[l] -= 1
    for r in reserve:
        dic[r] += 1
        
    for d in dic:
        if dic[d] == 2:
            if d == 1 and dic[d + 1] == 0:
                dic[d] -= 1
                dic[d + 1] += 1
            elif d == n and dic[d - 1] == 0:
                dic[d] -= 1
                dic[d - 1] += 1
            elif d != 1 and dic[d - 1] == 0:
                dic[d] -= 1
                dic[d - 1] += 1 
            elif d != n and dic[d + 1] == 0:
                dic[d] -= 1
                dic[d + 1] += 1
                
    return n - list(dic.values()).count(0)