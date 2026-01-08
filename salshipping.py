weight = 8.4
gnd_per_lb = 0
flat = 20

#ground shipping
if weight < 2:
  gnd_per_lb = weight * 1.5
elif weight <= 6:
  gnd_per_lb = weight * 3
elif weight <= 10:
  gnd_per_lb = weight * 4
elif weight > 10:
  gnd_per_lb = weight * 4.75
else:
  print("error calculating shipping, check inputs")

total_gnd_cost = gnd_per_lb + flat

gnd_ship_output = ("$" + str(total_gnd_cost))
print(gnd_ship_output)

#cost premium as gnd plus premium surcharge 

premium_gnd_cost = total_gnd_cost + 125

print("$" + str(premium_gnd_cost))

#drone shipping 

weight = 1.5
drone_per_lb = 0 


if weight < 2:
  drone_per_lb = weight * 4.5
elif weight <= 6:
  drone_per_lb = weight * 9
elif weight <= 10:
  drone_per_lb = weight * 12
elif weight > 10:
  drone_per_lb = weight * 14.25
else:
  print("error calculating shipping, check inputs")

total_drone_cost = drone_per_lb 

drone_ship_output = ("$" + str(total_drone_cost))
print(drone_ship_output)


