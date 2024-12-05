with open("input") as fichier:
    d = {0: [], 1: []}
    _ = [d[i].append(int(v)) for line in fichier.readlines() for i, v in enumerate(line.split())]
    t1 = sorted(d[0])
    t2 = sorted(d[1])
    print(sum([abs(v - t2[i]) for i, v in enumerate(t1)]))

# with open("input") as fichier:
#     t1 = []
#     t2 = []
#     for line in fichier.readlines():
#         l = line.split()
#         t1 += [int(l[0])]
#         t2 += [int(l[1])]
#     t1 = sorted(t1)
#     t2 = sorted(t2)
#     print(sum([abs(v - t2[i]) for i, v in enumerate(t1)]))