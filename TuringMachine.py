def turingMachine(word, program):
    #states = [0,1,2,3,4,5,6,7,8,9,10]
    #alphabet = [0,1]
    state = 1
    position = len(word)-1
    #position = 0

    while state != 0:
        action = program[(state,int(word[position]))]
        state = action[0]
        word = word[:position] + str(action[1]) + word[position+1:]
        position += action[2]
        if position < 0:
            word = "0" + word
            position += 1
        if position >= len(word):
            word = word + "0"
            position -= 1    
    print("output: ", word)

L = -1
C = 0
R = 1

program = {(1,1):(2,1,R),
           (2,0):(3,0,R),
           (3,0):(4,0,R),
           (4,0):(5,1,L),
           (5,0):(6,0,L),
           (6,0):(7,0,L),
           (7,0):(0,0,C),
           (7,1):(8,1,C),
           (8,0):(9,0,R),
           (8,1):(8,1,L),
           (9,1):(10,0,R),
           (10,1):(10,1,R),
           (10,0):(11,0,R),
           (11,0):(12,0,R),
           (12,1):(13,1,R),
           (13,0):(12,0,R),
           (12,0):(5,1,L),
           (5,1):(5,1,L)}
word = str(input("input: "))
turingMachine(word, program)