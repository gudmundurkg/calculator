"""
Notandi slær endurtekið inn reiknisegð
    Reiknisegð = (int) (operator) (int)
þangað til slegið er q
    while x != "q"

Niðurstaða skrifuð út með 2 aukastöfum
Leyfilegir virkjar/operatorar:
    +,-,*,/
Bara int tölur
Ef deiling þá má seinni int ekki vera 0

Skoða villuboð
"""
#Biðja um streng
    #Biðja um int
    #Biðja um reiknisegð
    #Biðja um int

user_str = input("Enter an equation: " )


while user_str != "q":

    #Afmörkum strengja input frá notanda
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
    #Umbreytum str inputti í int
    first_int = int(first_str)
    second_int = int(second_str)

    
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Invalid operator")
    elif operator == "+": #Samlagning
        sum = (first_int + second_int)
        sum_float = "{:.2f}".format(sum)
        print("Result:", sum_float)
    elif operator == "-": #Frádráttur
        subtract = first_int - second_int
        subtract_float = "{:.2f}".format(subtract)
        print("Result", subtract_float)
    elif operator == "*": #Margföldun
        multiply = first_int * second_int
        multiply_float = "{:.2f}".format(multiply)
        print("Result", multiply_float)
    elif operator == "/": #Deiling
        if second_int == 0:
            print("Cant divide by 0")
        else:
            divide = first_int / second_int
            divide_float = "{:.2f}".format(divide)
            print("Result", divide_float)
    user_str = input("Enter an equation: " )


#Villucheck/Villuboða
