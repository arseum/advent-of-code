def f(update):
    for index, page in enumerate(update):
        for indexx, val_before in enumerate(update[:index]):
            if page in d[val_before]:
                update[index], update[indexx] = val_before, page
                return f(update)
    return update[len(update) // 2 ]

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
                        somme += f(updates)
                        break
                if not good:
                    break

    print(somme)