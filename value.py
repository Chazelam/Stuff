class exp:
    big = [4.57, 20000]
    mid = [6.57, 5000]

class arts:
    gold = [1.07, 3780]
    pyrple = [2.48, 2520]
    blue = [3.55, 1260]

class tea:
    mora = [10000*20, 120*20]
    big_exp = [20*20000, 120*20]
    resin = [60, 1200]
    big_ess = [10000*5, 360*5]
    ess = [2500*20, 90*20]

exp = exp()
arts = arts()
tea = tea()
average_exp = exp.big[0]*exp.big[1] + exp.mid[0]*exp.mid[1]
average_art = arts.gold[0]*arts.gold[1] + arts.pyrple[0]*arts.pyrple[1] + arts.blue[0]*arts.blue[1]
exp_in_teapot = tea.big_exp[0] / average_exp
art_in_teapot = tea.ess[0] / average_art
print(exp_in_teapot)
print(art_in_teapot)