def bubble_sort(arr): #arr을 인수로하는 bubble_sort 함수 정의
    p = len(arr) # 편의를 위해 변수 설정
    for i in range(0,p-1,1): # 정렬 범위 설정 및 반복
        for j in range(0,p-1,1):# 내부 반복문: 앞뒤의 값을 비교하여 swap 반복
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1],arr[j] 
    return arr # 반환

a = list(map(int,input("숫자를 입력해주세요").split())) # 숫자를 입력받고 배열에 저장 
print(bubble_sort(a)) # 정의한 함수의 매개변수로 입력 받은 값 전달 및 출력

