#codecademy python 3 len pizza slice activity

# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
print(toppings, prices)
num_two_dollars_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell", str(num_pizzas), "different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineabpple"], [1, "cheese"], [3, "sausage"], 
[2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

cheapest_pizza = sorted(pizza_and_prices)

priciest_pizza = cheapest_pizza[-1]

print(priciest_pizza)
cheapest_pizza.pop()

cheapest_pizza.append([2.5, "peppers"])

print(sorted(cheapest_pizza))

three_cheapest = cheapest_pizza[0:3]

print(three_cheapest)
