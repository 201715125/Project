def adder(numbers):        # 함수 선언, 매개변수명은 numbers
    
 total = 0           # 초기값 설정
 for i in numbers:       # for문 사용
     total = total + i    
 return total        # for문을 실행한 후에 total에 저장된 값을 반환

s = list(map(int,input("숫자를 입력하세요:").split()))    # 숫자를 입력받고 배열에 저장         

print(adder(s))    # 정의한 함수의 매개변수로 입력 받은 값 전달 및 출력


