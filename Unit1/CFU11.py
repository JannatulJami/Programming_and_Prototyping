def num_1():
    for num in range(10, 71, 10):
        print(num)

def num_2():
    num = 0
    while num <= 10:
        print(num)
        num += 0.5

def song():
    bottles = 99
    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall.")

def choose_function():
    choice = input("Enter 1 for printing numbers 10 to 70, 2 for numbers 0 to 10, or 3 for the song: ")
    if choice == "1":
        num_1()
    elif choice == "2":
        num_2()
    elif choice == "3":
        song()
    else:
        print("Restart and choose a number from 1-3")


choose_function()
