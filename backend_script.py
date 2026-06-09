from number_conversion_functions import *
import sys

input_form = sys.argv[1].upper()
output_form = sys.argv[2].upper()
number = sys.argv[3]
mode = sys.argv[4] if len(sys.argv) > 4 else "SIGNED"

try:
    match input_form, output_form:
        case "BIN", "DEC":
            if mode == "SIGNED":
                print(binary_to_decimal(number)) 
            else:
                print(binary_to_decimal(number, signed=False))
        case "DEC", "BIN":
            if mode == "SIGNED":
                print(decimal_to_binary(number))
            else:
                print(decimal_to_binary(number, signed=False))
        case "BIN", "HEX":
            print(binary_to_hex(number))
        case "HEX", "BIN":
            print(hex_to_binary(number))
        case "BIN", "RMN":
            print(binary_to_roman(number))
        case "RMN", "BIN":
            print(roman_to_binary(number))
        case "DEC", "HEX": 
            if mode == "SIGNED":
                print(decimal_to_hex(number))
            else:
                print(decimal_to_hex(number, signed=False))
        case "HEX", "DEC":
            if mode == "SIGNED":
                print(hex_to_decimal(number))
            else:
                print(hex_to_decimal(number, signed=False))
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

    

