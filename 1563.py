while(True):
    try:
        N = int(input())
        count = 0
        total = N * N
        for i in range(1, N + 1):
            for j in range(1, N+1):
                if j <= N%i:
                    count += 1
        if count != 0:
            if total % count == 0:
                total = total / count
                count = count / count
        print(int(count),"/",int(total))
    except EOFError:
        break

