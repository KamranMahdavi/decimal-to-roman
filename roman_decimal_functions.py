def number_str_converter(number):
    if isinstance(number, int):
        return {'ones': number % 10, 'tens': number % 100 - number % 10, 'hundreds': number % 1000 - (number % 100), 'thousands': number // 1000}
    elif isinstance(number, str):
        number = int(number)
        return number_str_converter(number)
    else:
        return NotImplemented
    
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
    if type(number) != str:
        return NotImplemented
    
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

