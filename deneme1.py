class RomanNumeral:

    def __init__(self, roman):

        self.roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.roman = roman

    def is_valid_roman(self):

        # Ardışık dört aynı karakter kontrolü
        for i in range(len(self.roman) - 3):
            if self.roman[i] == self.roman[i + 1] == self.roman[i + 2] == self.roman[i + 3]:
                return False

        # Geçersiz çıkarma notasyonları kontrolü
        subtractive_notations = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        for notation in subtractive_notations:
            if notation in self.roman:
                index = self.roman.index(notation)
                if (index + len(notation) < len(self.roman) and self.roman_numerals[self.roman[index + len(notation)]] >
                        self.roman_numerals[notation[0]]):
                    return False

        # Geçersiz rakam kombinasyonları kontrolü
        invalid_combinations = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
        for combination in invalid_combinations:
            if combination in self.roman:
                return False

        for i in range(len(self.roman) - 1):
            current_value = self.roman_numerals[self.roman[i]]
            next_value = self.roman_numerals[self.roman[i + 1]]
            if current_value < next_value and (next_value / current_value not in [5, 10, 2, 3]):
                return False

        return True

    def to_arabic(self):

        if not self.is_valid_roman():
            raise ValueError("Geçersiz Roma rakamı")

        result = 0

        for i in range(len(self.roman)):
            current_value = self.roman_numerals[self.roman[i]]
            if i + 1 < len(self.roman) and self.roman_numerals[self.roman[i + 1]] > current_value:
                result -= current_value
            else:
                result += current_value

        return result

# Örnek Kullanım


roman_class = input("Bir Roma rakamı girin: ")
roman_numeral = RomanNumeral(roman_class)

try:
    output_arabic_class = roman_numeral.to_arabic()
    print(f"{roman_class} Roma rakamı olarak: {output_arabic_class}")

except ValueError as e:
    print(e)
