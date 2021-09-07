#12939 ÃÖ´ñ°ª°ú ÃÖ¼Ú°ª

def solution(s):
    answer = ''
    new_s = s.split(' ')
    max_num = int(new_s[0])
    min_num = int(new_s[0])
    for i in range(len(new_s)):
        num = int(new_s[i])
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    answer = str(min_num) + ' ' + str(max_num)
    return answer