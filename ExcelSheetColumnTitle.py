def convert_to_column_name(columnNumber):
    alphabets = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    column_name = ""
    while columnNumber != 0:
        quotient = int(columnNumber / 26)
        remainder = columnNumber % 26
        print(quotient, remainder)
        column_name += alphabets[remainder]
        columnNumber = quotient
    column_name = column_name[::-1]
    return column_name  

columnNumber = 701
print(convert_to_column_name(columnNumber))