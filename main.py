 2. Library Management System

Topics: Dictionary
library = {}

while True:
    print("\n1.Add Book")
    print("2.View Books")
    print("3.Search Book")
    print("4.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        book = input("Book Name: ")
        author = input("Author: ")
        library[book] = author

    elif ch == 2:
        for b, a in library.items():
            print(b, "-", a)

    elif ch == 3:
        book = input("Enter Book Name: ")
        if book in library:
            print("Author:", library[book])
        else:
            print("Book Not Found")

    elif ch == 4:
        break
