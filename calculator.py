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

user_str = input("Enter an equation:" )

user_str_split = user_str.split(' ')
first_str = user_str_split[0]
second_str = user_str_split[2]
operator = user_str_split[1]

#Umbreytum strengja inputti í int
first_float = float(first_str)
second_float = float(second_str)



while user_str != "q":
    if operator != "+" or operator != "-" or operator != "*" or operator != "/":
        print("Invalid operator")
    elif operator == "+":
        sum = first_float + second_float
        print(sum)
    elif operator == "-":
        subtract = first_float - second_float
        print(subtract)
    elif operator == "*":
        multiply = first_float * second_float
        print(multiply)
    elif operator == "/":
        if second_float == 0:
            print("Cant divide by 0")
        else:
            divide = first_float / second_float
    else:
        print("Invalid operator")




#print (user_str_split)

#Framkvæma reikniaðgerðir

#Villucheck/Villuboða
