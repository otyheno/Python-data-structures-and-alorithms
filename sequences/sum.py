#finding the sum of items in a sequence. entire sequence must be numeric

#string generates an error
# x = [4, 5, 'Bug']
# print(sum(x)) #Error

#list
j = [8,7, 4, 1, 5]
print(sum(j)) #output 25
print(sum(j[-2:])) #output 6

#tuple
i = (3,8)
print(sum(i)) #output is 11