'''

Street Fighter 2 - Character Selection


https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python

'''


fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

initial_position = (0, 0)

moves = ["up"]+["left"]*6+["down"]+["right"]*6


def street_fighter_selection(fighters, initial_position, moves):

    i = initial_position[0]
    j = initial_position[1]

    cur_pos = fighters[i][i]

    ret = []

    for move in moves:
        if j == 5:
            j = -1
        if j == -6:
            j = 0
        if i > 1:
            i = -1
        if move == 'right':
            cur_pos = fighters[i][j + 1]
            j = j + 1
        if move == 'left':
            cur_pos = fighters[i][j - 1]
            j = j - 1
        if move == 'down':  # alguns erros aqui
            if i == 1:
                cur_pos = fighters[i][j]
            else:
                cur_pos = fighters[i + 1][j]
                i = i + 1
        if move == 'up':  # alguns erros aqui
            if i == 0:
                cur_pos = fighters[i][j]
            else:
                cur_pos = fighters[i - 1][j]
                i = i - 1
        ret.append(cur_pos)

    return ret


print(street_fighter_selection(fighters, initial_position, moves))
