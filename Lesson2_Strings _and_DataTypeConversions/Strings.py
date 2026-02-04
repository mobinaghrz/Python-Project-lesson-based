name = "mobina"
#┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐
#│ m ││ o ││ b ││ i ││ n ││ a │
#└───┘└───┘└───┘└───┘└───┘└───┘
#  0    1    2    3    4    5
print("Length of the STR name is:",len(name)) #Length of the string "name" = 6
# The numbers under the squares (indexes) are counting the indexes which starts from 0
#Note: last index = len(string)-1

#Definition: Anything between '' or "" are considered chars and will be considered an string.
print(type(name)) #The type will be str <class 'str'>
Symbol = "!@ #$%" # Symboles

StringNumber = "23" # String of numbers
#┌───┐┌───┐
#│ 2 ││ 3 │   This is the char of the number 2 next to the chr of number 3 (the are not numbers)
#└───┘└───┘   The computer will see them the same way it sees any other alphabet or symbols (as chars)
#  0    1  
StrNumb = "34" # String of numbers
#┌───┐┌───┐
#│ 3 ││ 4 │ 
#└───┘└───┘   
#  0    1 
print(StringNumber + StrNumb)
#┌───┐┌───┐┌───┐┌───┐
#│ 2 ││ 3 ││ 3 ││ 4 │  The "+" operator will put the characters next to eachother
#└───┘└───┘└───┘└───┘
#  0    1    2    3

#------------------Operation on String-----------------------
# Multiplication: if You want to print a string a certain amount of time:
print("Hello World "*4)
StrVar = "Hiii :D"
print(3*StrVar)