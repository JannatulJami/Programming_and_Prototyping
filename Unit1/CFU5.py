#Jannatul Jami period 1 and 2 9/30/2024


#little Canadian kid broke their piggy bank
#you are to create a program to help the,
#figure out how much money they have
#pennies = $0.01
#nickles = $0.05
# dimes = $0.10
#auqrters = $0.25
#loonies = $1 or 100 cents
#ask kid how many coins he has of each
#calculaule the total and give answer in
#decimals and in combonination 
#13.67 or $13 and 2 quarters, 1 dime, 1 nickle, 2 cents

quarters = int(input("How many quarters do you have: "))
dimes = int(input("How many dime do you have: "))
nickles = int(input("How many nickles do you have: "))
pennies = int(input("How many pennies do you have: "))
loonies = int(input("How many loonies do you have: "))
toonies = int(input("How many toonies do you have: "))

coins = (quarters * 0.25) + (nickles * 0.05) + (pennies * 0.01)+ (dimes * 0.10)
dollars = (loonies * 1) + (toonies * 2)
money = dollars + coins

print("He has $" + str(money))
