class Node:     # 단순 연결 리스트를 위한 노드 클래스
    def __init__(self, elem, next = None):
        self.data = elem
        self.link = next
    
    def append(self, new):  # 현재 노드 다음에 new 노드를 삽입
        if new is not None:
            new.link = self.link
            self.link = new
    
    def popNext(self):  # 현재 노드의 다음 노드를 삭제한 후 변환
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node

class LinkedList:   # 단순 연결 리스트 클래스
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        # 리스트의 빈 상태 검사
        return self.head == None

    def isFull(self):
        # 리스트의 포화 상태 검사
        return False
    
    def getNode(self, pos):
        # pos 위치에 있는 노드를 반환
        if pos < 0:
            return None
        if self.head == None:
            return None
        else:
            ptr = self.head
            for _ in range(pos):
                if ptr == None:
                    return None
                ptr = ptr.link
            return ptr
    
    def getEntry(self, pos):
        # 리스트으 pos 위치에 있는 노드를 찾아 데이터 값을 반환
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
    
    def insert(self, pos, elem):
        # pos 위치에서 새 노드(elem) 삽입 연산
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        
        new = Node(elem)
        before = self.getNode(pos-1)

        if before is None:
            if pos == 0:     
                new.link = self.head
                self.head = new
                return
            else:
                raise IndexError("삽입할 위치가 유효하지 않음!")
        else:
            before.append(new)

    def delete(self, pos):
        # pos 위치에서 해당 노드 삭제한 후  그 노드 반환
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        
        before = self.getNode(pos-1)
        
        if before == None:
            if pos == 0:
                delete = self.head
                self.head = delete.link
                delete.link = None
                return delete
            else:
                raise IndexError("삽입할 위치가 유효하지 않음!")
        else:
            return before.popNext()
    
    def size(self):
        # 리스트의 전체 노드의 갯수
        if self.head == None:
            return 0
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count

    def display(self, msg = "LinkedList:"):
        # 리스트의 내용을 출력
        print(msg, end=" ")
        if self.head == None:
            return 0
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, end=" -> ")
                ptr = ptr.link
            print("None")

    def replace(self, pos, elem):
        # 리스트의 pos 위치에 있는 노드의 데이터 필드를 수정
        node = self.getNode(pos)
        if node != None:
            node.data = elem
    
    def find_by_title(self, title):
        # 책 제목으로 리스트에서 도서를 찾기
        ptr = self.head
        
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data
            ptr = ptr.link
        return None
    
    def find_pos_by_title(self, title):
        # 책 제목으로 리스트에서 도서의 위치를 찾기
        pos = 0
        ptr = self.head
        
        while ptr is not None:
            if ptr.data.title == title:
                return pos
            ptr = ptr.link
            pos += 1
        return -1
    
    def find_by_book_id(self, book_id):
        ptr = self.head
    
        while ptr is not None:
            if ptr.data.book_id == book_id:
                return ptr.data
            ptr = ptr.link
        return None

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"[책 번호 : {self.book_id}, 제목 : {self.title}, 저자 : {self.author}, 출판 연도 : {self.year}]"

class BookManagement:
    def __init__(self):
        self.books = LinkedList()
    
    def add_book(self, book_id, title, author, year): # 1. 도서 추가
        if self.books.find_by_book_id(book_id) is not None:
            print(f"오류! 책 번호 '{book_id}'은(는) 이미 존재합니다. ")
            return
        
        new_book = Book(book_id, title, author, year)
        
        pos = self.books.size()
        self.books.insert(pos, new_book)
        
        print(f"도서 '{title}'이(가) 추가되었습니다. ")
    
    def remove_book(self, title):   # 2. 도서 삭제 (책 제목으로 삭제)
        pos = self.books.find_pos_by_title(title)
        
        if pos == -1:
            print(f"오류! '{title}' 제목의 도서를 찾을 수 없습니다. ")
        else:
            self.books.delete(pos)
            print(f"책 제목 '{title}'의 도서가 삭제되었습니다. ")
    
    def search_book(self, title):   # 3. 도서 조회 (책 제목으로 조회)
        book = self.books.find_by_title(title)
        
        if book:
            print(book)
        else:
            print(f"오류! '{title}' 제목의 도서를 찾을 수 없습니다. ")
    
    def display_books(self):    # 전체 도서 목록 조회
        if self.books.isEmpty():
            print("현재 등록된 도서가 없습니다. ")
            return
        
        print("현재 등록된 도서 목록 : ")
        ptr = self.books.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link
    
    def run(self):
        while True:
            print("\n === 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 조회")
            print("5. 종료")
            
            menu = input("메뉴를 선택하세요 : ")
            
            try:
                if menu == "1":
                    book_id = input("책 번호 : ")
                    title = input("책 제목 : ")
                    author = input("저자 : ")
                    year = input("출판 연도 : ")
                    
                    self.add_book(book_id, title, author, year)
                elif menu == "2":
                    title = input("삭제할 책 제목을 입력하세요 : ")
                    
                    self.remove_book(title)
                elif menu == "3":
                    title = input("조회할 책 제목을 입력하세요 : ")
                    
                    self.search_book(title)
                elif menu == "4":
                    self.display_books()
                elif menu == "5":
                    print("프로그램을 종료합니다.")
                    break
                else:
                    print("오류! 1~5 사이의 숫자를 입력하세요. ")
            except Exception as e:
                print(f"오류가 발생했습니다. {e}")
if __name__ == "__main__":
    bookmanagement = BookManagement()
    bookmanagement.run()