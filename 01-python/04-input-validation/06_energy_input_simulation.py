energy = int(input("Enter Starting Energy: "))
age = 0
alive = True

while alive:
  if energy > 0:
    print("organism is alive:",energy) 
    energy_cost=5
    if energy < energy_cost:
      print("Not enough energy")
      break
    else:
      energy -= energy_cost
   
  elif energy == 0:
    print("organism is dead")
    alive = False
  else:
    energy = int(input("Enter Starting Energy: "))




