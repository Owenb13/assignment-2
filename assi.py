def modulo_calculator():

    x = int(input("please enter a whole number: "))
     #asks the user for an integer input

    y = int(input("please enter a second whole number: "))
     # asks the user for a number to modulus the first

    z = x % y
    # calculates the modulus of the two numbers

    print("the result of the modulus is " + str(z))
    #prints the result and casts the answer back to a string

def integer_division_calc():

    x = int(input("please enter a whole number: "))
    # asks the user to enter an integer and stores it in x

    y = int(input("please enter a whole number to divide by: "))
    # asks for a divisor as an integer and stores it in y

    z = x / y
     #divides x by y and stores the value in z

    z = int(z) 
    # makes sure the result of the division is an integer

    print("the result " + str(x)+ " divided by "+str(y)+" is "+str(z))
    #prints the result of the division

def float_integer_calc():

    x = float(input("please enetr a float value: "))
    # asks the user to enter a float value and stores it in x

    y = float(input("please enter a second float value: "))
    # asks the user for a divisor as a float and stores it in y

    z = x / y
    # divides the two floats and stores it in z

    z = int(z)
    # casts the result of float division to a an integer

    print(" the result of "+str(x)+" divided by "+str(y)+" is "+str(z))
    #prints the out the divisor dividend and the result of the division

def for_loop_counter():

    counter = float(input("what should the initial value of the counter: "))
    # counter asks for a value for to start the for loop

    loop_count = int(input("how many times would you like for the loop to run: "))
    # asks the user how many times the loop should run and stores the integer a loop_count

    increment = float(input(" please enter a value for the counter to increment by: "))
    # asks the user for an increment value and stores it in increment

    is_positive = int(input("should the counter decrement, if so type 1 , if false type 2: "))

    if is_positive == 1:
        for 
    else:
        print("goodbye")










print("choose one of the following options") # create a list of options for the user to choose from
print("0. Modulo claculator")
print("1. integer division calculator")
print("2. float and integer calculator")
print("3. for loop counter")
print("4. integer and float addition")
print("5. print ascii values of letters in a string")
print("6. change machine")
print("7. rock paper scissors")
print("8. mario stairs")
user_input= int(input(" What is your selection: "))    # ask the user what operation they would like to choose

if user_input == 0:
    modulo_calculator()
elif user_input == 1:
    integer_division_calc()
elif user_input == 2:
    float_integer_calc()
elif user_input == 3:
    for_loop_counter()




