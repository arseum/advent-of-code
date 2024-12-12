with open("input") as fichier:
    t = []
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
                y_depart += delta_y
                x_depart += delta_x
                c += 1 if t[y_depart][x_depart] != 'X' else 0
                t[y_depart][x_depart] = 'X'
        else:
            break
    for l in t:
        print(''.join(l))
    print(c)
