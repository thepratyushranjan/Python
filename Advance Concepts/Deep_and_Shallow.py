# Shallow Copy :-
# A shallow copy creates a new object, but it doesn't create copies of the objects that the original object refers to.
# Instead, it merely copies references to those objects.
# This means that any changes to mutable nested objects inside the copied object will reflect in the original object and vice versa.

# Example:-
import copy

# Original list with nested list
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a shallow copy of the original list
shallow_copy_list = copy.copy(original_list)

# Modify an element in the nested list
shallow_copy_list[0][0] = 100

print("Original List:", original_list)  # Output: [[100, 2, 3], [4, 5, 6]]
print("Shallow Copy:", shallow_copy_list)  # Output: [[100, 2, 3], [4, 5, 6]]

# Explanation:
#Changing an element in the nested list of shallow_copy_list affects the original_list because the shallow copy only copies references to the inner lists.
# The lists inside both the original and copied lists are still pointing to the same memory locations.

# Deep Copy
# A deep copy creates a new object and recursively copies all objects found within the original object.
# In this case, even the nested objects (like inner lists or dictionaries) are copied, not just referenced.
# As a result, changes to nested objects in the copied object do not affect the original object.

import copy

# Original list with nested list
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a deep copy of the original list
deep_copy_list = copy.deepcopy(original_list)

# Modify an element in the nested list
deep_copy_list[0][0] = 100

print("Original List:", original_list)  # Output: [[1, 2, 3], [4, 5, 6]]
print("Deep Copy:", deep_copy_list)  # Output: [[100, 2, 3], [4, 5, 6]]

# Here, the deepcopy() function creates a completely new, independent copy of the nested lists. Modifying the deep copy does not affect the original list.

# Example for both:-

import copy

# Original list with nested lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a shallow copy
shallow_copy_list = copy.copy(original_list)

# Create a deep copy
deep_copy_list = copy.deepcopy(original_list)

# Modify the shallow copy
shallow_copy_list[0][0] = 100

# Modify the deep copy
deep_copy_list[1][1] = 200

# Printing results
print("Original List:", original_list)  # Output: [[100, 2, 3], [4, 5, 6]]
print("Shallow Copy:", shallow_copy_list)  # Output: [[100, 2, 3], [4, 5, 6]]
print("Deep Copy:", deep_copy_list)  # Output: [[1, 2, 3], [4, 200, 6]]

# Explanation:

# Shallow Copy: Changing shallow_copy_list[0][0] to 100 affects the original_list because both the original and shallow copy reference the same nested list.
# Deep Copy: Changing deep_copy_list[1][1] to 200 does not affect the original_list because the deep copy created a completely independent copy of the nested lists.

