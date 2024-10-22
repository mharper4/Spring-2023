''' Name: Morgan Harper

Program is about ....
'''

# Half adder circuit
def halfAdder(a, b):
    sum = a ^ b
    carry = a & b
    return sum, carry

# Full adder circuit
def fullAdder(a, b, c):
    sum1, carry1 = halfAdder(a, b)
    sum2, carry2 = halfAdder(sum1, c)
    carry = carry1 | carry2
    return sum2, carry


# 4-bit adder circuit
def fourBitAdder(a0, a1, a2, a3, b0, b1, b2, b3):
    # First Full Adder
    s0, c0 = fullAdder(a0, b0, 0)

    # Second Full Adder
    s1, c1 = fullAdder(a1, b1, c0)

    # Third Full Adder
    s2, c2 = fullAdder(a2, b2, c1)

    # Fourth Full Adder
    s3, c3 = fullAdder(a3, b3, c2)

    # Output sum and overflow bit
    s = str(s3) + str(s2) + str(s1) + str(s0)
    o = c3

    return s, o


# Function to convert binary string to decimal
def binaryToDecimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2**(len(binary)-1-i)
    return decimal

# Function to convert decimal to hex
def decimalToHex(decimal):
    hexa = hex(decimal).replace("0x", "").upper()
    if len(hexa) == 1:
        hexa = "0" + hexa
    return hexa

# Function to add two 4-bit binary strings and return the binary sum and overflow bit
def hexAdder(a, b):
    # Split 4-bit inputs into single bits
    a0, a1, a2, a3 = [int(x) for x in a]
    b0, b1, b2, b3 = [int(x) for x in b]

    # Calculate binary sum and overflow bit using the 4-bit adder circuit
    s, o = fourBitAdder(a0, a1, a2, a3, b0, b1, b2, b3)

    # Convert binary sum to hex digit
    decimal = binaryToDecimal(s)
    hexa = decimalToHex(decimal)

    return o, s, hexa

def main():
    # Test cases
    inputs = ["0000", "0001", "0010", "0100", "1000"]
    for a in inputs:
        for b in inputs:
            o, s, hexa = hexAdder(a, b)
            print("a:", a, "b:", b, "sum:", s, "hex:", hexa)
if __name__ == '__main__':



    main()


