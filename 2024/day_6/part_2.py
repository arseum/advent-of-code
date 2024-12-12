with open("input") as fichier:
    t = []

    ligne = {}
    col = {}

    vecteur = {
        '<': (0, -1),
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0)
    }

    for y, line in enumerate(fichier.readlines()):
        line = line.replace("\n", "")
        for x, v in enumerate(line):
            if v in vecteur:
                y_depart, x_depart = y, x
            elif v == '#':
                if y not in ligne:
                    ligne[y] = []
                if x not in col:
                    col[x] = []
                ligne[y] += [x]
                col[x] += [y]
        t.append(list(line))

    vecteurs = list(vecteur.keys())
    index_vecteur = vecteurs.index(t[y_depart][x_depart])


    def dedans(yy, xx):
        return 0 <= yy < len(t) and 0 <= xx < len(t[0])


    c = 0

    while 1:
        delta_y, delta_x = vecteur[vecteurs[index_vecteur]]
        if dedans(y_depart + delta_y, x_depart + delta_x):
            if t[y_depart + delta_y][x_depart + delta_x] == '#':
                index_vecteur += 1
                index_vecteur %= len(vecteurs)
            else:
                index_temp = (index_vecteur + 1) % len(vecteurs)
                y_temp, x_temp = y_depart, x_depart
                for i in range(5):
                    delta = vecteur[vecteurs[index_temp]]
                    if delta[0]:
                        ar_possible = (filter(lambda y: y > y_temp, col[x_temp]) if delta[0] > 0 else filter(
                            lambda y: y < y_temp, col[x_temp])) if x_temp in col else []
                    else:
                        ar_possible = (filter(lambda x: x > x_temp, ligne[y_temp]) if delta[1] > 0 else filter(
                            lambda x: x < x_temp, ligne[y_temp])) if y_temp in ligne else []
                    ar_possible = list(ar_possible)
                    if not ar_possible:
                        break
                    ar_possible = sorted(ar_possible)
                    if delta[0]:
                        y_temp = ar_possible[0] - 1 if delta[0] > 0 else ar_possible[-1] + 1
                    else:
                        x_temp = ar_possible[0] - 1 if delta[1] > 0 else ar_possible[-1] + 1

                    if delta[0] and y_temp == y_depart and any([index_temp == 1 and x_temp < x_depart, index_temp == 3 and x_temp > x_depart]):
                        print(y_depart, x_depart, " --- ", y_temp, x_temp, vecteurs[index_vecteur])
                        c += 1
                        break
                    elif delta[1] and x_temp == x_depart and any([index_temp == 0 and y_depart < y_temp, index_temp == 2 and y_depart > y_temp]):
                        print(y_depart, x_depart, " --- ", y_temp, x_temp, vecteurs[index_vecteur])
                        c += 1
                        break
                    index_temp += 1
                    index_temp %= len(vecteurs)

                y_depart += delta_y
                x_depart += delta_x
                t[y_depart][x_depart] = 'X'
        else:
            break

    print(c)

    # for l in t:
    #     print(''.join(l))
