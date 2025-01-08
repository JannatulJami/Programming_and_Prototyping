#Jannatul Jami, 
#Period 1 and 2 
#01/07/2025

#Version 1 

prices_1 = [1.95, 4.50, 0.99, 5.99]
sum = 0

for i in prices_1:
    sum += i 
    print("The total sum of the prices is " + str(sum))
    
#Version 2 

def version2():
    prices = []
    question1 = int(input("How many prices do you want to ask: "))
    
    for i in range(question1):
        input_question = float(input("Write down one of the price"))
        prices.append(input_question)
    sum1 = 0
    
    for price in prices:
        sum1 += price
    print("The total amount is " + str(sum1))
                                 
version2()        
    
#Version 3 

def version3():
    prices = []
    items = []
    question1 = int(input("How many prices do you want to ask: "))
    
    for i in range(question1):
        input_question = float(input("Write down one of the price"))
        prices.append(input_question)
        input_question1 = input("Write down one item you want: ")
        items.append(input_question1)
    sum1 = 0
    print("This is your Reciept")
    for i in range(len(prices)):
        print("This " + items[i] + " is $" + str(prices[i]) + " dollars ")
      
    for price in prices:
        sum1 += price
    print("The total amount is " + str(sum1))
version3()
