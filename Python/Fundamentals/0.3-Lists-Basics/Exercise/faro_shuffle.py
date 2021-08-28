cards = input().split()
shuffle_count = int(input())
working_cards_list = cards.copy()
after_shuffle_list = working_cards_list
len_card_list = len(working_cards_list)


for shuffle in range(shuffle_count):
    left_list = [working_cards_list[left_index]
                    for left_index in range(1, len_card_list - 1) 
                    if left_index < len_card_list / 2]
    
    right_list = [working_cards_list[right_index] 
                    for right_index in range(1, len_card_list - 1) 
                    if right_index >= len_card_list / 2]

    right_index = 0
    left_index = 0

    for index in range(1, len_card_list - 1):

        if index % 2 == 1:
            after_shuffle_list[index] = right_list[right_index]
            right_index += 1
        else:
            after_shuffle_list[index] = left_list[left_index]
            left_index += 1

    working_cards_list = after_shuffle_list

print(after_shuffle_list)
