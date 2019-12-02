counter = 0
print(" A+, A, A-, B+, B, B-, C+,C,C-, D+, D-, F")
number = int(input("Cuantos grados?: "))
totalScore = 0
while counter < number:
  grade = input("Inserta tu grado: ")
  if grade == "A+":
    totalScore += 4.0
  if grade == "A":
    totalScore += 4.0
  if grade == "A-":
    totalScore += 3.7
  if grade == "B+":
    totalScore += 3.3
  if grade == "B":
    totalScore += 3.0
  if grade == "B-":
    totalScore += 2.7
  if grade == "C+":
    totalScore += 2.3
  if grade == "C":
    totalScore += 2.0
  if grade == "C-":
    totalScore += 1.7
  if grade == "D+":
    totalScore += 1.3
  if grade == "D":
    totalScore += 1.0
  if grade == "F":
    totalScore += 0.0
  counter = counter + 1

finalGrade = totalScore/number
print("Tu promedio es:", finalGrade)