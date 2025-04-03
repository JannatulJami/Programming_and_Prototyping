#Jannatul Jami
#Period 1 and 2

def first_chrcater(string):
    letter = string[0]
    return letter

def last_character(string):
    last_letter = string[-1]
    return last_letter
def middle_part(string):
    return string[1:-1]
    
def palindrome(string):
    if len(string) <= 1:
        return True
    if (string[0] == string[-1]):
        return palindrome(middle_part(string))
    else:
        return False
    
print(palindrome("noon"))
print(palindrome("redivider"))
print(palindrome("hello"))
print(palindrome("a"))
print(palindrome(""))
