# open file in read mode
file = open("players.txt","r")
# readline
readline = file.readline()
# read
read = file.read()
# test
# print("readline {0}".format(readline))
# print("read {}".format(read))

""" conclusion: readline will only read one line, read will read the entire file"""

# formatting with read
array = []
array = read.split()
print(array)


# formatting with readline
rl_array = []
for line in file:
    print(file.readline())
    rl_array.extend(file.readline())
print(rl_array)





