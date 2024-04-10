#Sal's Shipping Project
#var declaration
weight = 41.5
ground_cost = None
drone_cost = None
premium_ground_cost = None

#Premium Ground Shipping
premium_ground_cost = round(125, 2)
print(f"Premium Ground Shipping: ${premium_ground_cost}")

#Ground shipping logic
if weight <= 2:
  ground_cost = (weight * 1.50) + 20
elif weight > 2 and weight < 6:
  ground_cost = (weight * 3.00) + 20
elif weight > 6 and weight < 10:
  ground_cost = (weight * 4.00) + 20
else:
  ground_cost = (weight * 4.75) + 20

ground_cost = round(ground_cost, 2)
print(f"Ground Shipping: ${ground_cost}")

#Drone Shipping Logic
if weight <= 2:
  drone_cost = (weight * 4.50)
elif weight > 2 and weight < 6:
  drone_cost = (weight * 9.00)
elif weight > 6 and weight < 10:
  drone_cost = (weight * 12.00)
else:
  drone_cost = (weight * 14.25)
drone_cost = round(drone_cost, 2)
print(f"Drone Shipping: ${drone_cost}")

#Price Check Logic
if ground_cost < drone_cost and ground_cost < premium_ground_cost:
  print(f"Ground Shipping is the cheapest at: ${ground_cost}")
elif drone_cost < ground_cost and drone_cost < premium_ground_cost:
  print(f"Drone Shipping is the cheapest at: ${drone_cost}")
else:
  print(f"Premium Ground Shipping is the cheapest at: ${premium_ground_cost}")
