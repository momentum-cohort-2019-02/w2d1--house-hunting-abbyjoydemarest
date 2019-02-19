portion_down_payment = float(0.25)
current_savings = int(0)
annual_return = float(0.04)
month = 0

print("Yay! You are considering buying a house!"
"Please answer the following questions with whole numbers" 
"or decimals when requested).")
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
annual_return = input('Enter the expected annual rate of return: ')
if annual_return != "":
    annual_return = 0.04
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = (input("Enter the percent of your home's cost to save as a down payment: "))
if portion_down_payment != "":
    portion_down_payment = 0.25
monthly_salary = (annual_salary / 12)
print("monthly-salary" + str(monthly_salary))

monthly_portion_saved = portion_saved * monthly_salary
print( "monthly-portion-saved" + str(monthly_portion_saved))

down_payment = float(total_cost) * float(portion_down_payment)
print( "down-payment" + str(down_payment))


current_savings= 0
current_month = 0
while current_savings < down_payment:
    current_month += 1
    interest = current_savings * float(annual_return) / 12
    current_savings = current_savings + monthly_portion_saved + interest
print("Number of months: " + str(current_month))


