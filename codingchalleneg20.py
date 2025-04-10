#Jannatul Jami
#Period 1 and 2

def avoids(word, forbidden):
    for i in word:
        if i in forbidden:
            return False
    return True
        

letters = input("Write a list of letters: ") 
word_list = ["cookie", "water", "land", "ocean"]
print(avoids(word_list, letters))

count = 0
for i in word_list:
    if avoids(i, letters) == False:
        count += 1
print("There are " + str(count) + " words that passed the filter")    
