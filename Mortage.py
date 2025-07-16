print('Welcome to our Streamlined application process of calculating monthly mortage payments for our clients')

#M = P r(1+r)^n / (I + r)^n - 1

loan = int(input('Enter eligible loan amount ($):'))

rate = float(input('Enter annual rate (%): '))

duration = int(input('Enter convinient payback time (years): '))

monthly_rate = (rate / 100) / 12
 
monthly_duration = duration * 12 

print('Your monthly interest rate is ', monthly_duration)

monthly_payment_value = loan * (monthly_rate*(1 + monthly_rate)*monthly_duration) / ((1 + monthly_rate)*monthly_duration - 1)

print('Your monthly_payment_value is ', monthly_payment_value, 'Enjoy your time here! ')