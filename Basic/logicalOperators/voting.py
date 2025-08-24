def is_eligible(votes,age):
    return votes >= 1000 and age >= 18

print(is_eligible(10000,21))
print(is_eligible(200,32))