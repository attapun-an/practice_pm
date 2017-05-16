
def encryption(string):
    en_string = ""
    for i in string:
        new_num = ord(i) + 3
        en_string += chr(new_num)
    return en_string


def encryption_alt(string_2):
    en_string = ""
    for i in range(0, len(string_2)):
        new_num = ord(string_2[i])+3
        en_string += chr(new_num)
    return en_string


def input_message():
    print("input your message")
    inp_mess = input()
    return inp_mess


def append_to_file(str_to_file):
    file = open("messages.txt", "a")
    file.write(str_to_file)
    file.close()


UserInput = input_message()
print(UserInput)
# first encryption method
encrypted = encryption(UserInput)
# second encryption method
encrypted2 = encryption_alt(UserInput)
print(encrypted)
print(encrypted2)

append_to_file(encrypted)


