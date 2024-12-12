def f(value, y, x, n=0, pos_9=None):
    if pos_9 is None:
        pos_9 = set()
    if value != n:
        return 0
    if value == 9:
        pos_9.add((y, x))
        return
    for delta in range(-1, 2, 2):
        if 0 <= y + delta < len(t):
            f(t[y + delta][x], y + delta, x, n + 1, pos_9)
        if 0 <= x + delta < len(t[y]):
            f(t[y][x + delta], y, x + delta, n + 1, pos_9)
    return len(pos_9)

with open("input") as fichier:
    t = [list(map(int, line)) for line in fichier.read().splitlines()]
    # print(*[list(map(f, line, [y] * len(line), range(len(line)))) for y, line in enumerate(t)], sep='\n')
    print(sum([sum(map(f, line, [y] * len(line), range(len(line)))) for y, line in enumerate(t)]))
