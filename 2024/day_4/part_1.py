with open("input") as fichier:
    t = fichier.readlines()
    word = 'XMAS'

    total = 0
    for y, line in enumerate(t):
        for x, v in enumerate(line):
            if v == word[0]:  # X
                # print(f"X en [{y},{x}]")
                for vecteur in [[delta_x, delta_y] for delta_x in range(-1, 2) for delta_y in range(-1, 2)]:
                    # print(f"vecteur : {vecteur}")
                    for i in range(1, len(word)):
                        xx = x + vecteur[1] * i
                        yy = y + vecteur[0] * i
                        if xx < 0 or xx >= len(t[0]) or yy < 0 or yy >= len(t):
                            break
                        # print(f"test en [{yy},{xx}] : {t[yy][xx]}")
                        if t[yy][xx] != word[i]:
                            break
                        if i == len(word) - 1:
                            total += 1
                # print()
    print(total)
