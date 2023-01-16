print("Collections: Activity 1: Write a Python program to sum values of a list.")

n = int (input("How many items will your list have? ")) # I create a variable to get input from user about the number of items
i = 1 # I create a variable to indicate the starting point of the loop
collection = [] # I create a variable to be able to append elements to it
while i<=n: # I set the while loop to finish at the last item
 Input = int(input("Please enter a number: ")) # I create a variable to get a number input from user
 collection.append(Input) # I append this input to the list collection
 i+=1 # This allowes the loop to keep going to the next iteration
collectionList = list (collection) # I transform the collected numbers into a list variable
print("Your list is:", collectionList) # I print the result collection
print ('%s %d' % ("The sum is", sum(collectionList))) # I calculate and print the result

print("Collections: Activity 2: Write a Python program to find the average of a list.")
print ('%s %f' % ("The average is", sum(collectionList)/n)) # I calculate and print the average

print("Collections: Activity 3: Write a Python program to find the maximum and minimum value of a list.")
print('%s %f' % ("The maximum value is", max(collectionList))) # I calculate and print the maximum
print('%s %f' % ("The minimum value is", min(collectionList))) # I calculate and print the minimum







