"""
Höfundur: Guðmundur Kristján

Forrit sem tekur inn tvær heiltölur og einn virkja.
Reiknar út skv inntaki.
"""
user_str = input("Enter an equation: " )

while user_str != "q":

    #Afmörkum inntak frá notanda
    user_str_split = user_str.split(' ')
    first_str = user_str_split[0]
    second_str = user_str_split[2]
    operator = user_str_split[1]

    #Skoðum hvort inntak sé bókstafur
    numeric_check_first = first_str.isnumeric()
    numeric_check_second = second_str.isnumeric()
    
    if numeric_check_first == False or numeric_check_second == False:
        print("Invalid operands")
        user_str = input("Enter an equation: " )
        continue

    first_int = int(first_str)
    second_int = int(second_str)

    #Reiknivél
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Invalid operator")
    elif operator == "+": #Samlagning
        sum = (first_int + second_int)
        sum_final = "{:.2f}".format(sum)
        print("Result:", sum_final)
    elif operator == "-": #Frádráttur
        subtract = first_int - second_int
        subtract_final = "{:.2f}".format(subtract)
        print("Result:", subtract_final)
    elif operator == "*": #Margföldun
        multiply = first_int * second_int
        multiply_final = "{:.2f}".format(multiply)
        print("Result:", multiply_final)
    elif operator == "/": #Deiling
        if second_int == 0:
            print("Can't divide by 0")
        else:
            divide = first_int / second_int
            divide_final = "{:.2f}".format(divide)
            print("Result:", divide_final)

    user_str = input("Enter an equation: " )

