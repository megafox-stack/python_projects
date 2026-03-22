library = {} 
total_book = 5   
def add_book(book_id,book):
  if book_id in library:
    library[book_id]["copies"]+=1
    print("book already present!copy added")
  else:
     library[book_id] = {"name":book,"copies":0}
     print("new entry added!")

def view_book():
  for book_id,details in library.items():
    print("Book ID:", book_id)
    print("Book Name:", details["name"])
    print("Copies:", details["copies"])
    print("-----")

def issue_book(details):
  if(details["copies"] > 0):
    print("book issued!")
    details["copies"]-=1
  else:
    print("we ran out of copies!sorry")

def return_book(book_id,details,total_book):
  if book_id in library:
    if details["copies"] < total_book:
      library[book_id]["copies"]+=1
      print("book returned!copy added")
    else:
      print("cannot return:max copies reached!")
  else:
    print("book not found!")
             
  
def search_book(key):
  if key in library:
     details = library[key]
     print("Book ID:",key)
     print("Book Name:",details["name"])
     print("Copies:",details["copies"])
     print("-----")
  else:
    print("the book id does not exist!") 

   
                                
while True:
    print("python library")
    print("what services can we offer u:\n1.add book\n2.view all books\n3.issue book\n4.return book\n5.search book\n6.exit")
    choice = int(input("enter ur choice:"))
    if choice == 1:
     book_id = int(input("enter the book id:"))
     book = input("enter the book name:")
     add_book(book_id,book)
    elif choice == 2:
     view_book()
    elif choice == 3:
     issue_book(library[book_id])
    elif choice == 4:
     return_book(book_id,library[book_id],total_book)
    elif choice == 5:
      key = int(input("enter the book id to search:"))
      search_book(key)  
    else:
      print("exiting python library!visit us again")
      break    

