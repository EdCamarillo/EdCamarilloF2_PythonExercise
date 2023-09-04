
def decToBinary(dec):
    binary = ""
    if dec == 0:
        return '0'
    while dec > 0:
        binary = str(dec % 2) + binary
        dec = dec // 2

    return binary

def binaryToN(bin_str, type):
    if type == 'decimal':
        decimal = 0
        for digit in bin_str:
            decimal = decimal * 2 + int(digit)
        return str(decimal)

def decToOctal(dec):
    octal = ""
    if dec == 0:
        return '0'

    while dec > 0:
        octal = str(dec % 8) + octal
        dec = dec // 8

    return octal

def decToHex(dec):
    hexa = ""
    if dec == 0:
        return '0'

    while dec > 0:
        rem = dec % 16
        if rem < 10:
            hexa = str(rem) + hexa
        dec = dec // 10

    return hexa

def main():
    dec_num = int(input("Enter a decimal number: "))
    binary = decToBinary(dec_num)
    octal = decToOctal(dec_num)
    hexadecimal = decToHex(dec_num)

    print("Decimal: ", dec_num)
    print("Binary: ", binary)
    print("Octal: ", octal)
    print("Hexadecimal: ", hexadecimal)

main()
