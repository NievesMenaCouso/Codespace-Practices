print("Loops: Activity 1: Write a Python program to get the Fibonacci series between 0 to 50")
a = 0 # Set the first two values of the series as variables
b = 1
while b<50: # Set a loop to stop when b>=50
  print(b) # For each iteration print the value of b (the Fibonacci number)
  a, b = b, a+b # After each iteration, change the value of a to the value of b, and the value of b to the value of b plus a. This way we advance in the series.
  
print("Loops: Activity 2: Write a Python program to create the multiplication table (from 1 to 10) of a number")
a=int(input("Choose a number to calculate its multiplication table: ")) # Create a variable to call the input
b=1 # Set b as a new variable representing the numbers of iterations, and a starting point for the loop (where your multiplication table will start)
while b<=10: # Start the while loop, setting its ending after the 10nth iteration
    c=b*a # Create a new variable to do your calculations, in this case multiplicate the input by the number of iteration
    print(c) # Print the result of the previous calculation
    b+=1 # Add 1 to b (number of iteration) for the next iteration
    
