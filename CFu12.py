#Jannaul Jami 10/29/2024 Period 1 and 2

ask_password = input("Type the password in: ")
guesses = 0
while ask_password != "simonnyc" and guesses < 3:
    print("Wrong Password")
    guesses += 1
    ask_password = input("Type the password in: ")
if guesses == 3:
    print("No more guesses")
if ask_password == "simonnyc":
    print("Correct you may enter....")
