

#A list is a collection of items or elements, usually ordered and mutable, in programming.
# It allows you to store multiple values in a single variable.
# Lists can contain any type of data, such as numbers, strings, or other objects,
# and they can be modified after creation by adding, removing, or changing elements.



# len() list
my_list = [1, 2, 3, 4, 5]

# Get the length of the list
length = len(my_list)

# Display the result
print(f"The length of the list is: {length}")


# count() list
my_list = [1, 2, 3, 4, 3, 1, 4, 1, 5]

# Count the occurrences of the number 1 in the list
count_ones = my_list.count(1)

# Display the result
print(f"The number '1' appears {count_ones} times in the list.")


# index() list
my_list = [10, 20, 30, 40, 50]

# Find the index of the element 30
index_of_element = my_list.index(30)

# Display the result
print(f"The index of 30 is: {index_of_element}")


# sorted() list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Get a sorted version of the list
sorted_list = sorted(my_list)

# Display the results
print("Original List:", my_list)  # The original list remains unchanged
print("Sorted List:", sorted_list)  # The new sorted list


# sort() list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sort the list in place
my_list.sort()

# Display the result
print("Sorted List:", my_list)


# del() list
my_list = [10, 20, 30, 40, 50]

# Delete the element at index 
del my_list[2]

print(my_list) 


# remove() list
my_list = [10, 20, 30, 40, 50, 20]

# Remove the first occurrence
my_list.remove(20)

print(my_list)  


# pop() list
my_list = [10, 20, 30, 40, 50]

# Pop the element at index 
popped_element = my_list.pop(2)

print("Popped Element:", popped_element)  
print("Updated List:", my_list)       


# append() list
my_list = [10, 20, 30]

# Add an element to the end of the list
my_list.append(40)

print(my_list) 


# insert() list
my_list = [10, 20, 30]

# Insert 15 at index 1
my_list.insert(1, 15)

print(my_list)  


# + operator
my_list = [1, 2, 3]

# Single element to append
element = 4

# Using the + operator to append the element
my_list = my_list + [element]

print(my_list) 


# extend() list
my_list = [1, 2, 3]

# Extend the list by adding elements from another list
my_list.extend([4, 5, 6])

print(my_list)  


# min() list
numbers = [10, 20, 5, 30]

# Find the minimum value in the list
minimum_value = min(numbers)

print(minimum_value)  


# max() list
numbers = [10, 20, 5, 30]

# Find the maximum value in the list
maximum_value = max(numbers)

print(maximum_value)  


# reverse() list
my_list = [1, 2, 3, 4, 5]

# Reverse the list
my_list.reverse()

print(my_list)  
