#Jannatul Jami
#period 1 and 2

def is_power(a, b):
    if a < b:
        print("False")
    elif a == b:
        print("True")
    elif a % b == 0:
        print("True")
    else:
        print("False")
    
    
is_power(16, 2)
is_power(27, 3)
is_power(9, 2)
is_power(81, 3)
is_power(32, 5)
