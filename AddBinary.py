def addBinary(a, b):
    count_a = len(a) - 1
    count_b = len(b) - 1
    dec_num_a = 0
    dec_num_b = 0
    for num in a:
        dec_num_a += int(num) * pow(2, count_a)
        count_a -= 1
    for num in b:
        dec_num_b += int(num) * pow(2, count_b)
        count_b -= 1
    add_a_b = dec_num_b + dec_num_a
    return bin(add_a_b).replace("0b", "")

a = "110"
b = "101"
print(addBinary(a, b))