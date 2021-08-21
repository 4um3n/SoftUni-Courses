deposited_sum = float(input())
deposit_term = int(input())
interest_rate = float(input())
interest = deposited_sum * (interest_rate * 0.01)
month_interest = interest / 12
end_sum = deposited_sum + (deposit_term * month_interest)
print(end_sum)
