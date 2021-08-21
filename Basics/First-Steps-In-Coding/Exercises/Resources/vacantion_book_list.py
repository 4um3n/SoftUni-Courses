current_book_pages_count = int(input())
pages_read_for_hour = int(input())
days_for_book = int(input())
time_for_a_book = current_book_pages_count / pages_read_for_hour
hours_per_day = time_for_a_book / days_for_book
print(hours_per_day)
