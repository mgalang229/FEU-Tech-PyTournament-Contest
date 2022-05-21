def main():
    m, n = map(int, input().split())
    a = list(map(int, input().split()))[:m]
    new_a = [0] * m
    for i in range(m):
        new_a[(i + n) % m] = a[i]
    ans = 0
    for i in range(m):
        ans += (new_a[i] * i)
    print(ans)


if __name__ == "__main__":
    main()
