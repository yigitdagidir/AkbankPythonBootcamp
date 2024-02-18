import time 

class Library():
    def __init__(self) -> None:
        
        self.file=open("Books.txt","a+",encoding="utf-8")
        self.file.seek(0)
        
    def list_books(self):
        self.file.seek(0)
        file_str=self.file.read()
        if file_str=="":
            print("Library is EMPTY !")
            return
        book_lines=file_str.splitlines()

        for book_line in book_lines:
            book_info = book_line.split(",")
            book_name= book_info[0]
            book_author= book_info[1]
            print(f"Book: {book_name}\t\tAuthor: {book_author}")

        
    def add_book(self):
        book_info=[]
        for attribute in book_attributes:
            info=input(f"Enter the {attribute}: ").capitalize()
            book_info.append(info)
        book_name=book_info[0]
        book_info=",".join(book_info)
        self.file.write(book_info)
        self.file.write("\n")

        print(f"'{book_name.capitalize()}' is successfully added to the library.")


    def remove_book(self):
        book_name=input("Which book you want to remove?: ").lower()
        self.file.seek(0)
        file_str=self.file.read()
        book_lines=file_str.splitlines() # splitted lines
        removing_index=None

        for line_index,book in enumerate(book_lines):
            book_info = book.split(",") # splitted headings in a line
            if len(book_info) >=1 and book_info[0].strip().lower()== book_name:
                removing_index=line_index
                break
        
        if removing_index !=None:
            del book_lines[removing_index]
            self.file.seek(0)
            self.file.truncate(0)
            self.file.writelines("\n".join(book_lines))
            print(f"{book_name.capitalize()} is successfully removed from the library ")
        else:
            print(f"{book_name.capitalize()} is not in the library")
        

    
    def __del__(self):
        self.file.close()
        print(f"Thanks for using our library management system.")
        for i in range(shutdown_second):
            print(f"Closing in {shutdown_second-i} seconds")
            time.sleep(1)


def MainMenu(): 
    print(f"""*** MENU ***
    1) List Books
    2) Add book
    3) Remove book
    Press 'q' to quit""")

def ReturnMainMenu():
    choice=input("Press 'm' key to return to the Main Menu: ").lower()
    if choice.lower()=="m":
        return # exits the function here and then will continue in the main loop. must add continue after func
    else: ReturnMainMenu()   # function will repeat until input is 'm'         

lib=Library()
shutdown_second=3
book_attributes=["Book Title","Book Author","Released Year","Number of Pages"] # attributes of a book

while True:
    try:
        MainMenu()
        option=input("Choose your option: ").lower()
        if option=="1": # listing books
            lib.list_books()
            ReturnMainMenu()

        elif option=="2": # adding books
            lib.add_book()       
            ReturnMainMenu()
            continue

        elif option=="3": # removing books
            lib.remove_book()
            ReturnMainMenu()
            continue
        
        elif option=="q":
            del lib
            break
    except:
        print(f"Enter one of the available option")