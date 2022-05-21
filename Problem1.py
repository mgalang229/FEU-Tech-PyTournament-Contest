def main():
    t = input()
    c = input()
    t = t.upper()
    c = c.upper()
    no_occurrences = True
    for i in range(len(t)):
        checker = True
        if i + len(c) < len(t):
            for j in range(len(c)):
                if c[j] != t[i + j]:
                    checker = False
            if checker:
                no_occurrences = False
                print(i + 1, i + len(c))
    if no_occurrences:
        print(0)

if __name__ == "__main__":
    main()
