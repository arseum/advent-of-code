def valid_level(diff: []):
    return all([abs(sum(diff)) == sum(map(abs, diff)), max(diff) < 4, min(diff) > -4, 0 not in diff])

def get_dif(level: []):
    return [v - level[i + 1] for i, v in enumerate(level[:-1])]

with open("input") as fichier:
    t = 0
    for line in fichier.readlines():
        levels = list(map(int, line.split()))
        t += any([valid_level(get_dif(lv)) for lv in [levels[:i] + levels[i + 1:] for i in range(len(levels) + 1)]])
    print(t)
