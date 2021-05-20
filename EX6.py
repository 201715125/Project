  
class Library: # 도서관리 클래스
    def __init__(self):
        pass
    def addbook(self): #도서 정보 입력함수
        library.add()
    def searchbook(self): #도서 검색 
        library.search() 
    def renewbook(self): #도서 정보 수정
        library.renew() 
    def deletebook(self): #도서 삭제
        library.delete()
    def printbook(self): # 도서 목록 출력
        library.present()
    def out(self): #프로그램 종료함수
        print("프로그램 종료")


import library #bookcare 파일 import
while True: 
    L = Library() #객체
    print("1. 도서 추가 \n2. 도서 검색 \n3. 도서 정보 수정 \n4. 도서 삭제 \n5. 현재 총 도서 목록 출력  \n6. 프로그램 종료")
    number = int(input("번호를 선택하세요: " ))
    if number == 1:
        L.addbook()
    elif(number == 2):
        L.searchbook()
    elif(number == 3):
        L.renewbook()
    elif(number == 4):
        L.deletebook()
    elif(number == 5):
        L.printbook()
    elif(number == 6):
        break
L.out() 