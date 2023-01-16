print("Control Statements: Activity 1")
n1=input("Number 1: ") # First I create the variables out of the input
n2=input("Number 2: ")
n3=input("Number 3: ")
if n1==n2==n3: # If numbers are equal
    print("All numbers are equal") # Print "all numbers are equal"
elif n1!=n2!=n3: # If numbers are different
    print("All numbers are different") # Print "all numbers are different"
else: # Otherwise
    print("Neither all are equal or different") # Print that they are not equal nor different

print("Control Statements: Activity 2")
n1=input("First number: ") # First I create the variables out of the input
n2=input("Second number: ")
n3=input("Third number: ")
if n1<n2<n3: # If numbers are increasing order
    print("Increasing order") # Print "increasing order"
elif n1<n2<n3: # If numbers are decreasing order 
    print("Decreasing order") # Print "decreasing order"
else: # Otherwise
    print("Neither increasing nor decreasing order") # Print "neither increasing nor decreasing order"
