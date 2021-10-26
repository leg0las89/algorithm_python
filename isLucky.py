def isLucky(n):
    main = [int(i) for i in str(n)]
    middle = len(main)/2
    if sum(main[:int(len(main)/2)]) == sum(main[int(len(main)/2):]): return True
    else: return False
    print(sum(main[:int(len(main)/2)]))



print(isLucky(1230))
print(isLucky(239017))