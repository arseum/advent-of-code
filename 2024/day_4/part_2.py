with open("input") as fichier:
    t = [line.replace("\n", "") for line in fichier.readlines()]

    total = 0
    for y, line in enumerate(t):
        for x, v in enumerate(line):
            if v == 'A':
                # print()
                # print(f'A en [{y},{x}]')
                d = {'M': [], 'S': []}
                suivant = False
                for vecteur in [[delta_y, delta_x] for delta_y in range(-1, 2, 2) for delta_x in range(-1, 2, 2)]:
                    # print(vecteur)
                    yy = y + vecteur[0]
                    xx = x + vecteur[1]
                    # print(f"new y: {yy}, new x: {xx}")
                    if xx < 0 or xx >= len(t[0]) or yy < 0 or yy >= len(t) or t[yy][xx] not in d:
                        suivant = True
                        break
                    d[t[yy][xx]] += [(yy, xx)]
                if suivant:
                    continue
                else:
                    if len(d['M']) != len(d['S']):
                        break
                    b = d['M'][0][0] == d['M'][1][0] or d['M'][0][1] == d['M'][1][1]
                    if b:
                        total += 1
                    else:
                        print(d, b)
                        print('\n'.join(line[x-1:x+2] for line in t[y-1:y+2]))

    print(total)