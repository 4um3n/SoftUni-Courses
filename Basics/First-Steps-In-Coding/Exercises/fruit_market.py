strawberries_price = float(input())
bananas_kilos = float(input())
oranges_kilos = float(input())
raspberries_kilos = float(input())
strawberries_kilos = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.40)
bananas_price = raspberries_price - (raspberries_price * 0.80)

total_strawberries_price = strawberries_kilos * strawberries_price
total_bananas_price = bananas_kilos * bananas_price
total_oranges_price = oranges_kilos * oranges_price
total_raspberries_price = raspberries_kilos * raspberries_price

total_price = total_oranges_price + total_bananas_price + total_raspberries_price +total_strawberries_price

print(total_price)
