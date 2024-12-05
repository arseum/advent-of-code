with open("input") as fichier:
    # reports = [list(map(int, line.split())) for line in fichier.readlines()]
    t = 0
    for line in fichier.readlines():
        levels = list(map(int, line.split()))
        dif = [v - levels[i + 1] for i, v in enumerate(levels[:-1])]
        t += all([abs(sum(dif)) == sum(map(abs, dif)), max(dif) < 4, min(dif) > -4, 0 not in dif])
    print(t)
