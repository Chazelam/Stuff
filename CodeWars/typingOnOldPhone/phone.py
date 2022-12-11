# https://www.codewars.com/kata/635b8fa500fba2bef9189473/python

def splitWord(string):
    string = list(string)
    if string[0] == '1':
        while len(string) > 1 and string[0] == '1':
            string = string[1:]
    if string[0] == '1':
        return ''
    newString = [string[0]]
    for i in range(1,len(string)):
        if (string[i] != string[i-1]):
            if string[i] != '1':
                newString.append(';')
                newString.append(string[i])
        else:
            if string[i] != '1':
                newString.append(string[i])
    return ''.join(newString).split(';')
            
def phone_words(word):
    if word == '':
        return ''
    dict = {'0':' ',    '2':'abc', '3':'def',
            '4':'ghi',  '5':'jkl', '6':'mno',
            '7':'pqrs', '8':'tuv', '9':'wxyz'}
    str = splitWord(word)
    ans = ''
    for line in str:
        if len(line) > len(dict[line[0]]):
            while(len(line) > len(dict[line[0]])):
                ans += dict[line[0]][len(line[:len(dict[line[0]])]) - 1]
                line = line[len(dict[line[0]]):]
            ans += dict[line[0]][len(line) - 1]    
        else:
            ans += dict[line[0]][len(line) - 1]
    return ans