#17681 비밀지도

def solution(n, arr1, arr2):
    answer = []
    arr1_ch = []
    arr2_ch = []
    for i in range(n):
        arr1_ch.append(bin(arr1[i])[2:])
        arr2_ch.append(bin(arr2[i])[2:])
        arr1_ch[i] = '0' * (n-len(arr1_ch[i])) + arr1_ch[i]
        arr2_ch[i] = '0' * (n-len(arr2_ch[i])) + arr2_ch[i]
        
        txt = ''

        for j in range(n):
            if arr1_ch[i][j] == '1' or arr2_ch[i][j] == '1':
                txt += '#'
            elif arr1_ch[i][j] == '0' and arr2_ch[i][j] == '0':
                txt += ' '
        
        answer.append(txt)
    
    return answer