def sortByHeight(a):
    sort = sorted([i for i in a if i > 0])
    c = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sort[c]
            c += 1

    return(a)

a = [-1, 150, 190, 170, -1, -1, 160, 180]

print(sortByHeight(a))