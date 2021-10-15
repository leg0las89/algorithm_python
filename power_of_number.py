#How to calculate power of number using recursion

def power(num,expon):
    assert expon >= 0 and int(expon) == expon, "Please change number of exponent"
    if expon == 0:
        return 1
    if expon == 1:
        return num
    return num * power(num,expon - 1)


print(power(2,10))