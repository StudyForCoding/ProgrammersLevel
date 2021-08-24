#12947 ÇÏ»şµå ¼ö

def solution(x):
    answer = True
    arr = list(str(x))
    sum_arr = 0
    for i in range(len(arr)):
        sum_arr += int(arr[i])
    if x%sum_arr == 0:
        answer = True
    elif x%sum_arr != 0:
        answer = False
    return answer