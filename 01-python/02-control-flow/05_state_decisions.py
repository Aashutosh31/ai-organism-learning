age = 10
time = "adulthood"
alive = True
energy = 100
is_appropriate = True

if 0 < age <= 12:
     energy = 100
     alive = True
     time = "Childhood"
elif 12 < age < 18:
     energy = 100
     alive = True
     time = "Teenage"
elif 18 <= age <= 24:
     energy = 90
     alive = True
     time = "Adulthood"
elif 24 < age <= 40:
     energy = 70
     alive = True
     time = "Working-age"
elif 40 < age < 60:
    energy = 50
    alive = True
    time = "Middle-age"
elif 60 <= age <= 100:
    energy = 10
    alive = True
    time = "Old-age"
else:
    print("Please Enter Appropriate Age")
    is_appropriate = False
    
if is_appropriate:
  print("Age: ",age)
  print("Time: ",time)
  print("Energy: ",energy)
  print("Alive: ",alive)


