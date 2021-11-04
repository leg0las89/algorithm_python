def alternatingSums(a):
    b = []
    b.append(sum([a[i] for i in range(len(a)) if (i % 2) == 0]))
    b.append(sum([a[i] for i in range(len(a)) if (i % 2) != 0]))
    return b


print(alternatingSums([50, 60, 60, 45, 70]))