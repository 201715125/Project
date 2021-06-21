
import os # 모듈 불러오기


class catalog:
    def __init__(self):
        self.catalog = []

    def catalogGet(self):
        try:
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # 파일의 절대경로 리턴
            bookfile = os.path.join(THIS_FOLDER, 'input.txt') # input.txt 파일과 경로 결합
            Bookdata = open(bookfile, 'r') #bookfile 읽어들이기
            while True: 
                    Book_read = Bookdata.readline()   
                    if not Book_read:
                        break
                    Book_list = Book_read.split()
                    self.catalog.append(Book_list)
            Bookdata.close()
            return self.catalog
        except:
            pass