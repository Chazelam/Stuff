string = '1124335454'
if string[0] == '1':
    while len(string) > 1 and string[0] == '1':
        string = string[1:]
print(string)