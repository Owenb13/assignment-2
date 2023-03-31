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
 # asks the user if they would like to decrement
    
    if is_positive == 1:  # if statemnt to seperate increment or decrement option
        for i in range(loop_count):
            # for loop that iterates in the range of the loop count

            counter = counter - increment
            # counter gets decremented by the increment value

    else:
        for i in range(loop_count):
            # for loop that iterates in the range of the loop count


            counter = counter + increment
        # counter gets added to the increment value each time 

    print(""+str(counter))
    #prints out the result of the counter at the end



def integer_float_addition():

    x = int(input("please enetr an integer value: "))
    # asks the user for an integer value and stores it in x 

    y = float(input("please enter a float value: "))
    # asks the user for a float and stores iot in y
   
    z = y + float(x)
    # adds the two values togeather and casts the x value to a float
    
    z = str(z)
    # casts the result to a string to be printed

    print(" the result of " +str(x)+ " added to "+str(y)+" is "+z)

def ascii_string_values():
    
    user_str = input("please enter a string to find the ascii values of there letters: ")
    #asks the user to input a string and stores it in user_str

    str_size = len(user_str)
    #finds the lenght of the string inputed
   
    i = 0 
    while(i < str_size):
      #creates a while loop that iterates while i is less than the length of the string

      ascii =   ord(user_str[i])
      # finds the ascii value of the string

      print("the letter imputed "+user_str[i]+" has an ascii value "+ str(ascii) )
        # printds out the letter in the string and corresponding ascii value
      i+=1
    # increases variable i by 1 each time the loop runns

def change_machine():

    coins =[25,10,5]

    coin_counts = []

    x = float(input("please enter a float value: "))
     
    int_x = int(x)

    cents = x * 100 - int_x * 100
    i = 0
    for i in coin_counts:
        coin_counts[i] = cents / coins[i]
        cents = cents % coins[i]

        i+=1

    print("quaters: "+str(coin_counts[0])+" dimes: "+str(coin_counts[1])+" nickles: "+str(coin_counts[2]))









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
elif user_input == 4:
    integer_float_addition()
elif user_input == 5:
    ascii_string_values()
elif user_input == 6:
    change_machine()
elif user_input == 7:
    rpc_game()
elif user_input == 8:
    mario_stairs()






