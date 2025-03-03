#Jannatul Jami
#3/3/225
sentence = input("Input your string: ")
def print_twice(string):
    print(string)
    print(string)
    
def do_twice(spam):
    print(spam)
    print(spam)
def do_four(spam):
    do_twice(spam)
    do_twice(spam)
    
do_four(print_twice(sentence))
