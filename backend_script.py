from roman_decimal_functions import decimal_to_roman
import sys

decimal_input = sys.argv[1]

try:
    print(decimal_to_roman(decimal_input))
    sys.exit(0)

except Exception as e:
    print("Invalid input. You should give a decimal number.", file=sys.stderr)
    print(f"Error Message: {repr(e)}", file=sys.stderr)
    sys.exit(1)

    

