def findbad(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1
        
def almostIncreasingSequence(sequence):
    b = findbad(sequence)
    if b == -1:
        return True
    if findbad(sequence[b-1:b] + sequence[b+1:]) == -1:
        return True
    if findbad(sequence[b:b+1] + sequence[b+2:]) == -1:
        return True
    return False
    
        
print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))
print(almostIncreasingSequence([1, 3, 2]))


