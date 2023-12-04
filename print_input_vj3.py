# microwave_power = 1.3
# daily_usage_of_microwave = 2
# day_in_month = 30
# electicity_cost = 0.2
# monthly_usage = microwave_power *   daily_usage_of_microwave *  day_in_month
# monthly_price_of_electricity = monthly_usage * electicity_cost

# print('Mjesecna potrosnja iznosi:', monthly_usage, 'of kWh what costs', monthly_price_of_electricity)


microwave_power = float(input('Unesite snagu mikrovalne pečnice:'))
daily_usage_of_microwave = float(input('Unesite vrijeme dnevnog korištenja mikrovalne u satima: '))
day_in_month = int(input('Unesite broj dana u mjesecu:'))
electicity_cost = float(input('Unesite cijenu kWh struje:'))
monthly_usage = microwave_power * daily_usage_of_microwave * day_in_month
monthly_cost = monthly_usage * electicity_cost
print('Mjesecno koristenje mikrovalne:', monthly_usage, 'sto kosta:',monthly_cost,'.')
