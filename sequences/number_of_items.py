#count the number of items in a sequence

#string
name = 'Henry'
print (len(name)) #the output is 5

#list
animals = ['Goat', 'Donkey', 'Sheep', 'Cow']
print(len(animals)) #the output is 4

#tuple
students = ('Anne', 'Justine', 'Yvonne', 'Samwel')
print(len(students)) #the output is 4

#count(item) - returns the count n item
#string
name = 'Henry'
print(name.count('e')) #the output is 1

#list
animals = ['Goat', 'Donkey', 'Sheep', 'Cow']
print(animals.count("Goat")) #the output is 1

#tuple
students = ('Anne', 'Justine', 'Anne', 'Yvonne', 'Samwel')
print(students.count('Anne')) #the output is 2
