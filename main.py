








def multiplication():
    x = int(input("give me a number to multiply:"))
    y = int(input("what do you want it to be multiplied by?"))

    z = x * y

    print("the result is "+ str(z))



def division():
    x = input("please enter a dividend ")
    y = input("what do you want it divided by?")

    z = float(x) / float(y)

    print ("the result is "+ str(z))


def wide_boy_string():
   
    user_str = input("give me a string to w i d e n \n")

    for char in  user_str:
        print(char, end=" ") # end= is used because python always wants to create a new line



def wide_boy_string2():
   
    user_str = input("give me a string to w i d e n \n")

    i = 0

    wide_str = ""
    
    for char in  user_str:


        
        

        if i < len(user_str) - 1:
            wide_str = wide_str + char + " "
        else:
            wide_str = wide_str + char 
        i+=1


    print(wide_str)






def for_loop():
    
    x = int(input("how many times should I run"))

    for i in range(x):
        print("this loop is runningfor the " + str(i + 1) + " time.")




def odd_or_even():

    x = int(input("which number do you wnat me to check"))

    if x % 2 == 0:
        print("the number " + str(x) + " is even " )
    else:
         print("the number " + str(x) + " is odd " )


    


def asci_sum():
    user_str = input("give me a string for which you want the sum os ascii values of its chars\n")

    str_size = len(user_str)

    i = 0

    sum = 0 

    while( i < str_size):

        sum = sum + ord(user_str[i]) # ord is the extension of ascii

        i = i + 1
    print("the sem of all the ascii values is", sum)




def str_flipper():
    user_str = input("give me a string you want flipped\n")

    for char in reversed(user_str):
        print(char, end="")




    

print("0. multiplication")
print("1. division")
print("2.wide boy string")
print("3.wide boy string 2" )
print("4. for loop")
print("5. odd or even ")
print("6.ascii sum")
print("7. string flipper")

user_input = int(input("which function would you like to run?"))

if user_input == 0:
    multiplication()
elif user_input == 1:
    division()
elif user_input == 2:
    wide_boy_string()
elif user_input == 3:
    wide_boy_string2()
elif user_input == 4:
    for_loop()
elif user_input == 5:
    odd_or_even()
elif user_input == 6:
    asci_sum()
elif user_input == 7:
    str_flipper()

    









