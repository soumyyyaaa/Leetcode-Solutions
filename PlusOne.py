def plusOne(digits):
    # length_list = len(digits)
    # number = 0

    # for i in range(0, length_list):
    #     number += digits[i] * pow(10, length_list-i-1)

    # final_number = number + 1
    
    # return list(map(int, str(final_number)))
    digits = int("".join(map(str, digits)))
    digits += 1
    return list(map(int, str(digits)))

digits = [1, 2, 3]
print(plusOne(digits))