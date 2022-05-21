def main():

    # 1
    # ans = 1

    # 1 0
    # 0 1
    # ans = 2

    # 1 0 1
    # 0 1 0
    # 1 0 1
    # ans = 5

    # 1 0 1 0
    # 0 1 0 1
    # 1 0 1 0
    # 0 1 0 1
    # ans = 8

    # 1 0 1 0 1
    # 0 1 0 1 0
    # 1 0 1 0    1
    # 0 1 0 1    0
    # 1 0 1 0    1

    # 1 0 1 0 1 0
    # 0 1 0 1 0 1
    # 1 0 1 0 1 0
    # 0 1 0 1 0 1
    # 1 0 1 0 1 0
    # 0 1 0 1 0 1

    n = int(input())
    a = []
    for i in range(n):
        temp = list(map(int, input().strip().split()))[:n]
        a.append(temp)

    if n == 0:
        print("Uncolorable")
        return

    zeroes1 = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                zeroes1 += 1

    # for row in a:
    #     for col in row:
    #         print(col, end=" ")
    #     print()

    vec = []
    for i in range(n):
        temp = []
        for j in range(n):
            # print((i + j) % 2, end=" ")
            temp.append((i + j) % 2)
        # print()
        vec.append(temp)
    
    zeroes2 = 0
    for row in vec:
        for col in row:
            if col == 0:
                zeroes2 += 1

    if zeroes1 >= zeroes2:
        print("Colorable")
        return

    vec = []
    for i in range(n):
        temp = []
        for j in range(n):
            # print((i + j) % 2, end=" ")
            temp.append((i + j + 1) % 2)
        # print()
        vec.append(temp)

    zeroes2 = 0
    for row in vec:
        for col in row:
            if col == 0:
                zeroes2 += 1

    if zeroes1 >= zeroes2:
        print("Colorable")
        return

    print("Uncolorable")



if __name__ == "__main__":
    main()
