# list
my_list = [23,43,45,56,67] #list of integers
print(my_list)
my_list2 = ['John', 'Doe', 'Jane', 'Doe'] # list of strings
print(my_list2)
my_list.append(78) # append method
print(my_list)
my_list2.append('Jack') # append method
print(my_list2)
complete_list = [my_list, my_list2] # list of lists
print(complete_list)
print(complete_list[0]) # list indexing
print(my_list[2]) # list indexing
print(my_list2[3]) # list indexing

#dictionary # dictionary
my_dict = {'name':'obbse', 'country':'Ethiopia', 'age':23}
print(my_dict)
print(my_dict['name']) # dictionary indexing with key
print(my_dict['country']) # dictionary indexing with key
print(my_dict['age']) # dictionary indexing with key
my_dict['age'] = 24
my_dict['occupation'] = 'Software Engineer' # add new key value pair
print(my_dict)

# WORKING WITH LIST AND DICTIONARY
my_dict = {'name':'obbse', 'country':'Ethiopia', 'age':23}
my_list = [23,43,45,56,67] #list of integers
dict_list = [my_dict, my_list] # list of lists
print(dict_list)
print(dict_list[0]) # list indexing
print(dict_list[1]) # list indexing
print(dict_list[0]['name']) # dictionary indexing with key
print(dict_list[0]['country']) # dictionary indexing with key   
print(dict_list[0]['age']) # dictionary indexing with key
print(dict_list[1][2]) # list indexing
print(dict_list[1][3]) # list indexing

# TUPLE
my_tuple = (23,43,45,56,67) #tuple of integers
print(my_tuple)
my_tuple2 = ('John', 'Doe', 'Jane', 'Doe') # tuple of strings

print(my_tuple2)
my_tuple.append(78) # append method
print(my_tuple)
my_tuple2.append('Jack') # append method
print(my_tuple2)

complete_tuple = (my_tuple, my_tuple2) # tuple of tuples

print(complete_tuple)
print(complete_tuple[0]) # list indexing
print(complete_tuple[1]) # list indexing
print(complete_tuple[0][2]) # list indexing
print(complete_tuple[1][3]) # list indexing

# SET

my_set = {23,43,45,56,67} #set of integers
print(my_set)
my_set2 = {'John', 'Doe', 'Jane', 'Doe'} # set of strings
print(my_set2)
my_set.add(78) # add method

print(my_set)
my_set2.add('Jack') # add method
print(my_set2)
complete_set = {my_set, my_set2} # set of sets
print(complete_set)

print(complete_set[0]) # list indexing

print(complete_set[1]) # list indexing

print(complete_set[0][2]) # list indexing

print(complete_set[1][3]) # list indexing   

print(complete_set[0].add(78)) # add method

print(complete_set[0]) # list indexing

print(complete_set[1]) # list indexing

print(complete_set[0].add(78)) # add method

print(complete_set[0]) # list indexing

print(complete_set[1]) # list indexing
