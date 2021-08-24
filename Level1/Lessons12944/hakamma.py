#12944 Æò±Õ ±¸ÇÏ±â

def solution(arr):
    answer = 0
    sum_arr = 0
    for i in range(len(arr)):
        sum_arr += (arr[i])
    answer = float(sum_arr) / float(len(arr))
    return answer