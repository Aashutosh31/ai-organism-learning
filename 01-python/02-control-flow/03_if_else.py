energy = 12
temperature = 45
has_energy = False
is_tired = True


if energy >=40 and temperature <=60:
   print("Organism is healthy")
elif energy <= 10 or temperature >=80:
   print("Organism is critical")
elif 10 < energy < 40 or 60 < temperature < 80:
   print("Tired:",is_tired)
   print("Energy:",has_energy)
else:
   print("Organism is Sleeping")