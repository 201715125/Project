import sys
import os
import Book

class System: #class 선언
    def __init__(self,catalog):
        self.catalog = catalog
        self.Addcatalog = []
        self.Book = []
       
   
        
    def Menu(self):
        try:
            print("1. 추가")
            print("2. 검색")
            print("3. 수정")
            print("4. 삭제")
            print("5. 현재 목록 출력")
            print("6. 저장") 
            print("7. 종료")  
            choose = int(input("입력 : "))
            if choose == 1 :
                self.AddBook()
            elif choose == 2:
                self.searchBook()
            elif choose == 3:
                self.renewBook()
            elif choose == 4:
                self.deleteBook()
            elif choose == 5:
                self.showBook()
            elif choose == 6:
                self.save()
            elif choose == 7:
                self.Exit()    
            else:
                print("1부터 7까지의 숫자 입력")
                return self.Menu() 
        except ValueError:
            print("오류")
            return self.Menu()         



    def AddBook(self): # 추가기능 구현
        print("추가할 도서 입력: 도서명, 저자, 출판연도, 출판사, 장르순")
        addInput = list(map(str,input("입력 : ").split())) # 여려개 입력받기
        self.catalog.append(addInput) # append로 추가
        self.Addcatalog.append(addInput)
        print("추가 완료")
        return self.Menu()

    def searchBook(self): # 검색기능 구현
        searchnumber = int(input("0.도서명, 1.저자, 2.출판연도, 3.출판사, 4.장르 \n 번호 입력:")) # 베열이므로 0번부터 
        realsearch = input("검색: ")
        if realsearch == self.catalog[0][searchnumber]: # txt 파일 첫째줄 카테고리별로 나눠서 realsearch와 같은지 확인 
            print(self.catalog[0])                      # 맞으면 첫째줄 출력
        elif realsearch == self.catalog[1][searchnumber]:
            print(self.catalog[1])
        elif realsearch == self.catalog[2][searchnumber]:
            print(self.catalog[2])
        elif realsearch == self.catalog[3][searchnumber]:
            print(self.catalog[3])
        elif realsearch == self.catalog[4][searchnumber]:
            print(self.catalog[4])
        elif realsearch == self.catalog[5][searchnumber]:
            print(self.catalog[5])                    
        else: 
                print("다시 입력") 
                self.searchBook()

    def renewBook(self): # 수정기능 구현
        renewInput = str(input("수정 도서명 입력:"))  
        if renewInput == self.catalog[0][0]:
            newinfo1 = list(map(str,input("입력(도서명,저자,출판연도,출판사,장르 순으로) : ").split()))
            self.catalog[0] = newinfo1
        elif renewInput == self.catalog[1][0]:
            newinfo2 = list(map(str,input("입력(도서명,저자,출판연도,출판사,장르 순으로) : ").split()))
            self.catalog[1] = newinfo2
        elif renewInput == self.catalog[2][0]:
             newinfo3 = list(map(str,input("입력(도서명,저자,출판연도,출판사,장르 순으로) : ").split()))
             self.catalog[2] = newinfo3
        elif renewInput == self.catalog[3][0]:
             newinfo4 = list(map(str,input("입력(도서명,저자,출판연도,출판사,장르 순으로) : ").split()))
             self.catalog[3] = newinfo4                  
        elif renewInput == self.catalog[4][0]:
            newinfo5 = list(map(str,input("입력(도서명,저자,출판연도,출판사,장르 순으로) : ").split()))
            self.catalog[4] = newinfo5
        elif renewInput == self.catalog[5][0]:
            newinfo6 = list(map(str,input("입력(도서명,저자,출판연도,출판사,장르 순으로) : ").split()))
            self.catalog[5] = newinfo6
        return self.Menu()        

             
              
           
    def deleteBook(self): #삭제기능 구현
        for i in range(len(self.catalog)): #첫쨰줄부터 번호 지정
            print(i)
            print(self.catalog[i]) # 리스트 출력 
        number = int(input("삭제 도서 번호 입력: ")) 
        self.catalog.pop(number) # number번째 요소를 반환하고 삭제
        print("삭제 완료")
        return self.Menu()  


    def showBook(self): # 목록출력기능 구현
        for i in range(len(self.catalog)):
            print(self.catalog[i])  

        return self.Menu()
    

    def save(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        mofile = os.path.join(THIS_FOLDER, 'input.txt')
        Bookcatalog = open(mofile,'w')
        for i in range(len(self.catalog)):
            Bookcatalog.writelines(' '.join(self.catalog[i]))
            Bookcatalog.writelines('\n')
        Bookcatalog.close()

    def Exit(self): # 프로그램 종료
        print("종료.")
        sys.exit()
        
BookSet = Book.catalog() 
BookSet.catalogGet()
BookSystem = System(BookSet.catalog)
BookSystem.Menu()