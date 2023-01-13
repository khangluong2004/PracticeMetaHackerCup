import math

def combination(arr, count, max_count, banned_code):
    if count >= max_count:
        return
    else:
        new_arr = []
        for i in range(len(arr)):
            if arr[i] + "." != banned_code:
                new_arr.append(arr[i] + ".")
            if arr[i] + "-" != banned_code:
                new_arr.append(arr[i] + "-")
        arr[:] = new_arr
        combination(arr, count + 1, max_count, banned_code)
        

#-----------------Main-------------------------
input_f = open("second_second_meaning_input.txt", "r")
output_f = open("output.txt", "w")

test_num = int(input_f.readline().strip("\n"))
for test in range(test_num):
    n = int(input_f.readline().strip("\n"))
    c = input_f.readline().strip("\n")
    # Solutions accepted by online mechanism (Change first char of given word to ensure C1 is not a "prefix" of any generated encoding)
    # if c[0] == ".":
    #     arr = ["-"]
    # else:
    #     arr = ["."]
    arr = [".", "-"]
    length = min(10, math.ceil(math.log(n, 2)) + 1)
    combination(arr, 1, length, c)
    output_f.write("Case #{}:\n".format(test + 1))
    for i in range(n - 1):
        if len(c) >= length:
            if c[:length] != arr[i]:
                output_f.write(arr[i] + "\n")
        else:
            output_f.write(arr[i] + "\n")

input_f.close()
output_f.close()

