from number_conversion_functions import *
import sys

form_codes = {"Binary": "BIN", "Decimal": "DEC", "Hexadecimal": "HEX", "Roman": "RMN"}

input_form = form_codes[sys.argv[1]]
output_form = form_codes[sys.argv[2]]
number = sys.argv[3]
# True means signed
mode = True if sys.argv[4] == "true" else False

try:
    match input_form, output_form:
        case "BIN", "DEC":
            print(binary_to_decimal(number, mode)) 
        case "DEC", "BIN":
            print(decimal_to_binary(number, mode))
        case "BIN", "HEX":
            print(binary_to_hex(number))
        case "HEX", "BIN":
            print(hex_to_binary(number))
        case "BIN", "RMN":
            print(binary_to_roman(number))
        case "RMN", "BIN":
            print(roman_to_binary(number))
        case "DEC", "HEX": 
            print(decimal_to_hex(number, mode))
        case "HEX", "DEC":
            print(hex_to_decimal(number, mode))
        case "DEC", "RMN":
            print(decimal_to_roman(number))
        case "RMN", "DEC":
            print(roman_to_decimal(number))
        case "HEX", "RMN":
            print(hex_to_roman(number))
        case "RMN", "HEX":
            print(roman_to_hex(number))

    sys.exit(0)

except Exception as e:
    print(f"Error Message: {str(e)}", file=sys.stderr)
    sys.exit(1)

    

