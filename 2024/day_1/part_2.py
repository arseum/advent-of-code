with open("input") as fichier:
    mem = {}
    t1 = ""
    t2 = ""
    for line in fichier.readlines():
        l = line.split()
        t1 += l[0] + " "
        t2 += l[1] + " "
    t = 0
    for val in t1.split():
        if val not in mem:
            mem[val] = t2.count(val) * int(val)
        t += mem[val]
    print(t)
