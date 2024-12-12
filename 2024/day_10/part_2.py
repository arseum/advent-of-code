# def f(value, y, x, n=0):
#     if value != n:
#         return 0
#     if value == 9:
#         return 1
#     k = []
#     for delta in range(-1, 2, 2):
#         for d in [(0, 1), (1, 0)]:
#             yy = y + delta * d[0]
#             xx = x + delta * d[1]
#             if 0 <= yy < len(t) and 0 <= xx < len(t[yy]):
#                 k += [f(t[yy][xx], yy, xx, n + 1)]
#     return sum(k)

def f_dur(value, y, x, n=0):
    return sum([f_dur(t[y + delta * d[0]][x + delta * d[1]], y + delta * d[0], x + delta * d[1], n + 1) for d in [(0, 1), (1, 0)] for delta in range(-1, 2, 2) if 0 <= y + delta * d[0] < len(t) and 0 <= x + delta * d[1] < len(t[y + delta * d[0]])]) if (value == n and value < 9) else (value == n and value == 9)


with open("input") as fichier:
    t = [list(map(int, line)) for line in fichier.read().splitlines()]
    # print(*[list(map(f_dur, line, [y] * len(line), range(len(line)))) for y, line in enumerate(t)], sep='\n')
    print(sum([sum(map(f_dur, line, [y] * len(line), range(len(line)))) for y, line in enumerate(t)]))
