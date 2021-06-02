tmp = '012'
base = 3

def change(n):
    q, r = divmod(n, base)
    if q == 0:
        return tmp[r]
    else:
        return change(q) + tmp[r]

def solution(n):
    return int(change(n)[::-1], base)