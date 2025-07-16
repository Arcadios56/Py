price_per_litre = 855
budget = float(input('Enter your total budget in Naira: '))
litres = budget / price_per_litre

print('With a budget of', budget, 'Naira, you can purchase', round(litres, 2), 'litres of gas.')