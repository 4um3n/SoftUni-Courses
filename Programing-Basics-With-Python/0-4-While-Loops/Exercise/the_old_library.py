searched_book = input()
checked_books_count = 0
is_book_found = False
checked_book = input()

while checked_book != "No More Books":
    if checked_book == searched_book:
        is_book_found = True
        break

    checked_books_count += 1
    checked_book = input()

if is_book_found:
    print(f"You checked {checked_books_count} books and found it.")
else:
    print(f"The book you search is not here!\n"
          f"You checked {checked_books_count} books.")
