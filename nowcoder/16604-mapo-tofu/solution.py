import sys


def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    ans = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        fair_count = data[idx:idx + n].count("0.500000")
        idx += n

        ans.append(str((1 << n) - (1 << (n - fair_count))))

    print("\n".join(ans))


if __name__ == "__main__":
    main()
