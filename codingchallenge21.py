#Jannatul Jami
#Period 1 and 2

def uses_only(word, letters):
    for i in letters:
        if i in word:
            return True
    return False

allowed_letters = ["a", "c", "b", "e", "r","o"]
print(uses_only("Cat", allowed_letters))
print(uses_only("Violet", allowed_letters))
