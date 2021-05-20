def add(): # 추가 기능
    book = input("도서명, 저자, 출판연도, 장르 순서대로 입력세요: ") #책의 입력받기
    read = open("C:/파이선/input.txt","a") # input.txt 파일 불러오기
    read.write("\n"+ book) #입력받은 책의 정보 저장
    print("도서추가 완료했습니다.")
    read.close()
def search(): # 검색 기능
    import glob # 모듈 불러오기
    import re 

    search_book = input("검색: ")

    booklist = re.compile(search_book) 

    for i in glob.glob(r"C:/파이선/input.txt"):
        with open(i, "r") as read:
           for x, y in enumerate(read.readlines(),1):
               Check_book = booklist.findall(y) 
               if Check_book: 
                print("관련 도서목록 : %s" %y) 
           print()
def renew(): # 수정 기능
    newinfo = " "
    before = input("수정할 단어: ")
    after = input("수정후 단어: ")
    with open("C:/파이선/input.txt","r") as read:
        booklist1 = read.readlines() #전체 도서 목록 저장
        for i, l in enumerate(booklist1):# 해당 도서명을 번호로 나열
            newword = l.strip().replace(before, after) #before를 after로 대체
            if newword: 
                newinfo += newword + "\n" 
            else: 
                newinfo += "\n" 
    with open("C:/파이선/input.txt","w") as read:
        read.write(newinfo)
    print("수정완료.")
def delete(): # 삭제 기능
    with open("C:/파이선/input.txt","r") as kiki:
        lines = kiki.readlines() 
    read = open("C:/파이선/input.txt","r")
    book_num = 1
    line = read.readline()
    while line:   # 도서목록을 번호대로 출력
        print("%d. %s" %(book_num,line))
        line =read.readline()
        book_num += 1 
    read.close
    eli = int(input("삭제할 번호를 입력하세요: "))
    with open("C:/파이선/input.txt","w") as outfile:
        for i, line in enumerate(lines): # 번호 일치시 삭제
            if i != eli-1: 
                outfile.write(line) 
    print("삭제되었습니다. \n")
def present(): # 현재 목록 출력 기능
    read = open("C:/파이선/input.txt","r")
    show = read.read()
    print(show)
    read.close()