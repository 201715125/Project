a = list(map(int,input("array: ").split()))         # 배열 입력 받기
c = list(map(int,input("i, j, k: ").split()))

def solution(array, commands):                 # array, commands를 인수로 하는 함수 선언
    i = commands[0]                            # 배열의  0, 1 ,2번째 요소 입력받기
    j = commands[1]                             
    k = commands[2]
    
    array = array[i-1:j]                       # slice: 0번째 요소가 존재하므로 i-1
    array.sort()                               # sort 함수로 정렬
    result = array[k-1]                        # k-1 번째 요소 추출
    return result                              # 결과값 반환

print(solution(a, c))