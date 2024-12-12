with open("input") as fichier:
    d = {}
    max_x, max_y = 0, 0
    pos_antinode = set()

    for y, line in enumerate(fichier.readlines()):
        max_x = len(line) # attention cela fonctionne seulement car la dernière ligne ne contient pas le '\n'
        max_y += 1
        for x, v in enumerate(line[:-1]):
            if v != '.':
                d[v] = d.get(v, []) + [(y, x)]

    print(d, max_y, max_x)

    for v in d.values():
        for i, p1 in enumerate(v):
            for p2 in v[i + 1:]:
                vecteur = [p1[0] - p2[0], p1[1] - p2[1]]
                antinodes = [(p1[0] + vecteur[0], p1[1] + vecteur[1]), (p2[0] - vecteur[0], p2[1] - vecteur[1])]
                for a in antinodes:
                    if 0 <= a[0] < max_y and 0 <= a[1] < max_x:
                        pos_antinode.add((a[0], a[1]))

    print(len(pos_antinode))
