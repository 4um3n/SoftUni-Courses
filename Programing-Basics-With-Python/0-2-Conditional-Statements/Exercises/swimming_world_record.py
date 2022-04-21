world_record_seconds = float(input())
length_meters = float(input())
seconds_for_meter = float(input())

time_without_resistance = length_meters * seconds_for_meter
delay = round(length_meters / 15)
time_with_resistance = time_without_resistance + (delay * 12.5)

if time_with_resistance < world_record_seconds:
    print(f"Yes, he succeeded! The new world record is {time_with_resistance:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_with_resistance - world_record_seconds:.2f} seconds slower.")

