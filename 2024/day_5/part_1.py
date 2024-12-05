with open("input") as fichier:
    d = {}
    somme = 0
    for line in fichier.readlines():
        if '|' in line:
            right, left = map(int, line.split('|'))
            if left not in d:
                d[left] = []
            d[left] += [right]
        elif ',' in line:  # éviter ligne vide
            updates = list(map(int, line.split(',')))
            good = True
            for index, page in enumerate(updates):
                for val_before in updates[:index]:
                    if page in d[val_before]:
                        good = False
                        break
                if not good:
                    break
            if good:
                somme += updates[len(updates) // 2 ]
    print(somme)