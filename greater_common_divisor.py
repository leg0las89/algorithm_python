#How to find GCD (Greatest Common Divisor) of two numbers using recursion

def gcd(a,b):
    print(a,b)
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(18,-48))