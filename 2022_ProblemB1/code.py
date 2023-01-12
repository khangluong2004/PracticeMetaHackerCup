def is_valid(maps, coord):
    friend = 0
    if coord[0] != 0 and maps[coord[1]][coord[0] - 1] == "^":
        friend += 1
    if coord[0] != len(maps[0]) - 1 and maps[coord[1]][coord[0] + 1] == "^":
        friend += 1
    if coord[1] != 0 and maps[coord[1] - 1][coord[0]] == "^":
        friend += 1
    if coord[1] != len(maps) - 1 and maps[coord[1] + 1][coord[0]] == "^":
        friend += 1  
    if friend >= 2:
        return(True)
    return(False)

def remove(maps, fixed_trees, coord):
    x, y = coord
    if maps[y][x] == "^" and not ((x, y) in fixed_trees):
        if is_valid(maps, coord):
            return(False)
        else:
            maps[y] = maps[y][:x] + "." + maps[y][min(x+1, len(maps[y])):]
            if x > 0:
                remove(maps, fixed_trees, (x-1, y))
            if x < len(maps[0]) - 1:
                remove(maps, fixed_trees, (x+1, y))
            if y < len(maps) - 1:
                remove(maps, fixed_trees, (x, y+1))
            if y > 0:
                remove(maps, fixed_trees, (x, y-1))
    else:
        return(False)
        

def find_path(maps, fixed_trees):
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "^" and not ((x, y) in fixed_trees):
                remove(maps, fixed_trees, (x, y))
    
    

#----------------Main-----------------
input_f = open("input.txt", "r")
output_f = open("output.txt", "w")

test_num = int(input_f.readline())
for test in range(test_num):
    r, c = list(map(int, input_f.readline().strip("\n").split(" ")))
    maps = []
    fixed_trees = []
    for i in range(r):
        row = input_f.readline().strip("\n")
        for x in range(len(row)):
            if row[x] == "^":
                fixed_trees.append((x, i))
        maps.append(row)
    if len(fixed_trees) == 0:
        output_f.write("Case #{}: Possible\n".format(test + 1))
        output_f.write("\n".join(maps) + "\n")
    elif r == 1 or c == 1:
            output_f.write("Case #{}: Impossible\n".format(test + 1))         
    else:
        new_map = maps.copy()
        for i in range(len(new_map)):
            new_map[i] = new_map[i].replace(".", "^")
        find_path(new_map, fixed_trees)
        if new_map == maps:
            output_f.write("Case #{}: Impossible\n".format(test + 1))
        else:
            output_f.write("Case #{}: Possible\n".format(test + 1))
            output_f.write("\n".join(new_map) + "\n")
input_f.close()
output_f.close()