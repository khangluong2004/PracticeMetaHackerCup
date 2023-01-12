input_f = open("second_meaning_input.txt", "r")
output_f = open("output.txt", "w")

test_num = int(input_f.readline().strip("\n"))
for test in range(test_num):
    t = int(input_f.readline().strip("\n"))
    c = input_f.readline().strip("\n")
    additional = "."
    if "." in c:
        additional = "-"
    output_f.write("Case #{}:\n".format(test + 1))
    for i in range(1, t):
        output_f.write(c + additional * i + "\n")

input_f.close()
output_f.close()