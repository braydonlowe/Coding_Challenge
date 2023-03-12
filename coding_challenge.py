import os
#Coding Challenge
#There are four basic rules for creating roman numerals:

"""Now they want to convert all the numbers from the tablets to decimal numbers. To make this conversion easier,
they commissioned you to write a program to convert roman numerals to decimal numbers and decimal
numbers back to roman numerals to check their accuracy."""


"""
1) Normally, values are combined by adding the values of the symbol together.
For example, III = 3, VII = 7, CLXV = 165
2) Roman numerals also involve subractive notation.
If a symbol A is less than the symbol immediately following it (B), A is subracted from B and AB is treated
as a unit to add to the total. Thus IV = 4 XL = 40, XC = 90

3) Subractive notation only ever involves two symbols.
So, for example XIV = 14 not 4. XL = 40. XC = 90

4) A symbol representing 10x may not percede any symbol larger than 10x + 1.
For example, C cannot be preceeded by I or V, only by X (or, of course by a symbol representing a value equal to
or larger than C.)"""

#Roman numerals to numbers:
def numerals_to_numbers(starting_string, final_number = 0):
    """Takes in a starting string that is all Upper case. It then recursively runs through this program to turn
    the numeral into a number.
    >>> numerals_to_numbers("MMMCMXCIX")
    3999"""
    if len(starting_string) == 0:
        return final_number
    if starting_string[0] == "M":
        final_number += 1000
    elif starting_string[0] == "D":
        final_number += 500
    elif starting_string[0] == "C":
        if len(starting_string) >= 2 and starting_string[1] == "M":
            final_number += 900
            return numerals_to_numbers(starting_string[2:], final_number)
        elif len(starting_string) >= 2 and starting_string[1] == "D":
            final_number += 400
            return numerals_to_numbers(starting_string[2:], final_number)
        else:
            final_number += 100
    elif starting_string[0] == "L":
        final_number += 50
    elif starting_string[0] == "X":
        if len(starting_string) >= 2 and starting_string[1] == "C":
            final_number += 90
            return numerals_to_numbers(starting_string[2:], final_number)
        elif len(starting_string) >= 2 and starting_string[1] == "L":
            final_number += 40
            return numerals_to_numbers(starting_string[2:], final_number)
        else:
            final_number += 10
    elif starting_string[0] == "V":
        final_number += 5
    elif starting_string[0] == "I":
        if len(starting_string) >= 2 and starting_string[1] == "X":
            final_number += 9
            return numerals_to_numbers(starting_string[2:], final_number)
        elif len(starting_string) >= 2 and starting_string[1] == "V":
            final_number += 4
            return numerals_to_numbers(starting_string[2:], final_number)
        else:
            final_number += 1
    return numerals_to_numbers(starting_string[1:], final_number)


def subtraction_method(number):
    """Returns the string values needed to be subtracted to get the number.
    And it returns the new number (Should be one digit less)
    >>> subtraction_method(999)
    CM, 99
    >>> subtraction_method(444)
    XL, 44
    """
    #Find the next largest number.
    number = int(number)
    if 500 < number < 1000:
        str_number = "M"
    elif 100 < number < 500:
        str_number = "D"
    elif 50 < number < 100:
        str_number = "C"
    elif 10 < number < 50:
        str_number = "L"
    elif 5 < number < 10:
        str_number = "X"
    elif 1 < number < 5:
        str_number = "V"

    #Find the subtraction number
    if 1 < number < 10:
        subtraction_number = "I"
    elif 10 < number < 100:
        subtraction_number = "X"
    elif 100 < number < 1000:
        subtraction_number = "C"
    number = str(number)
    return subtraction_number + str_number , number[1:]



