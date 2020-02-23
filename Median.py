# Obtains the median of three integers that the user inputs
def median():
    Num_one = input ("Enter your first integer: ")
    Num_two = input ("Enter your second integer: ")
    Num_three = input("Enter the third integer: ")
    if (int (Num_one) < int (Num_two) and int (Num_one) > int (Num_three)):
        print ("The Median of the numbers is: " +Num_one)
    elif (int (Num_one) > int (Num_two) and int (Num_one) < int(Num_three)):
        print("The Median of the numbers is: " + Num_one)
    elif (int (Num_two) < int (Num_one) and int (Num_two) > int (Num_three)):
        print ("The Median of the numbers is: " +Num_two)
    elif (int (Num_two) > int (Num_one) and int (Num_two) < int (Num_three)):
        print("The Median of the numbers is: " + Num_two)
    elif (int (Num_three) < int (Num_two) and int(Num_three) > int(Num_one)):
        print("The Median of the numbers is: " + Num_three)
    elif (int (Num_three) > int (Num_two) and int (Num_three) < int (Num_one)):
        print("The Median of the numbers is: " + Num_three)
    else:
            print("Invalid")
# Using an array and sort function the program automatically spits out the median of the numbers 
num = [0, 17, 3]
num[0] = input("Enter the first number: ")
num[1] = input("Enter the second number: ")
num[2] = input("Enter the third number: ")
print(num)
num.sort()
print(num)
print("The Median of the numbers is: " +num [1])

median()
