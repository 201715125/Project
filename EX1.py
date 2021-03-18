number = input("양의 정수 입력")
number = int(number)

if number % 2 == 0: # 짝수는 2로 나누면 나머지가 0인것을 활용
    print("짝수")

if number % 2 == 1: # 홀수는 2로 나누면 나머지가 1인것을 활용 
    print("홀수")

if number <= 0 : # 0 이하의 수를 입력했을시 오류
    print("ERROR: 양의 정수를 입력해주세요")   

