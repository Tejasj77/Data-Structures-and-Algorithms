#Converting Integer to any Base like Decimal, Binary, HexaDecimal

def conversion(number,base):
    convert_string = "0123456789ABCDEF"     #A string for converting the decimal into the hexadecimal
    if(number<base):                        #This implies that number%base == number bcoz number < base
        print(type(convert_string[number]))
        return convert_string[number]
    else:
        list_op = convert_string[number%base]       #Assign the hexadecimal value to the remainder
        #Here, addition of strings take place i.e. a merger
        return conversion(number//base,base) + list_op  #Divide the number and now use the quotient to recursively do the same

print(conversion(769,16))
