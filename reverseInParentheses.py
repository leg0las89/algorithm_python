def reverseInParentheses(inputString):
    slovo = list(inputString)
    open_bracket = []
    for num, val in enumerate(slovo):
        if val == "(":
            open_bracket.append(num)
        elif val == ")":
            p = open_bracket.pop()
            slovo[p:num] = slovo[num:p:-1]
    return "".join(i for i in slovo if i not in "()")


print(reverseInParentheses("foo(bar)baz"))