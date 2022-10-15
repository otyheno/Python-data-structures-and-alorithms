
#access any item in the sequence using its index. Indexing starts at 0

#string
name = 'Henry'
print (name[3]) #the output is r

#list
animals = ['Goat', 'Donkey', 'Sheep', 'Cow']
print(animals[1]) #the output is donkey

#tuple
students = ('Anne', 'Justine', 'Yvonne', 'Samwel')
print(students[0]) #the output is Anne



#index(item) - returns the index of the first occurence of an item
#string
name = 'Henry'
print (name.index('e')) #the output is r

#list
animals = ['Goat', 'Donkey', 'Goat', 'Sheep', 'Cow']
print(animals.index("Goat")) #the output is donkey

#tuple
students = ('Anne', 'Justine', 'Yvonne', 'Samwel')
print(students.index('Justine')) #the output is Anne