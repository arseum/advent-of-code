def distance_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open("input") as fichier:
    t = []

    for line in fichier.read().splitlines():
        t += [list(line)]
        if 'S' in line:
            depart = (len(t) - 1, line.index('S'))
        elif 'E' in line:
            arrive = (len(t) - 1, line.index('E'))

    fifo = [depart]
    g_score = {depart: 0}
    f_score = {depart: distance_manhattan(depart, arrive)}
    chemin = {}
    direction = 1  # gauche — droite et 0 pour haut — bas

    while fifo:
        v = fifo.pop(0)
        # print("DEBUG: v=", v)
        # print("DEBUG: g_score =", g_score[v])
        # print("DEBUG: direction =", ["vertical","horizontal"][direction])

        if v == arrive:
            cout_total = g_score[v]
            while v in chemin:
                t[v[0]][v[1]] = '@'
                v = chemin[v]
            break

        for delta in range(-1, 2, 2):
            for d in [(0, 1), (1, 0)]:
                new_y = v[0] + delta * d[0]
                new_x = v[1] + delta * d[1]
                if 0 <= new_y < len(t) and 0 <= new_x < len(t[new_y]) and t[new_y][new_x] != '#':
                    bonus = 1000 * any([direction and new_y != v[0], not direction and new_x != v[1]])
                    g_score_temp = g_score[v] + 1 + bonus
                    if (new_y, new_x) not in g_score or g_score_temp < g_score[(new_y, new_x)]:
                        chemin[(new_y, new_x)] = v
                        g_score[(new_y, new_x)] = g_score_temp
                        f_score[(new_y, new_x)] = g_score_temp + distance_manhattan((new_y, new_x), arrive)
                        fifo += [(new_y, new_x)] if (new_y, new_x) not in fifo else []

        fifo = sorted(fifo, key=lambda point: f_score[point])
        if fifo:
            direction = chemin[fifo[0]][0] == fifo[0][0]

    # for line in t:
    #     print(''.join(line))
    print(cout_total)
