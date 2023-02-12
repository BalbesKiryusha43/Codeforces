for _ in range(int(input())):
    m = int(input())
    a = list(map(int, input().split()))
    ln = 1
    x = 0
    while ln < m:
        for i in range(0, m, ln * 2):
            if a[i + ln - 1] > a[i + ln]:
                if a[i] > a[i + ln * 2 - 1]:
                    a[i:i + ln], a[i + ln:i + ln * 2] = a[i + ln:i + ln * 2], a[i:i + ln]
                    x += 1
                else:
                    print(-1)
                    break
        else:
            ln *= 2
            continue
        break
    else:
        print(x)
