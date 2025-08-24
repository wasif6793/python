from numpy.ma.core import true_divide

is_loggedin = False

if not is_loggedin:
    print("Please login to continue")


#demo 2

age = 17
has_id = True
with_adult = True

if(age >= 18 and has_id) or (age < 18 and with_adult):
    print("Allowed")
else:
    print("Not allowed")
