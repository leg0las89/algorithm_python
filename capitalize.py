def capitalizeFirst(arr):
    result = []
    '''if len(arr) == 0:
        return result
    result.append(arr[0].title())
    return result + capitalizeFirst(arr[1:])'''
    for i in arr:
        result.append(i.title())
    return result

print(capitalizeFirst(["banana","apple","grape"]))