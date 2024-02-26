class RomanNumeral:

    def __init__(self, roman):
        self.roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.roman = roman.upper()

    def is_valid_roman(self):
        valid_characters = set('IVXLCDM')
        if not all(char in valid_characters for char in self.roman):
            return False

        invalid_combinations = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
        for combination in invalid_combinations:
            if combination in self.roman:
                return False

        for i in range(len(self.roman) - 1):
            current_value = self.roman_numerals[self.roman[i]]
            next_value = self.roman_numerals[self.roman[i + 1]]
            if current_value < next_value and (next_value / current_value not in [5, 10]):
                return False

        return True

    def to_arabic(self):
        if not self.is_valid_roman():
            raise ValueError("Invalid Roman numeral")

        result = 0
        for i in range(len(self.roman)):
            current_value = self.roman_numerals[self.roman[i]]
            if i + 1 < len(self.roman) and self.roman_numerals[self.roman[i + 1]] > current_value:
                result -= current_value
            else:
                result += current_value

        return result

# Example Usage
roman_class = input("Enter a Roman numeral: ")
roman_numeral = RomanNumeral(roman_class)

try:
    output_arabic_class = roman_numeral.to_arabic()
    print(f"{roman_class} as a Roman numeral: {output_arabic_class}")
except ValueError as e:
    print(e)
