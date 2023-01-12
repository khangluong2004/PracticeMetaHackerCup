input_f = open("second_friend_input.txt", "r")
output_f = open("output.txt", "w")

def print_fill(output_f, symbol):
    result = (symbol * c + "\n") * r
    output_f.write("Case #{}: Possible\n".format(test + 1))
    output_f.write(result)

test_num = int(input_f.readline())
for test in range(test_num):
    r, c = list(map(int, input_f.readline().strip("\n").split()))
    empty = True
    for i in range(r):
        row = input_f.readline().strip("\n")
        if "^" in row:
            empty = False 
    if r == 1 or c == 1:
        if empty == False:
            output_f.write("Case #{}: Impossible\n".format(test + 1))
        else:
            print_fill(output_f, ".")
    else:
        print_fill(output_f, "^")
    
input_f.close()
output_f.close()