def calPoints(operations):
    # i = 0
    # while i < len(str_arr):
    #     if str_arr[i] == "C":
    #         output_arr.pop()
    #         str_arr.remove(str_arr[i])
    #         str_arr.remove(str_arr[i-1])
    #         i -= 1
    #     elif str_arr[i] == "+":
    #         sum_ele = output_arr[i-1] + output_arr[i-2]
    #         output_arr.append(sum_ele)
    #         i += 1
    #     elif str_arr[i] == "D":
    #         double = 2 * output_arr[i-1]
    #         output_arr.append(double)
    #         i += 1
    #     else:
    #         output_arr.append(int(str_arr[i]))
    #         i += 1
    output_arr = []
    for element in operations:
        if element == 'D':
            double = output_arr[-1] * 2
            output_arr.append(double)
        elif element == 'C':
            output_arr.pop()
        elif element == '+':
            first_num = output_arr.pop()
            second_num = output_arr.pop()
            sum_of_nums = first_num + second_num
            output_arr.append(second_num)
            output_arr.append(first_num)
            output_arr.append(sum_of_nums)
        else:
            output_arr.append(int(element))
    return sum(output_arr)

operations = ['3', '5', '+', '2', 'C', '5', 'D', '1']
print(calPoints(operations))