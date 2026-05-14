# Decimal to Roman Converter

A JavaFX application that converts between Roman numerals and decimal numbers by invoking Python scripts that run using functions from the `roman_decimal_functions.py` module.

## Features
- Converts Roman numerals to decimal numbers and decimal numbers to Roman numerals
- Accepts lowercase input for Roman numerals and ignores leading and trailing spaces
- Displays Descriptive error messages in popup windows
- Validates input Roman numeral before conversion
- Combines JavaFX GUI frontend with Python backend scripts

## How it works

### Roman to Decimal
1. User enters a Roman numeral in the Roman numeral field
2. Java GUI invokes `roman_to_decimal_backend.py` and passes it the input
3. The Python script validates the numeral and returns the decimal form if valid
4. Java GUI receives it back and displays it in the decimal number field

### Decimal to Roman
1. User enters a decimal number in the decimal number field
2. Java GUI invokes `decimal_to_roman_backend.py` and passes it the input
3. The Python script converts the decimal number to its canonical Roman numeral equivalent
4. Java GUI receives the result from the script and displays it in the Roman numeral field

## Example

``` text
Roman Numeral: XIV
Decimal Number: 14

Roman Numeral: MMXXVI
Decimal Number: 2026

Decimal Number: 944
Roman Numeral: CMXLIV

Roman Numeral: IVX
Error: Invalid Roman numeral

```

## Notes

The files the application needs in order to run correctly:

- `roman_decimal_functions.py`
- `decimal_to_roman_backend.py`
- `roman_to_decimal_backend.py`
- `RomanToDecimalConverter.java` (needs compilation before execution)

Please make sure all of these files are saved in the same folder when you are downloading them.