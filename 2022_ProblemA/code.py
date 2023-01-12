input_f = open("second_hands_input.txt", "r")
output_f = open("output.txt", "w")

test_num = int(input_f.readline())
for test in range(test_num):
    n, k = (input_f.readline().strip("\n")).split(" ")
    types = (input_f.readline().strip("\n")).split(" ")
    if int(n) > 2 * int(k):
        output_f.write("Case #{}: NO".format(test + 1))
    else:
        types_count = {}
        success = True
        for i in types:
            if i in types_count:
                types_count[i] += 1
                if types_count[i] >= 3:
                    output_f.write("Case #{}: NO".format(test + 1))
                    success = False
                    break
            else:
                types_count[i] = 1
        if success == True:
            output_f.write("Case #{}: YES".format(test + 1))
    if test < test_num -1:
        output_f.write("\n")

input_f.close()
output_f.close()
