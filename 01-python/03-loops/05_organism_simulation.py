age = 0
energy = 100
alive  = True

print("Age: ",age)
print("Energy: ",energy)
print("Alive: ",alive)  


while alive:
  energy_cost = 0
  
  if 0 <= age <=18:
    energy_cost = 1
  elif 18 < age <=30:
    energy_cost = 2
  elif 30 < age <=60:
    energy_cost = 3
  elif 60 < age <=100:
    energy_cost = 5

  if energy < energy_cost:
    alive = False
  else:
    energy-=energy_cost
    age+=1

  if energy == 0:
    alive = False


  
  print("Age: ",age)
  print("Energy: ",energy)
  print("Alive: ",alive)


