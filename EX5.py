N = int(input())       # 입력 받기

for _ in range(N):
    t = N
    count_list = [1,2,3]

    for i in range(4, t+1):            # N이 4이상인 경우 t-1과 t-2인 경우의 합
        i = count_list[-1] + count_list[-2]
        count_list.append(i)

    if t == 1:      # 입력 숫자가 4 이하일 경우 개수 정의(예를들어, T = 3인 경우 result = 2 )
        result = 1
    elif t == 2:
        result = 2 
    elif t == 3: 
        result = 3
    else:
        result = count_list[-1] 
            
print(result)       