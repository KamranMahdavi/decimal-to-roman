from roman_decimal_functions import roman_to_decimal
import sys

roman_input = sys.argv[1]

try:
    print(roman_to_decimal(roman_input))
    sys.exit(0)

except Exception as e:
    print("You should give a valid Roman numeral.", file=sys.stderr)
    sys.exit(1)