def commonCharacterCount(s1, s2):
    count = 0
    for s in s1:
        if s in s2:
            print(s)
            count += 1
            s2 = s2.replace(s, '',1)
    return count



s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1, s2))