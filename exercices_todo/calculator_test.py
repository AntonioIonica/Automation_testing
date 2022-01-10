total_bill = 124.56
procent_10 = 0.10
procent_12 = 0.12
procent_15 = 0.15
split_people = 7
tip = total_bill * procent_12 + total_bill
print(tip)
total = tip / float(split_people)
print(round(total, 2))
