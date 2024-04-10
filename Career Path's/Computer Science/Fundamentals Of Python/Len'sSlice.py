#Len's Slice Project
#Var declaration
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olivers", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#count $2 pizzas
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#check mount of pizzas
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

#create 2d list of pizzas and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
#cheapest
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]

#Most $$ pizza
priciest_pizza = pizza_and_prices[-1]

#Remove Anchovies from Menu
pizza_and_prices.pop(-1)
print(pizza_and_prices)

#New pizza peppers
pizza_and_prices.append([2.5, "peppers"])

#three cheapest pizzas 
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
