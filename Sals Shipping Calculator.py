weight = input("Weight of Package(Lbs):")

weight = float(weight)

# Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4.00 + 20
else:
    cost_ground = weight * 4.75 + 20
print("Ground Shipping:" , "$",cost_ground)

#Premium ground shipping

Premium_ground = 125.00
print("Premium_ground:" , "$", Premium_ground)

#Drone Shipping

if weight <= 2:
    drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
   drone_cost = weight * 9.00
elif weight > 6 and weight <= 10:
    drone_cost = weight * 12.00
else:
   drone_cost = weight * 14.25
print("drone_cost:" , "$",drone_cost)



