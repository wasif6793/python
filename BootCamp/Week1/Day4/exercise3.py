marks = {"a":21,"b":32,"c":34,"d":92}
sum = 0
count = 0
for grade in marks:
    sum += marks[grade]
    count += 1

avg = sum / count

print(avg)