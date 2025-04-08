#Jannatul Jami
#Period 1 and 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        remainder = a % b 
        return gcd(b, remainder)
        
print(gcd(48, 18))
print(gcd(56, 98))
print(gcd(101, 10))
print(gcd(42, 56))
print(gcd(17, 13))
