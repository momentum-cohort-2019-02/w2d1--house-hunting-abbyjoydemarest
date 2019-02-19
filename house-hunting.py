portion_down_payment = float(0.25)
current_savings = int(0)
r = float(0.04)

annual_salary = True
while annual_salary:
    print('Yay! You are considering buying a house!' +
    'Please answer the following questions with whole numbers' + '(or decimals when requested).')
    annual_salary = int(input('What is your annual salary? '))
    if annual_salary != "":
        monthly_salary = int(annual_salary / 12)
        print(monthly_salary)
        portion_saved = monthly_salary * float(input('What portion of your salary do you want saved? (Provide as a decimal) '))
    if portion_saved != "":
        print('portion-saved' + str(portion_saved))
        annual_portion_saved = int((portion_saved * 12))
        current_savings = int(annual_portion_saved * r)
        print('current-savings' + str(current_savings))
        total_cost = int(input('What is the total cost of your dream home? '))
    if total_cost != "":
        print('total-cost' + str(total_cost))
        down_payment = int(total_cost * portion_down_payment)
    if down_payment > 0:
        print('down-payment' + str(down_payment))
        annual_savings = current_savings + annual_portion_saved
        number_of_years_annual_savings = down_payment / annual_savings
        number_of_months = int(number_of_years_annual_savings) * 12
        print('Number of months: ' + str(number_of_months))

