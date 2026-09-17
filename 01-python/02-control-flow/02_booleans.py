has_Energy = True
is_Tired = False

if has_Energy and not is_Tired:
  print("Organism Energized")
elif is_Tired and not has_Energy:
  print("Organism Tired")
elif has_Energy and is_Tired or not has_Energy and not is_Tired:
  print("Error Organism Can not exist in same state in both conditions simultaneously")