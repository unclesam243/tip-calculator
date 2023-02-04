#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill= int(input("Your bill is: $ "))
n_people = int(input("the number of people to split with is "))
tip = int(input("Tip is 10, 12, 15%, what would you like to give: "))
percentage_tip= tip/100
total_tip= (bill * percentage_tip)
total_bill= bill + total_tip
total_to_pay= total_bill/n_people
pay_to_round= round(total_to_pay, 2)
pay= "{:.2f}".format(pay_to_round)
           
print(f' everyone will have to pay: ${pay}')