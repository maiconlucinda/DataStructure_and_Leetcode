

myList = [1, 2, 3, 4, 5, 6, 10]

# It adds to the end
myList.append(10)

# The number of occurrencies of the value
print(myList.count(10))

# Add to the end
myList.extend([8, 9, 50])

# It returns the index based on the value that we pass
print(myList.index(2))

# Pass the index and the value that you want to add - the index will be the last one of the list, even if you pass 100000.
myList.insert(15, 80)

# Return the index of the value
print(myList.index(80))

# Remove the value that was passed. Only the first presence.
myList.remove(10)

# By the fault, it removes the last item, except if we pass a index.
myList.pop(3)


print(myList)

