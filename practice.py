def modulo_calculator():

    user_value = int(input("please enter an integer value"))

    print("you enetered:"+str(user_value))

    #modulo = int(input("please enter a number to modulo this by"))
    modulo = [3,4,5,6,7,8]
    times = int(input("how many times would you like for the modulo to run"))

    for i in range(times):
        result = user_value % modulo[i]


        print("the result of:"+str(user_value)+" moduloed with "+str(modulo[i])+" equals: "+str(result))


modulo_calculator()