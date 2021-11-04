def addBorder(picture):
    t_star = "*" * (len(picture))
    with_star = [ '*' + i + '*' for i in picture]
    output = []
    output.append(t_star)
    for n in with_star:
        output.append(n)
    output.append(t_star)
    return output

print(addBorder(["abc", "ded"]))