def addition_method(number, total = 0):
    """Returns the string values needed to get to add to the first digit of the number inputed.
    >>> addition_method(8)
    "VIII"
    >>> addition_method(899)
    DCCC"""
    our_strings = ""
    is_first = True
    our_number = ""
    for numbers in number:
        if is_first == True:
            our_number +=  numbers
            is_first = not is_first
        else:
            our_number += "0"

    int_number = int(our_number)
    while int_number > 0:
        if int_number >= 1000:
            total += 1000
            our_strings += "M"
            int_number -= 1000
        elif int_number >= 500:
            total += 500
            our_strings += "D"
            int_number -= 500
        elif int_number >= 100:
            total += 100
            our_strings += "C"
            int_number -= 100
        elif int_number >= 50:
            total += 50
            our_strings += "L"
            int_number -= 50
        elif int_number >= 10:
            total += 10
            our_strings += "X"
            int_number -= 10
        elif int_number >= 5:
            total += 5
            our_strings += "V"
            int_number -= 5
        else:
            total += 1
            our_strings += "I"
            int_number -= 1
    assert str(total) == our_number
    return our_strings, number[1:]

#Takes one argument. Number
def numbers_to_numerals(number_string):
    """Returns a Roman Numeral that is equivelent with the number that is put in.
    >>> numbers_to_numerals(3999)
    MMMCMXCIX"""
    if len(number_string) == 0:
        return ""
    if number_string[0] == "4" or number_string[0] == "9":
        string_values, new_number = subtraction_method(number_string)
    else:
        string_values, new_number = addition_method(number_string)
    return string_values + numbers_to_numerals(new_number)

def input_validate(input):
    list_of_characters = ["M", "D", "C", "L", "X", "V", "I"]
    dictionary = {"M" : 1000, "D": 500, "C": 100, "L": 50, "X": 10, "I": 1}
    if input[0].isdigit():
        for number in input:
            if not number.isdigit():
                return False, False
            else:
                continue
        return True, "Digit"
    else:
        for character in input:
            if not character.isalpha():
                return False, False
            characters = character.upper()
            if not characters in list_of_characters:
                return False, False
        total = 0
        for i in range(len(input)):
            if i < 2:
                total += dictionary[input[i].upper()]
            elif dictionary[input[i].upper()] > total:
                return False, False
        return True, "Alpha"
            
def system_clear():
    os.system('cls')
    pass


def main():
    #Spaces are entered to make the program look a bit better.
    system_clear()
    print("\n\n\n\n\n\n\n")
    print("                              Welcome to your Roman Numeral Converter!")
    print("\n\n\n\n\n\n\n")
    input("                                Please press enter to continue: ")
    system_clear()

    digit_list = []
    alpha_list = []
    boolean_switch = True
    while boolean_switch == True:
        x = True
        while x == True:
            our_input = input("Please enter desired roman numerals or a number value: ")
            validation_check, digit_or_alpha = input_validate(our_input)
            if validation_check == False:
                print("Please enter in an input as a number (0-9) or as a roman numeral M, D, C, L, X, V, I (upper or lowercase).\nRoman numerals that are inputed must also be in decending order.")
                continue
            else:
                x = not x
        if digit_or_alpha == "Digit":
            alpha_car = (numbers_to_numerals(our_input))
            digit_list.append(our_input)
            alpha_list.append(alpha_car)
            print(alpha_car)
        if digit_or_alpha == "Alpha":
            input_upper = our_input.upper()
            digit_car = (numerals_to_numbers(input_upper))
            alpha_list.append(our_input)
            digit_list.append(digit_car)
            print(digit_car)
        
        boolean_switch3 = True
        while boolean_switch3 == True:
            quit =input("To do another number, press enter, to quit enter Q/q: ")
            if len(quit) == 0:
                boolean_switch3 = not boolean_switch3
                system_clear()
            else:
                q_test = quit.upper()
                if q_test == "Q":
                    boolean_switch = not boolean_switch
                    boolean_switch3 = not boolean_switch3
                else:
                    print("Sorry, the input that was entered was not recognized. Please try again.")
    print("Thank you for using us for your Roman Numeral Converter!\n\n")

    print("Below can be found the numbers that were converted:\n")
    print("     Roman Numeral,   Number")
    for alpha, digit in zip(alpha_list, digit_list):
        #This is going to print out number that were converted with the Roman Numeral Converter. It's going to make it look nice in a table.
        print()
        character_length = len(alpha)
        #I want to print the numbers 20 characters in.
        number_of_spaces = 15 - character_length
        spaces = " " * number_of_spaces
        print("     ", alpha, spaces, digit)

    print("\n\n\n\n")


main()
