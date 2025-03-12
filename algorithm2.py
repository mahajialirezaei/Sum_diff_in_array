

lst = [3, 7, 4, 5]

def boosted_algorithm(lst, n):
    sum = 0
    lst.sort()
    for i in range(int(n/2)):
        sum += -1 * (n-1-(i * 2)) * lst[i]
    for i in range(int(n/2)):
        sum += +1 * (n-1-(i * 2)) * lst[n - 1 - i]



    return sum


lst1 = [3, 7, 4, 5, 1]
print(boosted_algorithm(lst, 4))
print(boosted_algorithm(lst1, 5))