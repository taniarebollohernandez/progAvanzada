number = int(input("Cuanta gente?: "))
cost = 0
counter = 0

while counter < number:
  age = int(input("Cual es la edad?: "))
  if age <=12 and age >=3:
    cost = cost + 14
  if age >= 65:
    cost = cost + 18
  if age >= 13 and age <= 64:
    cost = cost + 23
  counter = counter + 1
  
  
print("El total es: $", cost)
