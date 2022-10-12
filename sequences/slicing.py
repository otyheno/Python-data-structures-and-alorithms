#slice() [start:end+1:step] 
# default step=1 
# start is inclusive->end is not inclusive
# #Computational way to acess part of your data

shape = "Parallelogram"

print (shape[1:4]) #the output is ara (index 1 to 3)

print (shape[1:6:2]) #the output is aal since step option is 2

print (shape[3:]) # End not decleared. The output is allelogram. starts from index 3 to the end of string

print (shape[:5]) #start not decleared. The output is Paral. from index 0 to 4

print (shape[-1]) #last item of the element

print (shape[-3:]) #prints the last 3

print (shape[:-2]) #prints all the characters exept the last 2