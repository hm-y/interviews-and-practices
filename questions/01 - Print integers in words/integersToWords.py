# Question 1:
# Given an integer between 1-999, print it in words
# Ex: 419 => Four Hundred Nineteen

def intToWord(num):
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

# Question 2:
# Widen the range up to 999999
# Ex: 419 502 => Four Hundred Nineteen Thousand Five Hundred Two

def intToWordUpToMillion(num):
    word = ""

    thousands = num // 1000
    if thousands > 0:
        word += intToWord(thousands) + " Thousand "

    word += intToWord(num%1000)
    return word


# Test Cases
print("1000: " + intToWordUpToMillion(1000))
print("999999: " + intToWordUpToMillion(999999))
print("100000: " + intToWordUpToMillion(100000))
print("123456: " + intToWordUpToMillion(123456))
print("505050: " + intToWordUpToMillion(505050))
