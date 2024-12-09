# Step 1: Create an empty list
my_list = []

# Step 2: Append the elements 10, 20, 30, 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from the list
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find the index of the value 30 in the list
index_of_30 = my_list.index(30)

# Print the final list and the index of 30
print("Final List:", my_list)
print("Index of 30:", index_of_30)