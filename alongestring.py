def allLongestStrings(inputArray):
    maxleng=0
    for i in range(len(inputArray)):
        if len(inputArray[i]) > maxleng:
            maxleng = len(inputArray[i])
            print(maxleng)
    new = [inputArray[j] for j in range(len(inputArray)) if len(inputArray[j]) == maxleng]
    return new

inputArray = ["aba", "aa", "ad", "vcd", "aba"]

print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))

print(allLongestStrings(["aa"]))