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
    t = int(input_f.readline().strip("\n"))
    c = input_f.readline().strip("\n")
    arr = [".", "-"]
    combination(arr, 1, 10, c)
    output_f.write("Case #{}:\n".format(test + 1))
    for i in range(t - 1):
        if len(c) >= 10:
            if c[:10] != arr[i]:
                output_f.write(arr[i] + "\n")
        else:
            if arr[i][(-1* len(c)):] != c: 
                output_f.write(arr[i] + "\n")

input_f.close()
output_f.close()

