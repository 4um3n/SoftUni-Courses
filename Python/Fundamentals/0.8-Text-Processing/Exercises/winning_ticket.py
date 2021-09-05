tickets = input().split(", ")
winning_symbols = ["@", "#", "$", "^"]
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print(f"invalid ticket")
        continue
    
    is_found = False
    left_h, right_h = ticket[:10], ticket[10:]
    for s in winning_symbols:
        if s * 20 in ticket:
            print(f'ticket "{ticket}" - 10{s} Jackpot!')
            is_found = True
            break

        elif s * 6 in left_h and s * 6 in right_h:
            s_length = 0
            if left_h.count(s) < right_h.count(s):
                s_length = left_h.count(s)
            else:
                s_length = right_h.count(s)
            
            print(f'ticket "{ticket}" - {s_length}{s}')
            is_found = True
            break
    
    if not is_found:
        print(f'ticket "{ticket}" - no match')
