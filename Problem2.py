def main():
    d = int(input())
    ans = []
    for i in range(d):
        l1, c1, l2, c2 = map(int, input().split())
        ans.append(max(l1 * c1, l2 * c2))
    [print(x) for x in ans]

if __name__ == "__main__":
    main()

