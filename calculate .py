
#!The first example
first = float(input("insert first number:: "))
secc =  float(input("insert second number:: "))
opreation = input("please choise opreation : + , - , * , / , % ")
if opreation == "+":
  result = first + secc
elif opreation == "*":
  result = first * secc
elif opreation == "/":
    result = first / secc
elif opreation == "-":
    result = first - secc
elif opreation == "%":
    result = first % secc

print(result)

#!The second example 

first = input("insert first number:: ")
secc =  input("insert second number:: ")
opreation = input("please choise opreation : + , - , * , / , % ")
if opreation == "+":
  result = float(first) + float(secc)
elif opreation == "*":
  result = float(first) * float(secc)
elif opreation == "/":
    result = float(first) / float(secc)
elif opreation == "-":
    result = float(first) - float(secc)
elif opreation == "%":
    result = float(first) % float(secc)

print(result)

#! Notice that specifying the type to be given in the input or inside the condition depends on the programmer's preference and use