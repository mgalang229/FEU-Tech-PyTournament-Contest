def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:m]
    a = set(a)
    b = set(b)
    s = list(a.intersection(b))
    if len(s) == 0:
        print("none")
    else:
        s.sort()
        [print(x, end=" ") for x in s]
        print()


if __name__ == "__main__":
    main()
