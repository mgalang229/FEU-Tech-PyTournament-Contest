import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

def main():
    pos_x , pos_y = map(int, input().split())
    z = int(input())
    ans = [0] * 2
    mn = 501
    for i in range(z):
        x, y = map(int, input().split())
        if get_distance(pos_x, pos_y, x, y) < mn:
            ans[0] = x
            ans[1] = y
            mn = get_distance(pos_x, pos_y, x, y)
    [print(x, end=" ") for x in ans]
    print()

if __name__ == "__main__":
    main()

