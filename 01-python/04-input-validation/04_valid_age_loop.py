age = int(input("Enter Your age: "))

if 0 <= age <=120:
  print(age)
else: 
  while age:
   age = int(input("Enter Your Age: "))
   if 0 <= age <=120:
     print(age)
     break;
