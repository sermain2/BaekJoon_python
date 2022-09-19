import sys
t = int(sys.stdin.readline())
for i in range(t):
    k = list(map(int, sys.stdin.readline().rstrip().split()))
    print(k[0] + k[1])