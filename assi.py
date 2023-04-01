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
 # has the coin denominations as an array stored in coins
    coin_counts = [0,0,0]
    #creating an empty variable for coincounts 

    x = float(input("please enter a float value: "))
    # asking the user to enter a float value and store it in x 
     
    int_x = int(x) 
    #create a variable that is the integer of x
    money = 0
     # create a empty variable  
    cents = x * 100 - int_x * 100 
    #subtract the float of x multipled by 100 by the int of x multiplied by 100 to find the cents remainder
    i = 0
    for money in coin_counts: # create a for loop that iterates through the different coin denominations 
        money = cents / coins[i] # divide cents by coins[i] to find how many of each coin 
        cents = cents % coins[i] # find the remainder of the cents % coins to find the new remainder

        coin_counts[i] = int(money) # cast the result of the division to an int and store it in coincounts [i]
        
        

        i+=1
        #increase the array size by 1 each time 
    print("quaters: "+str(coin_counts[0])+" dimes: "+str(coin_counts[1])+" nickles: "+str(coin_counts[2]))
    # prints out the amount of change from the float inputed

def rpc_game():
    choice = int(input(" please enter 1 for rock, 2 for paper, and 3 for scissors: "))
    # asks the user to choose rock papar or scissors 

    if choice == 1:  # create if else statemnts to show the user what they chose
        print("you chose rock")
    elif choice == 2:
        print("you chose paper")
    elif choice == 3:
        print("you chose scissors")

    import random
    
    ai_choice = random.randint(0,30) # random number generator from 0-30

# determines wether the ai choice is rock paper or scissors 
    if ai_choice <= 9:
        rand_num = 1
        print (" The AI chose rock")
        
    elif 10<= ai_choice <= 19:
        rand_num = 2
        print("the AI chose paper")
    elif 20<= ai_choice <= 30:
        rand_num = 3
        print("the AI chose scissors")
    
 # creates game logic to determine if you win lose or tie  
    if choice == 1:
        if choice - rand_num == 0:
            print("you tied")

        elif choice - rand_num == -1:
            print("loser")
        elif choice - rand_num == -2:
            print("winner")

    elif choice == 2:
        if choice - rand_num == 0:
            print("you tied")

        elif choice - rand_num == -1:
            print("loser")
        elif choice - rand_num == 1:
            print("winner")
        
    elif choice == 3:
        if choice - rand_num == 0:
            print("you tied")

        elif choice - rand_num == 1:
            print("winner")
        elif choice - rand_num == 2:
            print("Loser")


def mario_stairs():
    level  = int(input("enter a value for the height of the level: "))
    # asked the user for the amount of levels they would like to create and stores that in level count 
    
    space = level # makes a variable called space and makes it equal to level
    counter = 0 # creates a counter variable and set it to zero
    for i in range(counter,level,1):
        # create a for loop that starts at the counter until it reaches the level and increases by 1 each time
        print(end=" " *(space - 1))
        # multiplies the number of spaces by the space variable -1 
        space = space - 1
        # decrements the space variable by 1 each time 
        print(end="#"*(counter + 1))
        # prints out the number of # in each level by multipling hastags by 1+ counter
        counter = counter + 1
        # increases the counter by 1 each time the loop runs 
        if space == level-1:
            print("   <")
            # prints out a flag if it is the first iteration of the loop
        else:
            print("   |")
            # prints ot the pole for every level except for the first
    

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

if user_input == 0:  # create multiple if else statements to call the function from the choice selected
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






