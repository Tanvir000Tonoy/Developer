FirstNumber = 0
SecondNumber  = 1
print(FirstNumber)
print(SecondNumber)
for i in range(18):
    newNumber = FirstNumber + SecondNumber
    print(newNumber)
    FirstNumber = SecondNumber
    SecondNumber = newNumber

