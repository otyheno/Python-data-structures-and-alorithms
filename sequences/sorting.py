#sorting returns a new list of items in sorted orer

#string
name = 'Henry'
print (sorted(name)) #the output is ['H', 'e', 'n', 'r', 'y']

#list
animals = ['Goat', 'Donkey', 'Sheep', 'Cow']
print(sorted(animals)) #the output is ['Cow', 'Donkey', 'Goat', 'Sheep']

#tuple
students = ('Anne', 'Justine', 'Yvonne', 'Samwel')
print(sorted(students)) #the output is ['Anne', 'Justine', 'Samwel', 'Yvonne']

#sorting by second letter
#Add parameter and a lambda function to return the second character(the word 
# key is defined parameter name, k is an arbitrary variable name)

#tuple
students = ('Anne', 'Justine', 'Yvonne', 'Samwel')
print(sorted(students, key=lambda k: k[1])) #the output is ['Samwel', 'Anne', 'Justine', 'Yvonne']
