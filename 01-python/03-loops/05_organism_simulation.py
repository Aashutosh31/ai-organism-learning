age = 0
energy = 100
alive  = True

while alive:


  if 0 <= age <=18:
    age += 1
    energy -= 1
  elif 18 < age <=30:
    age += 1
    energy -= 2
  elif 30 < age <=60:
    age += 1
    energy -= 2
  elif 60 < age <=100:
    age += 1
    energy -= 5
  if energy < 0:
    energy = 0
    alive = False
  
  print("Age: ",age)
  print("Energy: ",energy)
  print("Alive: ",alive)


