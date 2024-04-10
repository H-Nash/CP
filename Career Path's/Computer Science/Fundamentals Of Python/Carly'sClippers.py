# Carly's Clippers Project
# Pregened Code
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Written Code

# Prices and Cuts
total_price = 0

# Calc Average Price
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print(f"Average Haircut Price: ${round(average_price, 2)}")

# Calc new Price
new_prices = [price - 5 for price in prices]
print(new_prices)

# Revenue
total_revenue = 0

# Calc last weeks total revenue
for i in range(len(hairstyles)):
  total_revenue = prices[i] * last_week[i]
print(f"Total Revenue: ${round(total_revenue, 2)}")

# Calc average daily revenue
average_daily_revenue = total_revenue / 7
print(round(average_daily_revenue, 2))

# Cheap haircuts list creation
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
print(cuts_under_30)

