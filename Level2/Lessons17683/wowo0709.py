# [3차] 빙금그곡

# 1분당 음 1개, 반복 가능
# 조건 일치 곡이 여러 개일 경우 재생 시간이 가장 긴 음악 반환, 시간도 같을 경우 먼저 입력된 음악 반환

# 각 곡 정보에 대해 음을 재생 시간만큼 늘리거나 줄인다. 
# 들은 음이 각 곡에 있는 지 검사한다. 
# 없을 경우, 여러 개 있을 경우 등에 대한 처리를 해준다. 

def solution(m,musicinfos):
    scaleList = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # 12음계
    numList = ['0','1','2','3','4','5','6','7','8','9','a','b'] # 12진법
    scaleDict = dict(zip(scaleList,numList))
    musicList = []
    for musicinfo in musicinfos:
        startTime, endTime, title, scales = musicinfo.split(',')
        playtime = (int(endTime[0:2]) - int(startTime[0:2])) * 60 + (int(endTime[3:]) - int(startTime[3:]))
        
        for scale in scaleList[::-1]: # '#'음들을 먼저 변환해야 함
            scales = scales.replace(scale,scaleDict[scale])
        
        q,r = divmod(playtime,len(scales)) # 전체재생수,추가재생시간
        scales = scales*q + scales[:r]

        musicList.append([playtime,title,scales])

    # m도 변환
    for scale in scaleList[::-1]: m = m.replace(scale,scaleDict[scale])
    # 재생시간이 긴 순으로 정답 반환 (문제 조건)
    for playtime, title, scales in sorted(musicList,key = lambda music: music[0], reverse=True):
        if m in scales: return title
    return "(None)"


'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.5MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.05ms, 10.4MB)
테스트 6 〉	통과 (0.05ms, 10.5MB)
테스트 7 〉	통과 (0.13ms, 10.4MB)
테스트 8 〉	통과 (0.12ms, 10.4MB)
테스트 9 〉	통과 (0.12ms, 10.4MB)
테스트 10 〉	통과 (0.14ms, 10.4MB)
테스트 11 〉	통과 (0.11ms, 10.3MB)
테스트 12 〉	통과 (0.16ms, 10.4MB)
테스트 13 〉	통과 (0.13ms, 10.5MB)
테스트 14 〉	통과 (0.13ms, 10.4MB)
테스트 15 〉	통과 (0.13ms, 10.4MB)
테스트 16 〉	통과 (0.12ms, 10.4MB)
테스트 17 〉	통과 (0.13ms, 10.5MB)
테스트 18 〉	통과 (0.13ms, 10.4MB)
테스트 19 〉	통과 (0.14ms, 10.3MB)
테스트 20 〉	통과 (0.13ms, 10.5MB)
테스트 21 〉	통과 (0.11ms, 10.4MB)
테스트 22 〉	통과 (0.12ms, 10.4MB)
테스트 23 〉	통과 (0.13ms, 10.4MB)
테스트 24 〉	통과 (0.12ms, 10.4MB)
테스트 25 〉	통과 (0.05ms, 10.4MB)
테스트 26 〉	통과 (0.06ms, 10.4MB)
테스트 27 〉	통과 (0.06ms, 10.4MB)
테스트 28 〉	통과 (0.05ms, 10.4MB)
테스트 29 〉	통과 (1.75ms, 10.5MB)
테스트 30 〉	통과 (1.67ms, 10.5MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''