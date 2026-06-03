import math

def number_str_converter(number):
    if isinstance(number, int):
        return {'ones': number % 10, 'tens': number % 100 - number % 10, 'hundreds': number % 1000 - (number % 100), 'thousands': number // 1000}
    elif isinstance(number, str):
        number = int(number)
        return number_str_converter(number)
    else:
        return NotImplemented
    
def isbin(txt):
    if not isinstance(txt, str):
        return False
    if any(i != "0" and i != "1" for i in txt):
        return False
    return True

hex_num_list = ["A", "B", "C", "D", "E", "F"]

def isHex(txt):
    if not isinstance(txt, str):
        return False
    
    new_txt = txt.upper()

    if any(not i.isdecimal() and i not in hex_num_list for i in new_txt):
        return False
    
    return True

def check(format, number):
    if not isinstance(number, str):
        raise TypeError("Invalid input type.")
    if format == "Bin":
        if not isbin(number):
            raise ValueError("Input should be a binary number.")
    elif format == "Dec":
        if not number.isdecimal():
            if not number[0] == "-" or not number[1::].isdecimal():
                raise ValueError("Input should consist only of digits.")
    elif format == "Hex":
        if not isHex(number):
            raise ValueError("Input should be a valid hexadecimal number.")

def bin_flipper(number):
    new_number = number
    digits_list = [char for char in new_number]
    
    rightmost_one = None
    for i in range(len(digits_list) - 1, -1, -1):
        if digits_list[i] == "1":
            rightmost_one = i
            break
    
    if rightmost_one is None:
        return -1
    else:
        for i in range(rightmost_one - 1, -1, -1):
            if digits_list[i] == "1":
                digits_list[i] = "0"
            elif digits_list[i] == "0":
                digits_list[i] = "1"
                
    new_number = "".join(digits_list)

    return new_number

def space_remover(number):
    number_list = number.split(" ")
    joint_number = "".join(number_list)
    return joint_number
    
    
def decimal_to_roman(number):
    ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    tens = {0: '', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'}
    hundreds = {0: '', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM'}

    string = ''
    number_dict = number_str_converter(number)
    string += number_dict['thousands'] * 'M'
    string += hundreds[number_dict['hundreds']]
    string += tens[number_dict['tens']]
    string += ones[number_dict['ones']]
    return string

def roman_to_decimal(number):
    check("Roman", number)
    
    values = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    hierarchy = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
    value_list_1 = []
    if any(i not in values for i in number):
        raise ValueError('Invalid number format')
    original_number = number
    while number:
        if len(number) >= 2:
            if hierarchy[number[0]] < hierarchy[number[1]]:
                value_list_1.append(f'{number[0]}{number[1]}')
                number = number[2:]
            else:
                value_list_1.append(number[0])
                number = number[1:]
                
        else:
            value_list_1.append(number[0])
            number = number[1:]
    
    value_list_2 = [values[i] for i in value_list_1]

    decimal_form = sum(value_list_2)
    canonical_roman_form = decimal_to_roman(decimal_form)
    if original_number.upper() != canonical_roman_form:
        raise ValueError('Invalid number format')

    return decimal_form


def binary_to_decimal(number):
    modified_number = space_remover(number)
    check("Bin", modified_number)
    
    if modified_number[0] == "1":
        new_number = bin_flipper(modified_number)
        return "-" + binary_to_decimal(new_number)

    decimal_number = 0
    current_power = 0

    for i in range(len(modified_number) - 1, -1, -1):
        decimal_number += int(modified_number[i]) * math.exp2(current_power)
        current_power += 1
    
    return str(int(decimal_number))

def decimal_to_binary(number):
    new_number = space_remover(number)
    check("Dec", new_number)
    
    int_number = int(new_number)
    if int_number < 0:
        positive_binary = decimal_to_binary(str(abs(int_number)))
        return bin_flipper(positive_binary)

    if int_number == 0:
        return "0"

    binary_number = ""

    while(int_number != 0):
        binary_number = str(int(int_number % 2)) + binary_number
        int_number //= 2

    if binary_number[0] == "1":
        binary_number = "0" + binary_number

    return binary_number


def binary_to_hex(number):
    new_number = space_remover(number)
    check("Bin", new_number)

    hex_number = ""
    number_copy = new_number
    hex_list = []

    while len(number_copy) > 3:
        hex_list.append(number_copy[-1:-5:-1][::-1])
        number_copy = number_copy[:-4:]

    if len(number_copy) != 0:
        leading_zeros_count = 4 - len(number_copy)
        last_digit = leading_zeros_count * "0" + number_copy
        hex_list.append(last_digit)

    hex_list.reverse()

    for bits in hex_list:
        decimal_bits = int(binary_to_decimal(bits))
        if decimal_bits < 10:
            hex_number += str(decimal_bits)
        else:
            hex_number += hex_num_list[10 - decimal_bits]

    return hex_number

def hex_to_binary(number):
    new_number = space_remover(number)
    check("Hex", new_number)

    binary_number = ""

    for char in number:
        if char.isdecimal():
            result = decimal_to_binary(char)[1::]
            binary_number += (4 - len(result)) * "0" + result
        elif char.isalpha():
            result = 10 + hex_num_list.index(char.upper)
            result = decimal_to_binary(str(result))[1::]
            binary_number += result
    
    return binary_number


def decimal_to_hex(number):
    binary_number = decimal_to_binary(number)
    hex_number = binary_to_hex(binary_number)
    return hex_number

def hex_to_decimal(number):
    binary_number = hex_to_binary(number)
    decimal_number = binary_to_decimal(binary_number)
    return decimal_number


def roman_to_binary(number):
    decimal_number = roman_to_decimal(number)
    binary_number = decimal_to_binary(decimal_number)
    return binary_number

def binary_to_roman(number):
    decimal_number = binary_to_decimal(number)
    roman_number = decimal_to_roman(decimal_number)
    return roman_number


def roman_to_hex(number):
    decimal_number = roman_to_decimal(number)
    hex_number = decimal_to_hex(decimal_number)
    return hex_number

def hex_to_roman(number):
    decimal_number = hex_to_decimal(number)
    roman_number = decimal_to_roman(decimal_number)
    return roman_number