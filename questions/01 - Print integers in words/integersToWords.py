# Question:
# Given an integer between 1-999, print it in words
# Ex: 419 => Four Hundred Nineteen

# Question 2:
# Widen the range up to 999999
# Ex: 419 502 => Four Hundred Nineteen Thousand Five Hundred Two

def intToWord(num):
    thousands = num // 1000
    num %= 1000

    # Dictionaries
    singles = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["Twenty", "Thirty", "Forty","Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    tenPlus = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    word = ""

    # Digits
    hundredDigit = num // 100
    tenDigit = (num % 100) // 10
    oneDigit = num % 10

    # Wording
    if hundredDigit > 0:
        word += singles[hundredDigit-1] + " Hundred "

    if tenDigit == 1:
        word += tenPlus[oneDigit] + " "
    elif tenDigit > 1:
        word += tens[tenDigit-2] + " "
    
    if oneDigit > 0 and tenDigit != 1:
        word += singles[oneDigit-1]

    if thousands > 0:
        word = intToWord(thousands) + " Thousand " + word

    return word

# Test Cases
print("1: " + intToWord(1))
print("999: " + intToWord(999))
print("402: " + intToWord(402))
print("619: " + intToWord(619))
print("372: " + intToWord(372))
print("810: " + intToWord(810))
print("17: " + intToWord(17))
print("100: " + intToWord(100))

# Test Cases 2
print("1000: " + intToWord(1000))
print("999999: " + intToWord(999999))
print("100000: " + intToWord(100000))
print("123456: " + intToWord(123456))
print("505050: " + intToWord(505050))
