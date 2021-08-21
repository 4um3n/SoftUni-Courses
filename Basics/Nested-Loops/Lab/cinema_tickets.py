total_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0

movie = input()
while movie != "Finish":
    free_seats = int(input())
    total_free_seats = free_seats
    current_total_tickets = 0

    while free_seats > 0:
        ticket_type = input()

        if ticket_type == "End":
            break
        elif ticket_type == "student":
            total_student_tickets += 1
        elif ticket_type == "standard":
            total_standard_tickets += 1
        elif ticket_type == "kid":
            total_kid_tickets += 1

        current_total_tickets += 1
        total_tickets += 1
        free_seats -= 1

    current_room_volume = current_total_tickets / total_free_seats * 100

    print(f"{movie} - {current_room_volume:.2f}% full.")

    movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{total_student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{total_standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{total_kid_tickets / total_tickets * 100:.2f}% kids tickets.")
