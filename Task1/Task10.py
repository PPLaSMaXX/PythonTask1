library_user = {
    "ID": 213,
    "Second Name": "Fedorko",
    "First Name": "Max",
    "Group": "ІПЗс21-2",
    "Course": 3,
    "Books": ["Кобзар","451 градус по Фаренгейту"],
    "Books Stats":["Кобзар","Прикладна фізика"],
}

def show_summary():
    print(library_user)

def take_book():
    library_user["Books"].append(input("Enter name of the book: "))
    print("Book successfully taken!")

def return_book():
    book_to_return = input("Enter name of book you wanna to return: ")
    if book_to_return in library_user["Books"]:
        library_user["Books"].remove(book_to_return)
        library_user["Books Stats"].append(book_to_return)
        print("Book found and successfully returned!")
    else:
        print("You have not taken this book")


print("Enter number for corresponding action(1 - View summary, 2 - Take a book, 3 - Return a book )")
show_summary()

while(True):
    user_choice = input("\n")
    match(user_choice):
        case "1":
            show_summary()
        case "2":
            take_book()
        case "3":
            return_book()
        case "0":
            break
        case _:
            print("Invalid input!")









