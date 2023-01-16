print("Functions: Activity 1: Write 2 Python functions to show the list content and to find the max value in the list.")

def MyCollection(): # I create the function to show the list content out of a users input
    n = int (input("How many items will your list have? ")) # I create a variable to get input from user about the number of items
    i = 1 # I create a variable to indicate the starting point of the loop
    collection = [] # I create a variable to be able to append elements to it
    while i<=n: # I set the while loop to finish at the last item
        Input = int(input("Please enter a number: ")) # I create a variable to get a number input from user
        collection.append(Input) # I append this input to the list collection
        i+=1 # This allowes the loop to keep going to the next iteration
    collectionList = list (collection) # I transform the collected numbers into a list variable
    print("Your list is:", collectionList) # I print the result collection
MyCollection() # I call the function

def MaxCollection(): # I create the function to check for the maximum value of an user input list
    n = int (input("How many items will your list have? ")) # I create a variable to get input from user about the number of items
    i = 1 # I create a variable to indicate the starting point of the loop
    collection = [] # I create a variable to be able to append elements to it
    while i<=n: # I set the while loop to finish at the last item
        Input = int(input("Please enter a number: ")) # I create a variable to get a number input from user
        collection.append(Input) # I append this input to the list collection
        i+=1 # This allowes the loop to keep going to the next iteration
    collectionList = list (collection) # I transform the collected numbers into a list variable
    print('%s %f' % ("The maximum value is", max(collectionList))) # I check and print the maximum out of inputs
MaxCollection()

def MyCollection(array): # I create the function to display any array
    print("Your list is:", array)
def MaxCollection(array): # I create the function to check for the maximum value of any array
    print('%s %f' % ("The maximum value is", max(array))) 

a = [2, 4, 55] # A test array
MyCollection(a) # I call the function for the test array
MaxCollection(a) # I call the function for the test array

print("Functions: Activity 2: Create a function to calculate the factorial of a number. The function accepts the number as an argument.")

def Factorial(n):
    return 1 if (n==1 or n==0) else n * Factorial(n - 1) # I calculate the factorial
print("Factorial of",5,"is",Factorial(5))

print("Functions: Activity 3: Write a Python function that takes a number as a parameter and check the number is prime or not.")

n = int(input("Type a number to check whether it is prime or composite: "))
def Prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                print(n, "is a composite number")
                break
        else:
            print(n, "is a prime number")
    else:
        print(n, " is a composite number")
Prime(n)
