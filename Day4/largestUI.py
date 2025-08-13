def funct(ls, n):
    max_index = 0
    max_value = ls[0]

    for i in range(1, n):
        if ls[i] > max_value:
            max_value = ls[i]
            max_index = i

    return max_index

def main():
    ls = [1, 2, 3, 4, 5]
    n = len(ls)
    print(funct(ls, n))

main()
