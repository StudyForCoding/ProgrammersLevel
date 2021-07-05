    def solution(numbers, hand)
        answer = ''
        #  = 10, 0 = 11, # = 12
        Lefthands = 10
        Righthands = 12
                
        for n in numbers   # numbers 안의 요소 접근
            # n이 1,4,7일 때  L
            if n in [1,4,7]    
                answer += L
                Lefthands = n
            # n이 3,6,9일 때  R
            elif n in [3,6,9]
                answer += R
                Righthands = n
            # n이 2,5,8,0일 때 
            
            else
                if n == 0
                    n = 11        
                
                L_dis = abs(Lefthands-n)%3 + abs(Lefthands-n)3
                R_dis = abs(Righthands-n)%3 + abs(Righthands-n)3
                if L_dis  R_dis
                    answer += R
                    Righthands = n
                elif L_dis  R_dis
                    answer += L
                    Lefthands = n
                else
                    if hand == left
                        answer += L
                        Lefthands = n
                    else
                        answer += R
                        Righthands = n
        return answer